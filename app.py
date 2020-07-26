from flask import Flask, jsonify, abort, make_response, request
import json

app = Flask(__name__)

@app.route('/stm/api/v1.0/locations', methods=['GET'])
def read():
    with open('data.json', 'r') as f:
        return json.loads(f.read())

@app.route('/stm/api/v1.0/locations/bus/<string:busId>/', methods=['GET'])
def get_bus(busId):
    with open('data.json') as f:
        data = json.load(f)
    results = []
    buses = data['entity']
    for bus in buses:
        if busId == bus['vehicle']['trip']['routeId']:
            results.append(bus)    
    if len(results) > 0:
        return jsonify(results)
    else:
        return jsonify({'error': 'no matches found'})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
