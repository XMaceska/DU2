# otevření souboru GeoJSON v Pythonu
# mode "r" - čtení, "w" - zápis - smaže celý soubor a rovnou začne psát.


import json


with open("import.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)


def show_coordinates(json_data):
    """loads coordinates from GEOjson into list"""
    coordinates_list = []
    for x in json_data["features"]:
        coordinates_data = (x["geometry"]["coordinates"])
        coordinates_list.append(coordinates_data)
    print(coordinates_list)
    return(coordinates_list)


coordinates_list = show_coordinates(data)


def bounding_box(list):
    """find max and min in coordinates data"""
    maxcoords = max(list)
    print("max x:", maxcoords[0])
    print("max y:", maxcoords[1])
    mincoords = min(list)
    print("min x:", mincoords[0])
    print("min y:", mincoords[1])


bounding_box(coordinates_list)

