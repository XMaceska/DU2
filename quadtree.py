

datalist = []
ID_cluster = 0


def divide(data, north, south, east, west):
    """ this function divides cluster only if there is more than 50 point is cluster """
    """ recursion function"""
    if len(data) < 5:
        global datalist
        global ID_cluster
        for i in data:
            datalist = [(i[0] , i[1])] = ID_cluster
        ID_cluster = +1
        return data
    else:


