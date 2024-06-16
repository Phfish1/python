from time import sleep

matrix = [
[ 1, 1, 11 ] ,
[ 4, 5, 1 ] ,
[ 7, 8, 9 ]
]

matrix = [
 [1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
 [1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
 [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
 [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
 [0, 0, 1, 0, 1, 1, 1, 0, 1, 1],
 [1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
 [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
 [0, 1, 1, 1, 1, 1, 1, 0, 1, 1]
]

def mark_vertexes(graph):
    marked_vertexes = []

    for i in range(0, len(graph)):
        marked_vertexes.append([])
        for j in range(0, len(graph[i])):
            marked_vertexes[i].append(False) # "Creates identical matrix and marks the vertix position False" print(i, j, maze[i][j]) 

    return marked_vertexes

def draw_maze(maze, row, column, path, realtime):
    maze_string = ""

    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            #print(i, len(maze)-1, j, len(maze[0])-1)
            if ( (row == len(maze)-1 and column == len(maze[0])-1) and (i == len(maze)-1 and j == len(maze[0])-1) ):
                maze_string += f"\033[92m{maze[i][j]}\033[00m, "
            elif i == 0 and j == 0:
                maze_string += f"\033[92m{maze[0][0]}\033[00m, " # Marks the starting point 
            elif (row == i and column == j):
                maze_string += f"\033[91m{maze[i][j]}\033[00m, " # Marks current Vertex
            elif [i, j] in path:
                if (i == len(maze)-1 and j == len(maze[0])-1):
                    maze_string += f"\033[92m{maze[i][j]}\033[00m, "
                else:
                    maze_string += f"\033[91m{maze[i][j]}\033[00m, " # Marks already visited vertexes, [IN current path] "See explored_paths.pop()" in dfs()
            else:
                maze_string += f"{maze[i][j]}, "

        maze_string += f"\n"
    
    if realtime:
        print(f"{maze_string}", end='\r')
        sleep(0.01)
        for line in maze_string.splitlines():
            print("\033[1A", end="\x1b[2K")
    else:
        print(f"{maze_string}")
        print("---------------------")

def find_neighbours(graph, row, column):
    ### Checks if index exists
    ### Row vertecies represents the direction (DOWN) and the column_vertecies the direction (RIGHT)
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


    row_vertecies = [-1, +1, 0, 0]
    column_vertecies = [0, 0, -1, +1]

    valid_paths = []

    for direction in range(0, 4):
        next_row = row + row_vertecies[direction]
        next_column = column + column_vertecies[direction]

        if ( (0 <= next_row < len(graph)) and (0 <= next_column < len(graph[0])) ):
            if not marked_maze[next_row][next_column]:
                if graph[next_row][next_column] != 0:
                    valid_paths.append([next_row, next_column])

    return valid_paths

def dijkstras(graph, row, column, shortest, draw, report): ### Row + Collumn representing the vertex 
    global current_cost
    global current_path
    global shortest_path
    global marked_maze

    if row == (len(graph) -1) and column == (len(graph[0]) -1): ### Returns True when last vertex in maze is hit
        if do_shortest:
            if current_cost < shortest_path["cost"]: ### For shortest path
                shortest_path["path"] = current_path.copy() ### Use copy, OR else shortest_path["path"] will be BOUND to the current_path
                shortest_path["cost"] = current_cost
                if report:
                    print("NEW: ", shortest_path)
            return True
        else:
            if current_cost > shortest_path["cost"]: ### For highest path
                shortest_path["path"] = current_path.copy()
                shortest_path["cost"] = current_cost
                if report:
                    print("NEW: ", shortest_path)
            return True
    
    marked_maze[row][column] = True # Shows program you have already been to this vertex
    next_paths = find_neighbours(graph, row, column)

    
    for path in next_paths: ### Explores every path possible, but if there are no more vertixes to visit go back (recursivly) until you can visit one or if paths are depleted
        current_path.append( [path[0], path[1]] )
        current_cost += graph[current_path[-1][0]][current_path[-1][1]]

        if draw:
            draw_maze(graph, path[0], path[1], current_path, True)

        if current_cost > shortest_path["cost"] and shortest: ### For Eager dijkstras BUT ONLY works when calculating shortest path NOT highest.
            marked_maze[current_path[-1][0]][current_path[-1][1]] = False
            current_cost -= graph[current_path[-1][0]][current_path[-1][1]]
            current_path.pop()
        else:
            if dijkstras(graph, path[0], path[1], shortest, draw, report): ### IF last vertex is hit:
                marked_maze[current_path[-1][0]][current_path[-1][1]] = False
                current_cost -= graph[current_path[-1][0]][current_path[-1][1]]
                current_path.pop()

    
    try:
        marked_maze[current_path[-1][0]][current_path[-1][1]] = False
        current_cost -= graph[current_path[-1][0]][current_path[-1][1]]
        current_path.pop()
    except:
        return shortest_path
    



explored_paths = []
current_path = []
current_cost = matrix[0][0]
marked_maze = mark_vertexes(matrix)

do_shortest = True
draw = True
report = False

if do_shortest:
    shortest_path = {
        "path": [],
        "cost": float("inf") # Change to 0 for highest path
    }
elif not do_shortest:
    shortest_path = {
        "path": [],
        "cost": 0 # Change to 0 for highest path
    }

result = dijkstras(matrix, 0, 0, do_shortest, draw, report)

draw_maze(matrix, 0, 0, result["path"], False)
print(result)

### TO go from shortest to highest value CHANGE:
# 1 cost from "float("inf")" to 0
# 2 "<" to ">" in "if current_cost < shortest_path["cost"]: ### Change from "<" to ">" for highest cost"
# 3 True to False in "result = dijkstras(matrix, 0, 0, True)"