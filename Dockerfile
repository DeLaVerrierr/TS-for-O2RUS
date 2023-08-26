FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /route

COPY requirements.txt /route/
RUN pip install -r requirements.txt

COPY . /route/


RUN apt-get update && apt-get install -y sqlite3

RUN python route/manage.py collectstatic --noinput
RUN python route/manage.py createsuperuser --noinput --username=admin --email=admin@example.com

EXPOSE 8000

RUN useradd -ms /bin/bash route
USER route

CMD ["python", "route/manage.py", "runserver", "0.0.0.0:8000"]

