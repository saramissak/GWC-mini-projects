var map;
var loc;//location
var view;
var i;

function panToCountry(){
	/*
    The goal of this function is to pan to the country specified by the user input.
    While writing the steps, consider for instance how there might be an error that prevents you from doing the step.
    (E.g. 1a, 3a.)
    The steps we need to do would be to:
    1) Get the country entered by the user
      1a) Make sure the country is entered in the first place
    2) Use REST countries to get the country info by SENDING A REQUEST
    3) Read the response and try to get the latitude and longitude from it.
      3a) Handle the case that the server isn't reachable
      3b) Display some message if the country couldn't be found
    4) Pass the latitude and longitude to the Openlayers by animating the view to pan to it.
  */
  // Step one: Gets the input from user
	var countryName = document.getElementById("country-name").value;
  // Step 1a: Checks to see if there is an input in the box. If there isn't, function ends.
	if(countryName === "") {
	 	alert("You didn't enter a country name!");
	 	return;
	}
  // This part of the code only occurs if the return statement doesn't occur: if there is a country name.
  // STEP 2: From API documentation: https://restcountries.eu/#api-endpoints-name
  //    we see that the url we need to make the request to is "https://restcountries.eu/rest/v2/name/{name}"
  //    so we make that url with the country the user inputs.
	var query = "https://restcountries.eu/rest/v2/name/"+countryName;
  // this line replaces all the spaces in the query (in case the user input something like "United States") with %20
  //    because that's how urls are formatted (%20 means space.)
	query = query.replace(/ /g, "%20");
  // These next 3 lines send the request
	var countryRequest = new XMLHttpRequest(); // makes the new request
	countryRequest.open('GET', query, false); // gives the new request the details (uses GET, sends to the url at query, and is not asynchronous)
	countryRequest.send();  // sends the request.
	// Step 3a: looks at the status of the response
  //    Consult this link for status codes and their meanings: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
  // Basicaly, the only good readyState is 4, the only good status is 200. In addition, we want the response text to not be empty.
  //  So, if the ready state is NOT 4, or if the status is NOT 200, or if we have a blank responseText, then something went wrong.
  //    When something goes wrong, we'll log the error to console, and then end the function here.
	if(countryRequest.readyState != 4 || countryRequest.status != 200 || countryRequest.responseText === "") {
	 	window.console.error("Request had an error!");
	 	return;
	}
	// Step 3: Assuming everything went right, we need to change the response text into JSON. We do so by using
  // JSON.parse(), and pass what we're parsing to it. Parse just means to read. So we're reading the text in
  // responseText as a JSON object.
	var countryInformation = JSON.parse(countryRequest.responseText);
	// Take a look at a sample response here: https://restcountries.eu/rest/v2/name/China
  //    You'll see that the JSON response is a LIST of countries that match the search.
  //      It's a list because all the info is between these brackets: []
  //    So we'll take the first country in the list by calling countryInformation[0] because lists are 0 indexed.
  //    Next, you'll see that in each country's information, there is a value called "latlng".
  //    Calling countryInformation[0].latlng is the SAME as countryInformation[0]["latlng"]. Choose what is most readable for YOU.
  //    We also see that latlng is a list (2 values between []). Since it's called latlng, we can assume that the first element
  //      is latitude and the second is longituded, so we'll store this in a variable.
	var lat = countryInformation[0].latlng[0];
	var lon = countryInformation[0].latlng[1];
  // Just as we did in init(), we convert the latitude and longitude to an openlayer projection
	var location = ol.proj.fromLonLat([lon, lat]);
	// Just as we did in button(), we animate it to that location.
	view.animate({
		center: location, // Location
		duration: 2000  // Two seconds You can change this!
	});
}
function button(){
  view.animate({center:loc});
}
function init(){
  i = 0;
  loc = ol.proj.fromLonLat( [-73.97,40.78]);
  view = new ol.View({
    center: loc,
    zoom: 6
  });
  map = new ol.Map({
    view: view,
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    target: 'map'
  });
}


function next(){
  var myCountries = ["china", "germany", "mexico", "nigeria"];

  var country = myCountries[i];

  var query = "https://restcountries.eu/rest/v2/name/"+country;
  query = query.replace(/ /g, "%20");

  //alert(query);

  var countryRequest = new XMLHttpRequest(); // makes the new request
  countryRequest.open('GET', query, false); // gives the new request the details (uses GET, sends to the url at query, and is not asynchronous)
  countryRequest.send();

  if(countryRequest.readyState != 4 || countryRequest.status != 200 || countryRequest.responseText === "") {
    window.console.error("Request had an error!");
    return;
  }

  var countryInformation = JSON.parse(countryRequest.responseText);

  var lat = countryInformation[0].latlng[0];
  var lon = countryInformation[0].latlng[1];
  // Just as we did in init(), we convert the latitude and longitude to an openlayer projection
  var location = ol.proj.fromLonLat([lon, lat]);
  // Just as we did in button(), we animate it to that location.
  view.animate({
    center: location, // Location
    duration: 2000  // Two seconds You can change this!
  });
  if (query == "https://restcountries.eu/rest/v2/name/china"){
    alert("Here is China!");
  }
  if (query == "https://restcountries.eu/rest/v2/name/germany"){
    alert("Here is Germany!");
  }
  if (query == "https://restcountries.eu/rest/v2/name/mexico"){
    alert("Here is Mexico!");
  }
  if (query == "https://restcountries.eu/rest/v2/name/nigeria"){
    alert("Here is Nigeria!");
  }


  i += 1;

  if (i >= myCountries.length){
    i = 0;
  }

}




window.onload = init;

/*
i=0
countries[i]
countryRequest = new XMLHttpRequest(); // makes the new request
countryRequest.open('GET', query, false); // gives the new request the details (uses GET, sends to the url at query, and is not asynchronous)
countryRequest.send();
  countryInformation;
  location = ol.proj.fromLonLat([lon, lat]);
i = i + 1 */
