var map = L.map('map').setView([47.222078, 39.720358], 6); //

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    var waypoints = [
        L.latLng(47.222078, 39.720358), // Ростов
        L.latLng(43.115542, 131.885494)  // Владик
    ];

// Добавляем информацию о маршруте
var route = L.Routing.control({
    waypoints: waypoints,
    routeWhileDragging: true,
    show: false     // убрал описание маршрута
}).on('routesfound', function(event) {
    var route = event.routes[0];
    var distance = route.summary.totalDistance; // Расстояние в метрах
    var duration = route.summary.totalTime; // Время в секундах

    // Преобразование времени в часы и минуты
    var hours = Math.floor(duration / 3600);
    var minutes = Math.floor((duration % 3600) / 60);

    // Вывод информации на странице
    var infoDiv = document.createElement('div');
    infoDiv.innerHTML = 'Расстояние: ' + (distance / 1000).toFixed(2) + ' км<br>' +
                        'Время: ' + hours + ' ч ' + minutes + ' мин';
    document.querySelector('.route-detail').appendChild(infoDiv);
}).addTo(map);
