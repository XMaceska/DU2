

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
    len_x = abs(maxcoords[0] - mincoords[0]) / 2
    len_y = abs(maxcoords[1] - mincoords[1]) / 2
    print(mid_x, mid_y)
    return bouding_box_list, mid_x, mid_y, len_x, len_y


bounding_box(coordinates_D)


def quadtree (json_data,x_mid,y_mid,len_y, len_x, id,quad = 0):
    """quad-tree function, recursive"""
    new_json = []
    NW = []
    NE = []
    SW = []
    SE = []

    if len(json_data) < 50:
        print("ok")
        new_id = id[0]
        for i in json_data:
            i["properties"]["cluster_id"] = new_id
            new_json.append(i)
            print(new_json)
            id.append(new_id + 1)
    if quad == 1:
        x_mid = x_mid - len_x*2
        y_mid = y_mid + len_y

    elif quad == 2:
        x_mid = x_mid + len_x*2
        y_mid = y_mid + len_y

    elif quad == 3:
        x_mid = x_mid - len_x*2
        y_mid = y_mid - len_y

    elif quad == 4:
        x_mid = x_mid + len_x*2
        y_mid = y_mid - len_y

    for u in json_data:
        x, y = u[coordinates_data]

        if x < x_mid and y > y_mid:
            NW.append(u)
        elif x > x_mid and y > y_mid:
            NE.append(u)
        elif x < x_mid and y < y_mid:
            SW.append(u)
        elif x < x_mid and y < y_mid:
            SE.append(u)
        else:
            print("out")
    quadtree(NW,x_mid, y_mid, len_x, len_y, id, quad = 1)
    quadtree(NE,x_mid, y_mid, len_x, len_y, id, quad = 2)
    quadtree(SW,x_mid, y_mid, len_x, len_y, id, quad = 3)
    quadtree(SE,x_mid, y_mid, len_x, len_y, id, quad = 4)

    return new_json,id