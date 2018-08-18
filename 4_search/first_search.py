# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def move(pos, delta, grid):
    new_pos = [0,0,0]
    new_pos[0] = pos[0] + 1 
    new_pos[1] = pos[1] + delta[0]
    new_pos[2] = pos[2] + delta[1]
    if len(grid)-1 >= new_pos[1] >=0 and len(grid[0])-1>= new_pos[2] >= 0: # check new point inside the grid or not
        if grid[new_pos[1]][new_pos[2]] == 0: # check new point don't touch the wall
            return new_pos

def priority(openlist):
    min_value = 0;
    min_index = 0;
    for i in range(len(openlist)):
        if openlist[i][0] < min_value:
            min_value = openlist[i][0]
            min_index = i 
    return openlist[min_index]

def inChecklist(checklist, newpos):
    if newpos[1:3] in checklist:
        return True
    else:
        return False

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    cur_pos = [0, 0, 0]
    openlist =[]
    openlist.append(cur_pos)
    checklist = []
    checklist.append(cur_pos[1:3])
    found = 0
    while openlist:
        for i in range(len(delta)):
            cur_pos = priority(openlist)
            new_pos = move(cur_pos, delta[i], grid)
            if new_pos and not inChecklist(checklist, new_pos):
                checklist.append(new_pos[1:3])
                if new_pos[1] == goal[0] and new_pos[2] == goal[1]:
                    found = 1
                    path = new_pos
                if new_pos not in openlist:
                    openlist.append(new_pos)        
        openlist.remove(cur_pos)
    if found == 0:
        path = "fail"
    return path

