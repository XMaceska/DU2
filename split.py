# otevření souboru GeoJSON v Pythonu
# mode "r" - čtení, "w" - zápis - smaže celý soubor a rovnou začne psát.
#
#

import json, quadtree


with open("import.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)

print(type(data))

def show_coordinates(json_data):
    """loads coordinates from GEOjson into list"""
    global coordinates_data
    coordinates_list = []
    for x in json_data["features"]:
        coordinates_data = (x["geometry"]["coordinates"])
        coordinates_list.append(coordinates_data)
    print(coordinates_list)
    return(coordinates_list)


coordinates_D = show_coordinates(data)
bounding_box(coordinates_D)

id = []


new_json = quadtree.quadtree(data,x_mid,y_mid,y_len, x_len,id,)

gj_structure = {"type": "FeatureCollection"}
gj_structure["features"] = new_json


with open("output.geojson", "w", encoding="utf-8") as f:
    json.dump(gj_structure,f, indent =2)

