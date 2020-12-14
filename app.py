from flask import Flask, jsonify, abort, make_response, request
from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict
import requests, json, math


api = 'yourapikey'
url = 'https://api.stm.info/pub/od/gtfs-rt/ic/v1/vehiclePositions'
hdr = { 'apikey' : api }

def init():
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.post(url, headers=hdr)
    feed.ParseFromString(response.content)
    json_string = MessageToDict(feed)

    with open('data.json', 'w') as f:
        f.write(json.dumps(json_string, indent=2))
init()

app = Flask(__name__)

@app.route('/stm/api/v1.0/locations', methods=['GET'])
def get_all():
    with open('data.json', 'r') as f:
        return json.loads(f.read())

@app.route('/stm/api/v1.0/locations/bus/<string:busId>/', methods=['GET'])
def get_bus(busId):
    with open('data.json') as f:
        data = json.load(f)
    results = []
    for bus in data['entity']:
        if busId == bus['vehicle']['trip']['routeId']:
            results.append(bus)    
    if len(results) > 0:
        return jsonify(results)
    else:
        return jsonify({'error': 'no matches found'})

@app.route('/stm/api/v1.0/locations/busnearby/<string:busId>/<string:lat>/<string:long>/', methods=['GET'])
def findabus(busId, lat, long):
    coords = (float(lat), float(long))
    
    def calculateDistance(x1, y1, x2, y2): 
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) * 100  
        return round(dist, 2)

    with open('data.json') as f:
        data = json.load(f)
    results = []
    for bus in data['entity']:
        id = bus['vehicle']['trip']['routeId']
        locations = bus['vehicle']['position']['latitude'], bus['vehicle']['position']['longitude']
        distance = calculateDistance(locations[0], locations[1], coords[0], coords[1])
        if busId == id:
            results.append({
                'busId' : busId,
                'coords' : locations,
                'km' : distance,
            })
    if len(results) > 0:
        return jsonify(results)
    else:
        return jsonify({'error': 'no matches found'})

@app.errorhandler(404)
def not_found(error):
    print(error)
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
