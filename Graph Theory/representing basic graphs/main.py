from collections import deque

def create_adj_list(edges, num_nodes):
    adj_list = [[] for _ in range(num_nodes)]
    
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    return adj_list

def printDepth(depthNum):
    depthString = ""
    for num in range(depthNum):
        depthString += "-"*4

    return f"{depthString}>"


### Performs BFS on network graph
def print_adj_list(adj_list):
    startNode = 0 # 0 being the Root node
    visited = [False]* len(adj_list)
    queue = []
    depth = 0

    # Append start node and start depth to the queue and set the startNode to visited
    queue.append([startNode, depth])
    visited[startNode] = True

    while len(queue) != 0:

        currentNode, depth = queue[-1]
        queue.pop()
        
        #print(f"{printDepth(depth)} {nodeNameMap[currentNode]['name']}")

        for i, child in enumerate(adj_list[currentNode]):
            if visited[child] == False:
                visited[child] = True
                queue.append([child, depth+1])


        print(printDepth(depth), nodeNameMap[currentNode]["name"])

        

nodes = ["FirwWall-00", "Switch-00", "AP-01", "AP-02", "AP-03", "Switch-01", "AP-11"]
nodeNameMap = {}
edges = [(0, 1), (1, 2), (1, 3), (1, 4), (0, 5), (5, 6)]


for i, device in enumerate(nodes):
    nodeNameMap[i] = {
        "isRoot": i == 0, # Not currently used
        "name": device
    }

depthList = []
dephtString = ""

adj_list = create_adj_list(edges, len(nodes))
print_adj_list(adj_list),
