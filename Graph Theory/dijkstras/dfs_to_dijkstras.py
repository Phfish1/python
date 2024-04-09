

def find_neighbours(graph, row, column):
    ### Checks if index exists, then checks if you can go to neighbour AKA if number == 1 
    ### THEN Check if vertex is marked / already visited
    ### Row vertecies represents the directions (UP, DOWN) and the column_vertecies the directions (LEFT, RIGHT)
    ### THEN we return valid_paths AKA all the directions we can move in from the specified vertecy

    row_vertecies = [-1, +1, 0, 0]
    column_vertecies = [0, 0, -1, +1]

    valid_paths = []

    for direction in range(0, 4):
        next_row = row + row_vertecies[direction]
        next_column = column + column_vertecies[direction]

        if ( (0 <= next_row < len(graph)) and (0 <= next_column < len(graph[0])) ): ### UP
            if graph[next_row][next_column] != 0:
                valid_paths.append([next_row, next_column])

    return valid_paths

def dfs(graph, row, column): ### Row + Collumn representing the vertex 
    if row == (len(graph) -1) and column == (len(graph[0]) -1): ### Returns True when last vertex in maze is hit
        return True
    
    #marked_maze[row][column] = True # Shows program you have already been to this vertex

    next_paths = find_neighbours(graph, row, column)

    
    for path in next_paths: ### Explores every path possible, but if there are no more vertixes to visit go back (recursivly) until you can visit one or if paths are depleted
        if dfs(graph, path[0], path[1]): ### IF last vertex is hit:
            #true_path.append([path[0], path[1]]) ### retrace paths back to start (not needed anymore though)
            return True

    
    return False



## if new_path has-less-cost than old path, replace shortest_path
shortest_path = {
    "path": [],
    "cost": 9999
}
