#manhattan distance debug
import math
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