def draw_graph(nodeHierarchy):
    # Convert nodeHierarchy list to a dictionary for easy lookup
    node_dict = {node['name']: node for node in nodeHierarchy}
    
    # Create an adjacency list to keep track of parent-child relationships
    adj_list = {node['name']: [] for node in nodeHierarchy}
    for node in nodeHierarchy:
        for child in nodeHierarchy:
            if child['depth'] == node['depth'] + 1:
                adj_list[node['name']].append(child['name'])
    
    def draw_node(node, depth):
        # Draw the current node centered with respect to its depth
        spacing = " " * (4 * depth)
        print(f"{spacing}{node['name']}")
        
        # Recursively draw children nodes
        for child_name in adj_list[node['name']]:
            draw_node(node_dict[child_name], depth + 1)

    # Start drawing from the root node
    root = next(node for node in nodeHierarchy if node['depth'] == 0)
    draw_node(root, 0)

# Example data
nodeHierarchy = [
    {
        "name": "FirwWall-00",
        "children": 2,
        "totalChildren": 6,
        "depth": 0
    },
    {
        "name": "Switch-00",
        "children": 3,
        "totalChildren": 3,
        "depth": 1
    },
    {
        "name": "AP-01",
        "children": 0,
        "totalChildren": 0,
        "depth": 2
    },
    {
        "name": "AP-02",
        "children": 0,
        "totalChildren": 0,
        "depth": 2
    },
    {
        "name": "AP-03",
        "children": 0,
        "totalChildren": 0,
        "depth": 2
    },
    {
        "name": "Switch-01",
        "children": 1,
        "totalChildren": 1,
        "depth": 1
    },
    {
        "name": "AP-11",
        "children": 0,
        "totalChildren": 0,
        "depth": 2
    }
]

# Draw the graph
draw_graph(nodeHierarchy)
