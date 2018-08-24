# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
'''
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn
'''
grid = [[0, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [4, 5, 0]
goal = [4, 3]
cost = [1, 1, 1]

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):
    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))] for dir in range(len(forward))]

    x = init[0]
    y = init[1]
    d = init[2]
    g = 0

    open = [[g, d, x, y]]
    #value[d][x][y] = 0
    found = False
    
    policy2D = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    policy3D = [[[' ' for row in range(len(grid[0]))] for col in range(len(grid))] for dir in range(len(forward))]

    while not found:

        open.sort()
        open.reverse()
        next = open.pop()
        x = next[2]
        y = next[3]
        d = next[1]
        g = next[0]
        
        if x == goal[0] and y == goal[1]:
            value[d][x][y] = g + 1
            policy2D[x][y] = '*'
            found = True
        elif grid[x][y] == 0:
            for rel_dir in range(len(action)):                   
                d2 = (d + action[rel_dir]) % 4
                x2 = x + forward[d2][0]
                y2 = y + forward[d2][1]
                if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                    if grid[x2][y2] == 0:
                        g2 = g + cost[rel_dir]
                        open.append([g2, d2, x2, y2])                     
                        if g2 < value[d][x][y]:
                            value[d][x][y] = g2
                            policy3D[d][x][y] = action_name[rel_dir]

     # recursive to get direction from starting position

    count = 0
    x = init[0]
    y = init[1]
    d = init[2]

    while count < g:
        policy2D[x][y] = policy3D[d][x][y]
        here = policy2D[x][y] 
        if here in action_name:
            direction = action_name.index(here)
            d = (d + action[direction]) % 4
            x += forward[d][0]
            y += forward[d][1]
        count += 1
    
    policy2D[goal[0]][goal[1]] = '*'
    return policy2D



policy2D = optimum_policy2D(grid,init,goal,cost)
print policy2D