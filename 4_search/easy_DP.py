# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def recursive(x, y, current_value, value):

    openlist = []
    for i in range(len(delta)):
        x2 = x - delta[i][0]
        y2 = y - delta[i][1]
        if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
            if grid[x2][y2] == 0:
                if value[x2][y2]==99 or (value[x2][y2]!= 99 and value[x2][y2]>=current_value+1):
                    value[x2][y2]= current_value + cost
                    openlist.append([x2, y2])
    for i in range(len(openlist)):
        recursive(openlist[i][0], openlist[i][1], current_value + 1, value)

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    value = [[99 for x in range(len(grid[0]))] for y in range(len(grid))]
    value[goal[0]][goal[1]] = 0
    recursive(goal[0], goal[1], 0, value)
                
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    return value 

value = compute_value(grid, goal, cost)
print value
