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
    new_pos[0] = pos[0] + delta[0] 
    new_pos[1] = pos[1] + delta[1]
    new_pos[2] = pos[2] + 1
    if new_pos[0] >=0 and new_pos[1] >= 0: # check new point inside the grid or not
        if grid[new_pos[0]][new_pos[1]] == 0: # check new point don't touch the wall
            return new_pos

def priority(checklist):
    min_value = 0;
    min_index = 0;
    for i in range(len(checklist)):
        if checklist[i][2] < min_value:
            min_value = checklist[i][2]
            min_index = i 
    return checklist[min_index]

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    cur_pos = [0, 0, 0]
    checklist =[]
    checklist.append(cur_pos)
    path = 0
    found = 0
    while checklist:
        for i in range(len(delta)):
            cur_pos = priority(checklist)
            new_pos = move(cur_pos, delta[i], grid)
            if new_pos:
                print "new:", new_pos
                if new_pos[0] == goal[0] and new_pos[1] == goal[1]:
                    found = 1
                    path = new_pos
                    print "found"
                if new_pos not in checklist:
                    checklist.append(new_pos)
                    print "add"
        
        checklist.remove(cur_pos)
    #if found == 0:
    #    path = "fail"
    return path

path = search(grid,init,goal,cost)
print(path)
