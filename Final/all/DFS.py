import DATA

#----------------------------------------------
global visited,dfsPath,graph
dfsPath = []
visited = set()
graph = DATA.nodesGraph
#-----------------------------------------------
def dfs(start_node,stop_node):
    while start_node not in visited and stop_node not in visited:
        dfsPath.append(start_node)
        visited.add(start_node)
        for neighbour in graph[start_node]:
            if stop_node in visited:
                break
            else:
                dfs(neighbour,stop_node)
    return dfsPath
