from time import sleep

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

def draw_maze(maze, row, column):
    maze_string = ""

    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            if ( (row == len(maze)-1 and column == len(maze[0])-1) and (i == len(maze)-1 and j == len(maze[0])-1) ) :
                maze_string += f"\033[92m{maze[i][j]}\033[00m, "
            elif (row == i and column == j):
                explored_paths.append([i, j])
                maze_string += f"\033[91m{maze[i][j]}\033[00m, " # Marks current Vertex
            elif [i, j] in explored_paths:
                maze_string += f"\033[91m{maze[i][j]}\033[00m, " # Marks already visited vertexes, [IN current path] "See explored_paths.pop()" in dfs()
            elif i == 0 and j == 0:
                maze_string += f"\033[92m{maze[0][0]}\033[00m, " # Marks the starting point 
            else:
                maze_string += f"{maze[i][j]}, "

        maze_string += f"\n"
    
    sleep(0.2)
    print(f"\r{maze_string}")
    print("------------------------------",)

def mark_vertexes(graph):
    marked_vertexes = []

    for i in range(0, len(graph)):
        marked_vertexes.append([])
        for j in range(0, len(graph[i])):
            marked_vertexes[i].append(False) # "Creates identical matrix and marks the vertix position False" print(i, j, maze[i][j]) 

    return marked_vertexes

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
                if not marked_maze[next_row][next_column]:
                    valid_paths.append([next_row, next_column])

    return valid_paths

def dfs(graph, row, column): ### Row + Collumn representing the vertex 
    if row == (len(graph) -1) and column == (len(graph[0]) -1): ### Returns True when last vertex in maze is hit
        return True
    
    marked_maze[row][column] = True # Shows program you have already been to this vertex

    next_paths = find_neighbours(graph, row, column)

    
    for path in next_paths: ### Explores every path possible, but if there are no more vertixes to visit go back (recursivly) until you can visit one or if paths are depleted
        draw_maze(graph, path[0], path[1])
        if dfs(graph, path[0], path[1]): ### IF last vertex is hit:
            #true_path.append([path[0], path[1]]) ### retrace paths back to start (not needed anymore though)
            return True

    try:
        explored_paths.pop()
    except:
        print("ERROR: no more paths to explore ;(")
    
    return False


explored_paths = [] ### could be used to draw true_path after
#true_path = [] ### true_path no longer needed,
marked_maze = mark_vertexes(maze)


is_solvable = dfs(maze, 0, 0)

print(f"Is the MAZE solvable: \033[1m{is_solvable}\033[00m")
print("------------------------------")


