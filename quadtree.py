def bounding_box(list):
    """find max and min in coordinates data"""
    global x_mid
    global y_mid
    global x_len
    global y_len
    maxcoords = max(list)
    print("max x:", maxcoords[0])
    print("max y:", maxcoords[1])
    mincoords = min(list)
    print("min x:", mincoords[0])
    print("min y:", mincoords[1])
    bouding_box_list = [[maxcoords[0],maxcoords[1],mincoords[0],mincoords[1]]]
    x_mid = (maxcoords[0] + mincoords[0]) / 2
    y_mid = (maxcoords[1] + mincoords[1]) / 2
    x_len = abs(maxcoords[0] - mincoords[0]) / 2
    y_len = abs(maxcoords[1] - mincoords[1]) / 2
    print(x_mid, y_mid)
    return bouding_box_list, x_mid, y_mid, x_len, y_len


def quadtree (json_data, x_mid, y_mid, y_len, x_len, id, quad = 0):
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
        x_mid = x_mid - x_len * 2
        y_mid = y_mid + y_len

    elif quad == 2:
        x_mid = x_mid + x_len * 2
        y_mid = y_mid + y_len

    elif quad == 3:
        x_mid = x_mid - x_len * 2
        y_mid = y_mid - y_len

    elif quad == 4:
        x_mid = x_mid + x_len * 2
        y_mid = y_mid - y_len

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
    quadtree(NW, x_mid, y_mid, x_len, y_len, id, quad = 1)
    quadtree(NE, x_mid, y_mid, x_len, y_len, id, quad = 2)
    quadtree(SW, x_mid, y_mid, x_len, y_len, id, quad = 3)
    quadtree(SE, x_mid, y_mid, x_len, y_len, id, quad = 4)

    return new_json,id
