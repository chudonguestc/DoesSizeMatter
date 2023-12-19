# adding ids
import json as js

with open('world_merge.json') as json_data:
    geo = js.load(json_data)

for i in range(len(geo['features'])):
    geo['features'][i]['id'] = geo['features'][i]['properties']['name']

# delete the overall USA because treated as states
for i in range(len(geo['features'])):
    if (geo['features'][i]['id'] == "United States of America"):
        geo['features'].remove(geo['features'][i])
        break

    # geo['features'][i]['id'] = i
with open("world_merge_plotly.json", "w") as outfile:
    js.dump(geo, outfile)



# # print csv values
# import pandas as pd
#
# # Replace 'your_file.csv' with the path to your CSV file
# file_path = 'world_merge.csv'
#
# # Load the CSV file into a DataFrame
# df = pd.read_csv(file_path)
#
# # Display the DataFrame
# print(list(df.nb_breweries))