# otevření souboru GeoJSON v Pythonu
# mode "r" - čtení, "w" - zápis - smaže celý soubor a rovnou začne psát.
#
#

import json
import operator

with open("import.geojson", "r", encoding="utf-8") as f:
    dataD = json.load(f)

print(type(dataD))

def show_coordinates(json_data):
    """loads coordinates from GEOjson into list"""
    global IdCoord_D
    IdCoord_D={};  coordinates_list = []
    for x in json_data["features"]:
        #coordinates_data = (x["geometry"]["coordinates"])
        value= (x["geometry"]["coordinates"])
        key=(x["id"]).replace ("node/","")
        IdCoord_D[key] =value #Dictionary d = dict([ (<key>, <value>), (<key>, <value),......)

        coordinates_list.append(value)
    print(IdCoord_D) ;print()
    return(coordinates_list)
coordinates_list = show_coordinates(dataD)

IdCoord_D_sort = sorted(IdCoord_D.items(), key=operator.itemgetter(0))
#print (IdCoord_D_sort )

for  pol in (IdCoord_D_sort):
    print (pol)


def bounding_box(list):
    """find max and min in coordinates data"""
    maxcoords = max(list)
    print("max x:", maxcoords[0])
    print("max y:", maxcoords[1])
    mincoords = min(list)
    print("min x:", mincoords[0])
    print("min y:", mincoords[1])


bounding_box(coordinates_list)