function initMap() {
    // Constructor creates a new map - only center and zoom are required.
    map = new google.maps.Map(document.getElementById('map'), {
        center: {
            lat: 30.0293603,
            lng: 31.2617308
        },
        zoom: 13,
        mapTypeControl: false
    });
}
