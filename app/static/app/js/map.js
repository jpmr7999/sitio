// Inicializar el mapa con Leaflet
var mymap = L.map('map').setView([-36.794849879040726, -73.06227239445289], 13);

// Agregar una capa de mapa base de OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);

// Opcional: agregar un marcador en una ubicación específica
var marker = L.marker([51.5, -0.09]).addTo(mymap);