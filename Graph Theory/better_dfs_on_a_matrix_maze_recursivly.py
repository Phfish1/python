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

#print(f"\033[91m {variable} \033[00m")

def draw_maze(maze, row, column):
    maze_string = ""
    print(row, column)
    print(len(maze)-1, len(maze[0])-1)

    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            #if row == (len(maze)-1 and column == len(maze[0])-1):
            #    print("WAIIIIIT")
            #    maze_string += f"\033[92m{maze[0][0]}\033[00m, " # Marks the starting point 
            if (row == i and column == j) or [j, i] in explored_paths:
                explored_paths.append([j, i])
                maze_string += f"\033[91m{maze[i][j]}\033[00m, "
            elif i == 0 and j == 0:
                maze_string += f"\033[92m{maze[0][0]}\033[00m, " # Marks the starting point 
            else:
                maze_string += f"{maze[i][j]}, "
        maze_string += f"\n"
    

    print(maze_string)
    print("------------------------------")

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
    if row == (len(maze) -1) and column == (len(maze[0]) -1): ### Returns True when last vertex in maze is hit
        true_path.append([row, column])
        return true_path
    
    marked_maze[row][column] = True # Shows program you have already been to this vertex

    next_paths = find_neighbours(graph, row, column)

    #print(next_paths)
    #if len(next_paths) > 0:
    #    draw_maze(graph, next_paths[0][0], next_paths[0][1])

    for path in next_paths:
        if dfs(graph, path[0], path[1]): ### Then if there are no more vertixes to visit, go back (recursivly) until you can visit one
            true_path.append([path[0], path[1]])
            draw_maze(graph, path[0], path[1])
            return true_path
    
    ### and when there are no more vertixes to visit, 
    return 



explored_paths = []
true_path = []
marked_maze = mark_vertexes(maze)
true_path = dfs(maze, 0, 0)


### Printing

if true_path != None:
    is_solvable = True
else:
    is_solvable = False

print("------------------------------")
print(f"Is the MAZE solvable: {is_solvable}")
print("------------------------------")


#print(list(reversed(true_path)))
#for path in list(reversed(true_path)):
#    draw_maze(maze, path[0], path[1])

