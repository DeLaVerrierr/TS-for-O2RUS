from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, get_user
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .forms import RegisterUserForm, ProfileForm
from .models import Profile, Route


def index(request):
    ''' Отображает главную страницу приложения '''
    routes = Route.objects.all()
    context = {'routes': routes}
    return render(request, 'main/index.html', context)

def route_detail(request, route_id):
    route = get_object_or_404(Route, pk=route_id)
    context = {'route': route}
    return render(request, 'main/route_detail.html', context)


def login_user(request):
    ''' Обрабатывает запрос на вход пользователя в систему.
     Если запрос отправлен методом POST и данные формы валидны,
    производится аутентификация пользователя и перенаправление на главную страницу.
    В противном случае отображается страница входа с формой аутентификации '''
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm(request)
    return render(request, 'main/login.html', {'form': form})


class RegisterUser(CreateView):
    ''' Представляет форму регистрации пользователя.
    При валидации формы происходит сохранение нового пользователя
    и автоматический вход в систему '''
    form_class = RegisterUserForm
    template_name = 'main/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)  # Автоматический вход пользователя
        return response


class LoginUser(LoginView):
    ''' Представляет форму входа пользователя.
    После успешной аутентификации пользователь перенаправляется
    на главную страницу. '''
    template_name = 'main/login.html'
    success_url = reverse_lazy('home')


class LogoutUser(LogoutView):
    ''' Представляет функциональность выхода пользователя из системы. '''
    next_page = reverse_lazy('login')


def register(request):
    ''' Обрабатывает запрос на регистрацию пользователя.
    Если запрос отправлен методом POST и данные формы валидны,
    производится сохранение нового пользователя и автоматический вход в систему,
    после чего пользователь перенаправляется на главную страницу.
    В противном случае отображается страница регистрации с формой. '''
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход пользователя
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, 'main/register.html', {'form': form})


@login_required
def profile(request):
    ''' Отображает страницу профиля пользователя.
    Если запрос отправлен методом POST и данные формы валидны,
    происходит сохранение профиля пользователя.
    Если профиль уже существует, он обновляется.
    Если профиля нет, создается новый.
    После сохранения профиля пользователь перенаправляется на страницу профиля. '''
    user = request.user
    profile = user.profile if hasattr(user, 'profile') else None

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user  # Set the user for the profile
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile, initial={'user': user})

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'main/profile.html', context)



@login_required
def edit_profile(request):
    '''  Отображает страницу редактирования профиля пользователя.
    Если запрос отправлен методом POST и данные формы валидны, происходит сохранение профиля пользователя.
    Если профиль уже существует, он обновляется.
    Если профиля нет, создается новый.
    После сохранения профиля пользователь перенаправляется на страницу профиля. '''
    user = request.user
    if not hasattr(user, 'profile'):
        profile = Profile.objects.create(user=user)
    else:
        profile = user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            new_username = form.cleaned_data['username']
            if new_username != user.username:
                if User.objects.filter(username=new_username).exists():
                    form.add_error('username', 'This username is already taken.')
                else:
                    user.username = new_username
            user.email = form.cleaned_data['email']
            new_password = form.cleaned_data['new_password']
            if new_password:
                user.set_password(new_password)
                user.save()
            else:
                user.save()

            form.save()
            return redirect('profile')
    else:
        if profile:
            form = ProfileForm(instance=profile)
        else:
            form = ProfileForm(initial={'username': user.username, 'email': user.email})

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'main/edit_profile.html', context)





