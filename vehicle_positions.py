from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict
import requests, json

api = 'apikey'
url = 'https://api.stm.info/pub/od/gtfs-rt/ic/v1/vehiclePositions'
hdr = { 'apikey' : api }

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.post(url, headers=hdr)
feed.ParseFromString(response.content)
json_string = MessageToDict(feed)

# Saves all the STM data into data.json
with open('data.json', 'w') as f:
    f.write(json.dumps(json_string, indent=2))

# Deletes unused data and saves only bus ID's and locations to busId.json
with open('data.json') as f:
    data = json.load(f)
for entity in data['entity']:
    del entity['id'], entity['isDeleted'], entity['vehicle']['trip']['tripId'], entity['vehicle']['trip']['startTime'], entity['vehicle']['trip']['startDate'], entity['vehicle']['currentStopSequence'], entity['vehicle']['currentStatus'], entity['vehicle']['timestamp'], entity['vehicle']['vehicle']
with open('busId.json', 'w') as f:
    json.dump(data, f, indent=2)
