

datalist = []
ID_cluster = 0


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