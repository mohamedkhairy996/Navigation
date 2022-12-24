import DATA
from DATA import *
import math
graph = DATA.graph
#----------------------------------------------------------------------
def hestimatedDistance(start_node,end_node):
    Radius = 6373.0 #the radius of the earth
    latitude1 = math.radians(start_node[0]) #  khat el 3ard
    longitude1 = math.radians(start_node[1]) # khat el tool
    latitude2 = math.radians(end_node[0]) #  khat el 3ard
    longitude_2 = math.radians(end_node[1]) # khat el tool
    distanceLatitude = latitude2 - latitude1
    distance_Longitude = longitude_2 - longitude1
    a = math.sin(distanceLatitude / 2) ** 2 + math.cos(latitude1) * math.cos(latitude2) * math.sin(distance_Longitude / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    #https://wiki.hsoub.com/%D9%90Algorithms/distance_2_points_on_earth
    return Radius * c
#------------------------------------------------------------------------------

global hestimatedTable
hestimatedTable = {}
#----------------------------------------------------------------------
def A_star(start,goal):
    for val in DATA.coordinates:
        hestimatedTable[val] = hestimatedDistance(DATA.coordinates[val], DATA.coordinates[goal])
    visited = []
    queue = [[(start , 0)]]
    while queue:
        queue.sort(key=path_f_cost)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal :
            return path
        else:
            neighbour =graph.get(node , [])
            for (node2 , cost) in neighbour:
                new_path = path.copy()
                new_path.append((node2,cost))
                queue.append(new_path)


#----------------------------------------------------------------------

#------------------------------------------------------------------------------
def path_f_cost(path):
    g_cost = 0
    for (node, cost) in path:
        g_cost += float(cost)
    last_node = path[-1][0]
    h_cost = hestimatedTable[last_node]
    f_cost = int(h_cost) + g_cost
    return f_cost, last_node,g_cost

#------------------------------------------------------------------------------


