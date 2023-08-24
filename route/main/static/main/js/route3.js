var map = L.map('map').setView([43.115542, 131.885494], 6); //

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    var waypoints = [
        L.latLng(43.115542, 131.885494), // Владик
        L.latLng(48.480229, 135.071917), // хабаровск
        L.latLng(50.257486, 127.534047), // благовещинск
        L.latLng(52.289901, 104.279572), // иркутц
        L.latLng(52.033635, 113.501049), // чита
        L.latLng(53.736227, 119.766047),
        L.latLng(51.999517, 127.675930),
        L.latLng(53.195211, 50.097125),  // самара
        L.latLng(51.768085, 55.096400), // оренбург
        L.latLng(55.160279, 61.401372), // челяба
        L.latLng(53.347310, 83.776399), // барнаул
        L.latLng(42.057669, 48.288776)  // Дембрент
    ];


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
