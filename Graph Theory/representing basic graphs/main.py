import networkx
import matplotlib.pyplot
import json

def create_adj_list(edges, num_nodes):
    adj_list = [[] for _ in range(num_nodes)]
    
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    return adj_list

def printDepth(depthNum):
    if depthNum == 0:
        return ""
    
    depthString = ""
    for num in range(depthNum):
        depthString += "-"*4
    
    depthString = depthString[:(4//2) *depthNum] + "" + depthString[:(4//2)*depthNum]

    return f"{depthString}> "


### Performs DFS on network graph
def getNodeHierarchy(adj_list):
    startNode = 0 # 0 being the Root node
    visited = [False]* len(adj_list)
    queue = []
    
    depth = 0
    nodeHierarchy = [{}] * len(adj_list)  

    # Append start node and start depth to the queue and set the startNode to visited
    queue.append([startNode, depth])
    visited[startNode] = True

    #children = 0
    while len(queue) != 0:
        currentNode, depth = queue[-1]
        queue.pop()

        children = 0
        
        for i, child in enumerate(adj_list[currentNode]):
            if visited[child] == False:
                visited[child] = True
                queue.append([child, depth+1])
                children += 1

        nodeHierarchy[currentNode] = {
            "name": nodeNameMap[currentNode]['name'],
            "children": children,
            "depth": depth, ### If Depth == 0, then node Is Root
        }

    return nodeHierarchy

nodes = ["FirwWall-00", "Switch-00", "AP-01", "AP-02", "AP-03", "Switch-01", "AP-11"]
edges = [(0, 1), (1, 2), (1, 3), (1, 4), (0, 5), (5, 6)]

nodeNameMap = {}
nodeList = []

for i, device in enumerate(nodes):
    nodeList.append(i)
    nodeNameMap[i] = {
        "isRoot": i == 0, # Not currently used
        "name": device
    }


adj_list = create_adj_list(edges, len(nodes))
nodeHiearchy = getNodeHierarchy(adj_list)

#print(json.dumps(nodeHiearchy, indent=4))
for node in nodeHiearchy:
    print("-"*4*node['depth'], node['name'], node['children'])
