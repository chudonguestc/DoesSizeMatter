import numpy as np
import json as js

with open('geo.json') as json_data:
    geo = js.load(json_data)

for i in range(len(geo['features'])):
    geo['features'][i]['id'] = i

with open("geo_id.json", "w") as outfile:
    js.dump(geo, outfile)

