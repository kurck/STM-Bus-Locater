# STM BUS LOCATER

This app is used to find where in Montreal a specific bus is, so you don't have to wait so long for it. It uses the GPS coords of the bus to give you an accurate location.

## Documentation

* [Python3](https://www.python.org/downloads/)
* [flask](https://flask.palletsprojects.com/en/1.1.x/installation/#install-flask)
* [gtfs-realtime-bindings](https://developers.google.com/transit/gtfs-realtime/examples/python-sample)
* [requests](https://pypi.org/project/requests/)

# Important/Helpful links

* You will need to obtain an API key from Google to use this app. Without this key the app will not run. Follow these [instruction](https://developers.google.com/maps/documentation/directions/get-api-key) to get your API key.

*  To make this app useful, you'll want to add your own GPS coordinates. Go to [gps-coordinates.net](https://www.gps-coordinates.net/). Use the DD (decimal degrees) format and not the DMS (degrees, minutes, seconds).

### Installation

```bash
pip install flask
pip install gtfs-realtime-bindings
pip install requests
```

# API

```bash
GET http://localhost:5000/stm/api/v1.0/locations/busnearby/<busNumber>/<lat>/<long>/
```

Sample success response:

```json
{
    "busId": "51", 
    "coords": [
      45.48427, 
      -73.628716
    ], 
    "km": 0.19
  }, 
```

Sample error response:

```json
{
  "error": "Not found"
}
```

# Usage

1. Download app.py
2. Install all dependencies in the above Installation section
3. Enter [your API key](https://developers.google.com/maps/documentation/directions/get-api-key) in the place of ```'yourapikey'``` on line 7 of app.py
4. Run app.py
5. Open your browser and paste in (without pressing enter):
```bash
http://localhost:5000/stm/api/v1.0/locations/busnearby/<busNumber>/<lat>/<long>/
```
6. Enter the bus number you want to locate in place of <busNumber>
7. Enter your latitude and longitude in place of <lat> and <long> respectively.
8. Press enter