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
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    value[goal[0]][goal[1]] = 0
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    openlist = [[0, goal[0], goal[1]]]
    while openlist:
        openlist.sort()
        openlist.reverse()
        cur_pos = openlist.pop()

        cur_x = cur_pos[1]
        cur_y = cur_pos[2]
        cur_value  = cur_pos[0] + 1

        for i in range(len(delta)):
            x = cur_x + delta[i][0]
            y = cur_y + delta[i][1]
            if x >= 0 and x < len(grid) and y >=0 and y < len(grid[0]):
                if grid[x][y] == 0: #check if wall or not
                    if cur_value < value[x][y]:
                        value[x][y] = cur_value
                        openlist.append([cur_value, x, y])
        
    return value 

value = compute_value(grid, goal, cost)
print value