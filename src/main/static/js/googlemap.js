function initMap() {
  // The location of Uluru
  var _lat = parseFloat(document.querySelector('#map').dataset.lat);
  var _lng = parseFloat(document.querySelector('#map').dataset.lng);
  var loc = {lat: _lat, lng: _lng};
  console.log(loc);
  var uluru = {lat: -25.344, lng: 131.036};
  console.log(uluru);
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 18, center: loc});
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({position: loc, map: map});
}

