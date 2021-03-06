'''
#DEBUG actionGeneration
#generates the list for the various actions

import math

somelist = [1,2,3,4,0,6,7,8,9]
total_length = len(somelist)
nSize = int(abs(math.sqrt(len(somelist)))) #n definition of matrix


def actionSwap(somelist,direction):
  zval = somelist.index(0)
  if(direction == "U"):
    print("UP")
    tempval = somelist[zval-nSize]
    print("tempval :", tempval)
    somelist[zval] = tempval
    somelist[zval-nSize] = 0

  elif (direction == "D"):
    print("DOWN")
    tempval = somelist[zval+nSize]
    print("tempval :", tempval)
    somelist[zval] = tempval
    somelist[zval+nSize] = 0
  
  elif (direction == "R"):
    print("RIGHT")
    tempval = somelist[zval+1]
    print("tempval :", tempval)
    somelist[zval] = tempval
    somelist[zval+1] = 0

  elif (direction == "L"):
    print("LEFT")
    tempval = somelist[zval+1]
    print("tempval :", tempval)
    somelist[zval] = tempval
    somelist[zval-1] = 0
  return somelist

listActions = ["D","R"]
for i in listActions:
  swappedlist = actionSwap(somelist,i)

  print(swappedlist)

'''

'''
#valid actions debug

import math
import copy
somelist = [1,2,3,4,5,6,7,8,0]
total_length = len(somelist)
nSize = int(abs(math.sqrt(len(somelist)))) #n definition of matrix




def validActions(somelist):

        temp_copy = copy.deepcopy(somelist) #makes a copy of the initial state
        #check boundary 
        coordinates = findZero(temp_copy)
        xVal = coordinates[0]
        yVal = coordinates[1]
        #evaluated case conditions

        valid_actions = ["U","D","L","R"]

        boundary = nSize - 1 
        if(xVal == 0): valid_actions.remove("L")
        if(xVal == boundary): valid_actions.remove("R")
        if(yVal == 0): valid_actions.remove("U")
        if(yVal == boundary): valid_actions.remove("D") 

        return valid_actions

    
    #returns a pair that indicates the x and y of 0
def findZero(state):
  xCtr = 0
  yCtr = 0

  for x in range(total_length):
    if(xCtr == nSize): #nSize == 3 
      yCtr += 1
      xCtr = 0 
            
    if(state[x] == 0):
      break
    xCtr += 1
  return xCtr,yCtr

lis = validActions(somelist)
print(lis)
'''
'''
import math
#Manhattan distance code - final
init_state = [1,2,3,4,5,0,7,8,6]
goal_state = [1,2,3,4,5,6,7,8,0]

n = int(abs(math.sqrt(len(init_state)))) 
print("size of n :", n)
        
manhattan_distance = 0
count = 0


for i in range(0,9):
  istate = init_state.index(i)
  gstate = goal_state.index(i)

  print("istate value :", istate)
  print("gstate value :", gstate)

  if((istate) == 0):
    continue
  manhattan_distance += (abs(istate%n - gstate%n) + abs(istate//n - gstate//n))


#manhattan_distance = sum(abs(b%3 - g%3) + abs(b//3 - g//3) for b, g in ((init_state.index(i), goal_state.index(i)) for i in range(0, 9)))
'''
'''
#initial_state = [1,5,3,4,2,6,7,8,0]
#goal_state = [0,1,2,3,4,5,6,7,8]
#initial_state = [3,1,2,0,4,5,6,7,8]
def calculateManhattan(initial_state):
    initial_config = initial_state
    manDict = 0
    for i,item in enumerate(initial_config):
        prev_row,prev_col = int(i/ 3) , i % 3
        goal_row,goal_col = int(item /3),item % 3
        manDict += abs(prev_row-goal_row) + abs(prev_col - goal_col)
    return manDict
print("mDict: ",calculateManhattan(initial_state))

'''

import math
init_state = [1,2,3,4,5,0,7,8,6]
goal_state = [1,5,3,4,2,6,7,8,0]

def manhatan_dist(board,goal_stat):
    #Manhattan priority function. The sum of the Manhattan distances 
    #(sum of the vertical and horizontal distance) from the blocks to their goal positions, 
    #plus the number of moves made so far to get to the search node.
    b = board
    g = goal_stat

    manh_dist = 0
    for i in range (0,3,1):
        for j in range (0,3,1):
            bij = b[i][j]
            i_b = i
            j_b = j

            i_g, j_g = value_index(g,bij) 

            manh_dist += (math.fabs(i_g - i_b) + math.fabs(j_g - j_b))

    print("mandict: ", manh_dist)

manhatan_dist(init_state,goal_state)
'''
for istate, gstate in ((init_state.index(i),goal_state.index(i)) for i in range(0,n):
manhattan_distance += (abs(istate%n - gstate%n) + abs(istate//n - gstate//n))





x = sum(abs((val-1)%3 - i%3) + abs((val-1)//3 - i//3)for i, val in enumerate(init_state) if val) #will return the value
        
y = sum(abs(b%3 - g%3) + abs(b//3 - g//3) for b, g in ((init_state.index(i), goal_state.index(i)) for i in range(0, 9)))
print(x)
print(y)




while count < len(init_state):
  ini_col = (init_state[count] / n)
  ini_row = (init_state[count] % n)
  goal_col = (goal_state[count] / n)
  goal_row = (goal_state[count] % n)
  print("ic:", ini_col, " gc: ", goal_col, " ir: ", ini_row, " gr: ", goal_row )
  print("")

  print(" count :", count, "index m_dist:",(abs(ini_col-goal_col) + abs(ini_row - goal_row)),"\n" )
  curr_md = (abs(ini_col-goal_col) + abs(ini_row - goal_row))

  manhattan_distance += (abs(ini_col-goal_col) + abs(ini_row - goal_row))
  print("current Manhattan distance: ", curr_md)

  print("")
  count += 1
        
print(manhattan_distance)

initial_state = [1,5,3,4,2,6,7,8,0]
goal_state = [0,1,2,3,4,5,6,7,8]
def calculateManhattan(initial_state):
    initial_config = initial_state
    manDict = 0
    for i,item in enumerate(initial_config):
        prev_row,prev_col = int(i/ 3) , i % 3
        goal_row,goal_col = int(item /3),item % 3
        manDict += abs(prev_row-goal_row) + abs(prev_col - goal_col)
    print (manDict)
    '''