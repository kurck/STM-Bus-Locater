# STM BUS LOCATER

This app is used to find where in Montreal a specific bus is, so you don't have to wait so long for it. It uses the GPS coords of the bus to give you an accurate location.

## Documentation

* [Python3](https://www.python.org/downloads/)
* [flask](https://flask.palletsprojects.com/en/1.1.x/installation/#install-flask)
* [gtfs-realtime-bindings](https://developers.google.com/transit/gtfs-realtime/examples/python-sample)
* [requests](https://pypi.org/project/requests/)

# Important/Helpful links

* You will need to obtain an API key from the [STM website](https://developpeurs.stm.info/) to use this app. Without this key the app will not run. You must register an account and follow the instructions.

*  To make this app useful, you'll want to add your own GPS coordinates. Go to [gps-coordinates.net](https://www.gps-coordinates.net/). Use the DD (decimal degrees) format and not the DMS (degrees, minutes, seconds).

### Installation

```bash
pip install flask
pip install gtfs-realtime-bindings
pip install requests
```

# API

### All busses

```bash
GET /stm/api/v1.0/locations
```

Sample success response:

```json
{
  "entity": [
    {
      "id": "25203", 
      "isDeleted": false, 
      "vehicle": {
        "currentStatus": "IN_TRANSIT_TO", 
        "currentStopSequence": 23, 
        "position": {
          "latitude": 45.468166, 
          "longitude": -73.56605
        }, 
        "timestamp": "1607917279", 
        "trip": {
          "routeId": "71", 
          "startDate": "20201213", 
          "startTime": "22:18:00", 
          "tripId": "221331010"
        }, 
        "vehicle": {
          "id": "25203"
        }
      }
    }, 
```
Sample error response:

```json
{
  "error": "Not found"
}
```
### Specific bus

```bash
GET /stm/api/v1.0/locations/bus/<busNumber>
```

Sample success response:

```json
[
  {
    "id": "36002", 
    "isDeleted": false, 
    "vehicle": {
      "currentStatus": "STOPPED_AT", 
      "currentStopSequence": 9, 
      "position": {
        "latitude": 45.463085, 
        "longitude": -73.646515
      }, 
      "timestamp": "1607917284", 
      "trip": {
        "routeId": "51", 
        "startDate": "20201213", 
        "startTime": "22:36:00", 
        "tripId": "222772045"
      }, 
      "vehicle": {
        "id": "36002"
      }
    }
  }, 
```
Sample error response:

```json
{
  "error": "Not found"
}
```
### Closest bus to you

```bash
GET /stm/api/v1.0/locations/busnearby/<busNumber>/<lat>/<long>/
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