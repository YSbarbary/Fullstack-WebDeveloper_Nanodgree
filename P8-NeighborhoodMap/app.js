var infowindow;

var Location = function (title, lng, lat, venueId ){
  var self = this;
  this.title = title;
  this.location = {lat: lat, lng: lng};
  this.venueId = venueId;

  this.infowindow = new google.maps.InfoWindow();
  this.streetViewService = new google.maps.StreetViewService() ;
  this.marker = new google.maps.Marker({
    position: new google.maps.LatLng(self.location.lng, self.location.lat),
    map: map,
    title: self.title,
    animation: google.maps.Animation.DROP
  });

  this.getContent = function() {
    var topTips = [];
    var venueUrl = 'https://api.foursquare.com/v2/venues/' + self.venueId + '/tips?sort=recent&limit=3&v=20170509&client_id=0QU44M2WZUWRQB1LW2TNAA2RBUXAK2L3HUWJ2JMZNHLOGM4N&client_secret=KINEOKCMXZ31P23Y4GMPZ2TVNGJJTOXYKXAPZGXGAL3IJRQ2';

    $.getJSON(venueUrl,
      function(data) {
        $.each(data.response.tips.items, function(i, tips){
          // foursquare api has bug that doesn't limit the number of responses
          if (i < 5) {topTips.push('<li>' + tips.text + '</li>'); }
        });

      }).done(function(){

        self.content = '<h2>' + self.title + '</h2>' + '<h3>5 Most Recent Comments</h3>' + '<ol>' + topTips.join('') + '</ol>';
      }).fail(function(jqXHR, textStatus, errorThrown) {
        self.content = '<h2>' + self.title + '</h2>' + '<h3>5 Most Recent Comments</h3>' + '<h4>Oops. There was a problem retrieving this location\'s comments.</h4>';
        console.log('getJSON request failed! ' + textStatus);
      });
    }();

    this.closeAllInfowindows = function() {
      for (var i=0; i < viewModel.locations.length; i++) {
        viewModel.locations[i].infowindow.close();
      }
    };

    this.nullAllMarkers = function() {
      for (var i=0; i < viewModel.locations.length; i++) {
        viewModel.locations[i].marker.setMap(null);
      }
    };

    this.showInfoWindow = function() {
      for (var i=0; i < viewModel.locations.length; i++) {
        viewModel.locations[i].infowindow.close();
        viewModel.locations[i].marker.setMap(null);
      }
      //self.streetViewService.getPanoramaByLocation(self.marker.position, 50, self.getStreetView);
      map.panTo(self.marker.getPosition());
      infowindow.setContent(self.content);
      self.marker.setMap(map);
      self.bounceMarker();
      infowindow.open(map, self.marker);
    };

    this.getStreetView = function()  {

    };

    this.bounceMarker = function () {
      if (self.marker.getAnimation() !== null) {
        self.marker.setAnimation(null);
      } else {
        self.marker.setAnimation(google.maps.Animation.BOUNCE);
        window.setTimeout(function() {
          self.marker.setAnimation(null);
        }, 1500);
      }
    };


    self.marker.addListener('click', function() {
      self.closeAllInfowindows();
      self.streetViewService.getPanoramaByLocation(self.marker.position, 50, self.getStreetView);
      infowindow.setContent(self.content);
      self.bounceMarker();
      self.marker.setMap(map);
      infowindow.open(map, self.marker);
    });

    // this.addListener = google.maps.event.addListener(self.marker, 'click', (this.openInfowindow));
  };

  var model = {
    locations: ko.observableArray([{
      title: 'Heliopolis Sporting Club',
      venueId: '4b87bd16f964a52086c931e3',
      location: {
        lat: 30.0886895,
        lng: 31.3163998
      }
    },
    {
      title: 'Cairo Jazz Club',
      venueId: '4bae84e1f964a52018bc3be3',
      location: {
        lat: 30.0619985,
        lng: 31.2119196
      }
    },
    {
      title: 'Baron Empain Palace',
      venueId: '4e5baceee4cd875e8eca83cd',
      location: {
        lat: 30.0870458,
        lng: 31.3298284
      }
    },
    {
      title: 'Il Mulino',
      venueId: '4e76427788775d593e541839',

      location: {
        lat: 29.969811,
        lng: 31.2750256
      }
    },
    {
      title: 'The Westin Cairo Golf Resort & Spa Katameya Dunes',
      venueId: '57a4466c498ef02574b8a6f8',
      location: {
        lat: 30.0032417,
        lng: 31.5228921
      },

    },
    {
      title: 'The Saladin Citadel of Cairo',
      venueId: '4cee65cb3b03f04deec239dc',
      location: {
        lat: 30.0293603,
        lng: 31.2617308
      }
    }
  ]),
};

var viewModel = {

  locations: ko.observableArray(),
  query: ko.observable(''),
};

viewModel.instantiateLocations = function () {
  for (i=0,len = model.locations().length; i < len; i++)
  {
    var location = new Location(model.locations()[i].title, model.locations()[i].location.lat, model.locations()[i].location.lng, model.locations()[i].venueId);
    viewModel.locations.push(location);
  }
};


// Search function for filtering through the list of locations based on the name of the location.
viewModel.search = ko.dependentObservable(function() {
  var self = this;
    // self.instantiateLocations();
  var search = this.query().toLowerCase();
    return ko.utils.arrayFilter(self.locations(),function(location) {
    if (location.title.toLowerCase().indexOf(search) < 0) {location.marker.setMap(null); }
    if (location.title.toLowerCase().indexOf(search) >= 0) {location.marker.setMap(map); }
    return location.title.toLowerCase().indexOf(search) >= 0;
  });
}, viewModel);



function hideAllListings () {
  for (var i=0; i < this.locations.length; i++){
    viewModel.locations[i].marker.setMap(null);
  }
}

function showAllListings() {
  for (var i=0; i < this.locations.length; i++){
    viewModel.locations[i].marker.setMap(map);
  }
}

function initMap() {
  // Constructor creates a new map - only center and zoom are required.
  map = new google.maps.Map(document.getElementById('map'), {
    center: {
      lat: 29.969811,
      lng: 31.2750256
    },
    zoom: 15,
    mapTypeControl: false
  });
  viewModel.instantiateLocations();
  infowindow = new google.maps.InfoWindow();
}

function googleError() {
  alert("Error loadings the maps API. Please check your internet connection");
}

ko.applyBindings(viewModel);