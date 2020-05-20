
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

Manhattan distance code - final
init_state = [1,2,3,4,5,0,6,7,8]
goal_state = [1,2,3,4,5,6,7,8,0]

n = int(abs(math.sqrt(len(init_state)))) 
print("size of n :", n)
        
manhattan_distance = 0
count = 0

manhattan_distance = sum(abs(istate%n - gstate%n) + abs(istate//n - gstate//n) for istate, gstate in ((init_state.index(i), goal_state.index(i)) for i in range(0, 9)))

#manhattan_distance = sum(abs(b%3 - g%3) + abs(b//3 - g//3) for b, g in ((init_state.index(i), goal_state.index(i)) for i in range(0, 9)))

print("Manhattan distance: ", manhattan_distance)


'''
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