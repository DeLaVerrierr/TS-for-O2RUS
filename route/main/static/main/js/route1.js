var map = L.map('map').setView([53.354779, 83.769783], 6); // Координаты Барнаула

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var waypoints = [
    L.latLng(53.354779, 83.769783), // Барнаул
    L.latLng(55.030199, 82.920430), // Новосибирск
    L.latLng(54.989342, 73.368212), // Омск
    L.latLng(53.507821, 49.420330), // Тальяти
    L.latLng(42.057669, 48.288776)  // Дембрент
];

// Добавляем невидимые маркеры для Новосибирска и Омска
for (var i = 1; i < waypoints.length - 1; i++) {
    L.marker(waypoints[i], {
        icon: L.divIcon({className: 'invisible-icon'}),
        zIndexOffset: -1000 // Сдвиг z-index для скрытия маркеров под маршрутом
    }).addTo(map);
}

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
