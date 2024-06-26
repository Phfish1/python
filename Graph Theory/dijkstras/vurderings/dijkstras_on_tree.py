from time import sleep

matrix = [
[ 0 ] ,
[ 2, 4 ] ,
[ 0, 5, 6 ],
[ 7, 2, 9, 10 ],
[ 25, 11, 1, 0, 5 ],
[ 1, 88, 51, 88, 61, 4 ],
[ 93, 12, 73, 36, 71, 65, 34 ],
[ 233, 5, 2, 1, 6, 7, 55, 1 ],
[ 16, 111, 213, 9, 23, 433, 1, 34, 13 ],
[ 5, 23, 453, 789, 123, 200, 212, 345, 556, 99 ]
]


def draw_maze(maze, row, column, path, fast):
    maze_string = ""

    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            if ( (i == len(maze)-1 and j == column) and (row == len(maze)-1 and column) ):
                maze_string += f"\033[92m{maze[i][j]}\033[00m, "
            elif i == 0 and j == 0:
                maze_string += f"\033[92m{maze[0][0]}\033[00m, " # Marks the starting point 
            elif (row == i and column == j):
                maze_string += f"\033[91m{maze[i][j]}\033[00m, " # Marks current Vertex
            elif [i, j] in path:
                if (i == len(maze)-1):
                    maze_string += f"\033[92m{maze[i][j]}\033[00m, "
                else:
                    maze_string += f"\033[91m{maze[i][j]}\033[00m, " # Marks already visited vertexes, [IN current path] "See explored_paths.pop()" in dfs()
            else:
                maze_string += f"{maze[i][j]}, "

        maze_string += f"\n"
    
    if fast:
        print(f"{maze_string}", end='\r')
        sleep(0.01)
        for line in maze_string.splitlines():
            print("\033[1A", end="\x1b[2K")
    else:
        print(f"{maze_string}")
        print("---------------------")

def find_neighbours(graph, row, column):

    row_vertecies = [+1, +1, +1]
    column_vertecies = [0, +1, -1]

    valid_paths = []

    for direction in range(0, 3):
        next_row = row + row_vertecies[direction]
        next_column = column + column_vertecies[direction]

        if ( (0 <= next_row < len(graph)) and (0 <= next_column < len(graph[row])) ):
            valid_paths.append([next_row, next_column])

    return valid_paths

def dijkstras(graph, row, column, shortest, draw, report): ### Row + Collumn representing the vertex 
    global current_cost
    global current_path
    global shortest_path
    

    if row == (len(graph) -1): ### Returns True when last vertex in maze is hit
        if shortest:
            if current_cost < shortest_path["cost"]: ### Change from "<" to ">" for highest cost
                shortest_path["path"] = current_path.copy() ### Use copy, OR else shortest_path["path"] will be BOUND to the current_path
                shortest_path["cost"] = current_cost
                if report:
                    print("NEW: ", shortest_path)
            return True
        else:
            if current_cost > shortest_path["cost"]: ### Change from "<" to ">" for highest cost
                shortest_path["path"] = current_path.copy() ### Use copy, OR else shortest_path["path"] will be BOUND to the current_path
                shortest_path["cost"] = current_cost
                if report:
                    print("NEW: ", shortest_path)
            return True
    
    next_paths = find_neighbours(graph, row, column)

    for path in next_paths: ### Explores every path possible, but if there are no more vertixes to visit go back (recursivly) until you can visit one or if paths are depleted
        current_path.append( [path[0], path[1]] )
        current_cost += graph[current_path[-1][0]][current_path[-1][1]]

        if draw:
            draw_maze(graph, path[0], path[1], current_path, True)

        if current_cost > shortest_path["cost"] and shortest: ### Makes dijkstras Eager BUT ONLY if the goal is the shortest path
            current_cost -= graph[current_path[-1][0]][current_path[-1][1]]
            current_path.pop()
        else:
            if dijkstras(graph, path[0], path[1], shortest, draw, report): ### IF last vertex is hit:
                current_cost -= graph[current_path[-1][0]][current_path[-1][1]]
                current_path.pop()

    
    try:
        current_cost -= graph[current_path[-1][0]][current_path[-1][1]]
        current_path.pop()
    except:
        return shortest_path
    



explored_paths = []
current_path = []
current_cost = matrix[0][0]

do_shortest = True
draw = True
report = True

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


