maze = [
[1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ] ,
[1, 0, 1, 0, 1, 1, 1, 1, 0, 1 ] ,
[1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ] ,
[0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ] ,
[1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ] ,
[1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ] ,
[1, 0, 1, 0, 0, 0, 0, 0, 0, 1 ] ,
[1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ] ,
[1, 1, 0, 0, 0, 1, 1, 1, 0, 1 ]
]

def mark_vertexes(graph):
    marked_vertexes = []

    for i in range(0, len(graph)):
        marked_vertexes.append([])
        for j in range(0, len(graph[i])):
            marked_vertexes[i].append(False) # "Creates identical matrix and marks the vertix position False" print(i, j, maze[i][j]) 

    return marked_vertexes

def visit_neighbours(graph, row, column):
    ### Checks if index exists, then checks if you can go to neighbour AKA if number == 1 
    ### THEN Check if vertex is marked / already visited
    ### Then if you can visit it and it is not already visited visit it

    if (0 <= row-1 < len(graph)): ### UP
        if graph[row-1][column] != 0:
            if not marked_maze[row-1][column]:
                print("UP")
                dfs(graph, row-1, column)

    if (0 <= row+1 < len(graph)): ### DOWN
        if graph[row+1][column] != 0:
            if not marked_maze[row+1][column]:
                print("DOWN")
                dfs(graph, row+1, column)

    if (0 <= column-1 < len(graph[row])): ### LEFT
        if graph[row][column-1] != 0:
            if not marked_maze[row][column-1]:
                print("LEFT")
                dfs(graph, row, column-1)

    if (0 <= column+1 < len(graph[row])): ### RIGHT
        if graph[row][column+1] != 0:
            if not marked_maze[row][column+1]:
                print("RIGHT")
                dfs(graph, row, column+1)

    return

def dfs(graph, row, column): ### Row + Collumn representing the vertex 
    marked_maze[row][column] = True # Shows program you have already been to this vertex
    
    if marked_maze[-1][-1]: ### This is just to catch extra recursion
        return

    visit_neighbours(graph, row, column) ### Then if there are no more vertixes to visit, go back (recursivly) until can visit one
    ### and when there are no more vertixes to visit, 

    if marked_maze[-1][-1]:
        return True
    else:
        return False




marked_maze = mark_vertexes(maze)
is_solvable = dfs(maze, 0, 0)

print("------------------------------")
print(f"Is the MAZE solvable: {is_solvable}")
print("------------------------------")
