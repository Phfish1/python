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
def getNodeHierarchy(adj_list, nodeIndexMap):
    visited = [False] * len(adj_list)
    nodeHierarchy = [{}] * len(adj_list)

    def dfs(node, depth):
        visited[node] = True
        children = 0
        total_descendants = 0

        for child in adj_list[node]:
            if not visited[child]:
                visited[child] = True
                children += 1
                descendants = dfs(child, depth + 1)
                total_descendants += descendants + 1  # Include the child itself

        nodeHierarchy[node] = {
            "name": nodeIndexMap[node]['name'],
            "children": children,
            "totalChildren": total_descendants, ### This will be HUGE LATER, if example website / graphic display
            "depth": depth  # If Depth == 0, then node Is Root
        }

        return total_descendants

    dfs(0, 0)
    return nodeHierarchy


def printNodeHierarchy(nodeHierarchy):
    #print(json.dumps(nodeHierarchy, indent=4))

    ### PROBLEM 1, Find out how to get which edge each node is connected to its parent from

    for node in nodeHierarchy:
        if node["depth"] == 0:
            print(f"\033[1m{node['name']}\033[0m")
        else:
            print(f"{' '*node['depth']*5} \033[30;3mFrom\033[0m \033[4mG0/0\033[0m \033[30;3mto\033[0m \033[4mG0/1\033[0m \033[1m{node['name']}\033[0m")




def main():
    nodes = ["FirwWall-00", "Switch-00", "AP-01", "AP-02", "AP-03", "Switch-01", "AP-11"]
    edges = [(0, 1), (1, 2), (1, 3), (1, 4), (0, 5), (5, 6)]

    nodeIndexMap = {}

    for i, device in enumerate(nodes):
        nodeIndexMap[i] = {
            "isRoot": i == 0, # Not currently used
            "name": device
        }


    adj_list = create_adj_list(edges, len(nodes))
    nodeHierarchy = getNodeHierarchy(adj_list, nodeIndexMap)

    printNodeHierarchy(nodeHierarchy)
    #print(json.dumps(nodeHierarchy, indent=4))




if __name__ == "__main__":
    main()
