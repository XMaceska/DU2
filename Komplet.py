# otevření souboru GeoJSON v Pythonu
# mode "r" - čtení, "w" - zápis - smaže celý soubor a rovnou začne psát.
#
#

import json
import operator

with open("import.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)
features = data["features"]

new_json = []



def show_coordinates(json_data):
    """loads coordinates from GEOjson into list"""
    coordinates_list = []
    for x in json_data["features"]:
        coordinates_data = (x["geometry"]["coordinates"])
        coordinates_list.append(coordinates_data)
    print(coordinates_list)
    return(coordinates_list)


coordinates_D = show_coordinates(data)

#
def bounding_box(list):
    """find max and min in coordinates data"""
    global mid_x
    global mid_y
    global len_x
    global len_y
    maxcoords = max(list)
    print("max x:", maxcoords[0])
    print("max y:", maxcoords[1])
    mincoords = min(list)
    print("min x:", mincoords[0])
    print("min y:", mincoords[1])
    bouding_box_list = [[maxcoords[0],maxcoords[1],mincoords[0],mincoords[1]]]
    mid_x = (maxcoords[0] + mincoords[0])/2
    mid_y = (maxcoords[1] + mincoords[1])/2
    len_x = abs(maxcoords[0] - mincoords[0])/2
    len_y = abs(maxcoords[1] - mincoords[1])/2
    print(mid_x,mid_y)
    return bouding_box_list, mid_x, mid_y, len_x, len_y

bounding_box(coordinates_D)

def quadtree (json_data,x_mid,y_mid,id,quad):
    """quad-tree function, recursive"""
    quad = 0
    if len(json_data) < 50:
        print("ok")
        new_id = id[0]
        for i in json_data:
            i["properties"]["cluster_id"] = new_id
            new_json.append(i)
            print(new_json)
        if quad == 1:
            x_mid = x_mid - len_x
            y_mid = y_mid + len_y

        elif quad == 2:
            x_mid = x_mid + len_x
            y_mid = y_mid + len_y

        elif quad == 3:
            x_mid = x_mid - len_x
            y_mid = y_mid - len_y

        elif quad == 4:
            x_mid = x_mid + len_x
            y_mid = y_mid - len_y



