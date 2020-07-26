import json
import math  

us = (45.485792, -73.627534)
# reqbus = input('What bus?: ')
reqbus = '51'
def calculateDistance(x1, y1, x2, y2): 
    # print(x1, y1, x2, y2)
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) * 100  
    return dist
def findabus():
    with open('busId.json') as f:
        data = json.load(f)
    for busId in data['entity']:
        busNumber = busId['vehicle']['trip']['routeId']
        locations = busId['vehicle']['position']['latitude'], busId['vehicle']['position']['longitude']
        distance = calculateDistance(locations[0], locations[1], us[0], us[1])
        if reqbus == busNumber:
            result = [reqbus]
            result.append(locations)
            result.append(distance)
            x = result
            print(x)

findabus()

  
print calculateDistance(x1, y1, x2, y2)