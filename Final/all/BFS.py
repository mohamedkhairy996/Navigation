import DATA
import cv2

def bfs(start_node, stop_node):
    graph = DATA.nodesGraph
    points = DATA.points
    visited = []
    queue = []
    data = []
    visited.append(start_node)
    data.append(start_node)
    queue.append(start_node)
    title = "Route from " + start_node + " to " + stop_node + " using BFS"      # giving title to window
    global flag
    global end
    end = start_node
    img2 = cv2.imread(r'map.png', 1)
    while queue:
        m = queue.pop(0)
        if m == start_node:
            cv2.circle(img2, points[m], 7, (0, 0, 255), -1)
        elif m == stop_node:
            cv2.circle(img2, points[m], 7, (255, 255, 0), -1)
        else:
            cv2.circle(img2, points[m], 7, (128, 128, 128), -1)
        if end == stop_node and end in visited:
            break
        else:
            neighbors = []
            for neighbour in graph[m]:
                neighbors.append(neighbour)
                # you must draw the path here mr mohamed
                if neighbour == start_node:
                    cv2.circle(img2, points[neighbour], 7, (0, 0, 255), -1)
                elif neighbour == stop_node:
                    cv2.circle(img2, points[neighbour], 7, (255, 255, 0), -1)
                else:
                    cv2.circle(img2, points[neighbour], 7, (128, 128, 128), -1)
                cv2.arrowedLine(img2, points[m], points[neighbour], (0, 0, 0), 2)
                cv2.imshow(title, img2)
                cv2.waitKey(1000)
                if neighbour not in visited:
                    visited.append(neighbour)
                    data.append(neighbour)
                    queue.append(neighbour)
                    if neighbour == stop_node and neighbour in visited:
                        flag = 1
                        end = neighbour
                        break
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return visited