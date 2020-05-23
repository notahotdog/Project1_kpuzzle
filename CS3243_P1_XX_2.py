# CS3243 Introduction to Artificial Intelligence
# Project 1: k-Puzzle

import os
import sys
import math
from copy import deepcopy
import collections
import copy
from itertools import chain
import time

# Running script on your own - given code can be run with the command:
# python file.py, ./path/to/init_state.txt ./output/output.txt

class Puzzle(object):
    def __init__(self, init_state, goal_state):
        # you may add more attributes if you think is useful

        self.init_state = init_state
        self.goal_state = goal_state
        self.actions = []
        self.einit_state = list(chain.from_iterable(init_state)) #flattens the list
        self.egoal_state = list(chain.from_iterable(goal_state)) #flattens the list

        #self.actions = list()

    def astarsearch(self):

        #pass the goal state and the initial state
        #self.init_state = list(chain.from_iterable(init_state)) #flattens the list
        #self.goal_state = list(chain.from_iterable(goal_state)) #flattens the list
       

        #print("Flattened list: ", self.einit_state)
        #print("Flattened list: ", self.egoal_state)


        queue = collections.deque([Node(self.einit_state,self.egoal_state,0,"N", None)]) #add the initial state
        seen = set()
        #seen.add()

        #ctr = 0
        while queue:

            #sort the deque
            queue = collections.deque(sorted(list(queue), key= lambda node: node.fscore()))
            #ctr += 1
            #print("----------------------------------------------------")
            #print("Debug queue of actions :", ctr)
            #self.debugQueue(queue)
            #print("End of debug queue of actions")
            #print("----------------------------------------------------")

            #debug queue

            tempNode = queue.popleft()
            #self.debugNode(tempNode,"C") #node to be assessed
            self.actions.append(tempNode.actionType()) #add to list of actions attempted

            #seen = set()
            seen.add(tempNode.state())

            if(tempNode.solved(tempNode.initial_state)):
                #print("Puzzle solved, list of actions conducted:")
                #print(self.actions)
                return tempNode #can be changed later on
            


            #if(self.solved(self.init_state)):
            #    return self.actions #can be changed later on
            
            else:

                #create a new node to be added into the queue to be decremented from
                actionCheck = tempNode.validActions() #all available actions for the node being assessed
                #self.debugActions(actionCheck)

                for i in actionCheck:
                    #create a modified node
                    #modifiedNode = tempNode.actionSwap(i)
                    #newNode = Node(modifiedNode,goal_state,tempNode.inc_g,i)
                    newNode = Node(tempNode.actionSwap(i),self.egoal_state,tempNode.g +1,i, tempNode)
                    if newNode.state() not in seen:
                        #seen.add(newNode.state)
                        queue.appendleft(newNode) 




    #DEBUGS the contents inside the queue
    def debugQueue(self,queue):
        ctr = 0
        for x in (queue):
            ctr+= 1
            print("****")
            print("Matrix Order:", ctr)
            self.debugNode(x,"C")
            print("****")
    
    #DEBUGS the contents of the node s-simple c-complex
    def debugNode(self,node,eType):

        print("")
        print("-------")
        print("DEBUG NODE: ")
        
        if eType == "S":
            print(" Initial State: ")
            node.debugMatrix(node.initial_state)
            print(" g val: ", node.g, " action: ", node.action)

        elif eType == "C":
            print("Node representation:")
            node.debugMatrix(node.initial_state)
            print("Node Details:")
            print(" g val: ", node.g, "fscore val", node.fscore() , "manhattan distance", node.manhattan_distance(), " action: ", node.action)


    #debug actions allows to check whether the action is in the action list
    def debugActions(self, *args):
        print("DEBUG: ")
        if len(args) == 0:
            print (" PATH for solution")
            for x in self.actions:
                print(x)
        
        elif len(args) == 1:
            print("actionChecks to be evaluated:")
            actionCheck = args[0]
            print(actionCheck)

#            for x in actionCheck:
#                print(x)


    def solve(self):
        #TODO
        # implement your search algorithm here
        if (not self.solvable()):
            return ["UNSOLVABLE"]
        
        #need to do solve the puzzle

        self.backtrack(self.astarsearch()) #Find the goal node and backtrack to obtain the actions   
        return self.actions   

        #return ["LEFT", "RIGHT"] # sample output 


    # you may add more functions if you think is useful

    def solvable(self):
        n = len(self.init_state)
        if ((n % 2 == 1) and (self.count_inv(n) % 2 == 0)):
            return True
        elif (n % 2 == 0):
            row = self.find_zero(self.init_state, n)
            if (self.count_inv(n) % 2 == 0):
                if (row % 2 == 1):
                    return True
            else:
                if (row % 2 == 0):
                    return True       
        return False


    def count_inv(self, n):
        cpy = []
        count = 0
        for i in range(n):
            cpy.extend(self.init_state[i])
        for i in range(n*n):
            for j in range(i + 1, n*n):
                if ((cpy[i] > cpy[j]) and (cpy[j] != 0)):
                    count += 1
        return count

    #count row number (bottom row as 1) that contains the blank
    def find_zero(self, state, n):
        for i in range(n):
            for j in range(n):
                if (state[i][j] == 0):
                    return n - i


    def backtrack(self, goalNode):
        current = goalNode
        while (current.parent != None):
            self.actions.append(current.actionType())
            current = current.parent
        self.actions.reverse()
        
    #checks whether puzzle has been solved - need to ensure values inside are equal
    def solved(self, tempState):
        return tempState == self.goal_state     

class  Node(object):
    

    def __init__(self, initial_state,goal_state,g,action,parent): #initial state and the g value
        self.initial_state = initial_state
        self.goal_state = goal_state


        # you may add more attributes if you think is useful
        
        self.total_length = len(initial_state) #length of list
        self.nSize = int(abs(math.sqrt(len(initial_state)))) #n definition of matrix
        self.g = g #this should be an int but somehow its a instance method
        #print("class g type :", type(g))
        #self.h  = self.manhattan_distance
        
        #self.fscore = self.g+ self.h

        #type(initial_state)
        self.zeroCoordinates = self.findZeroCoordinates()
        self.action = action #actionType 
        #self.valid_actions = self.validActions()
        self.parent = parent #parent node
    

    #Takes in a node to be swapped and the direction of the swap
    def actionSwap(self,direction):
        #print(" ")
        print("actionSwap Initial state:", self.initial_state)
        zval = self.initial_state.index(0)
        nSize = self.nSize
        #modList is the list of actions 
        modList = copy.deepcopy(self.initial_state) #makes a copy of the initial state
        #modList = self.initial_state #list to be modified
        if(direction == "DOWN"):
            print("DOWN")
            tempval = modList[zval-nSize]
            print(" 0 swapped with :", tempval)
            modList[zval] = tempval
            modList[zval-nSize] = 0
        
        elif (direction == "UP"):
            print("UP")
            tempval = modList[zval+nSize]
            print(" 0 swapped with :", tempval)
            modList[zval] = tempval
            modList[zval+nSize] = 0
        
        elif (direction == "LEFT"):
            print("LEFT")
            tempval = modList[zval+1]
            print(" 0 swapped with :", tempval)
            modList[zval] = tempval
            modList[zval+1] = 0
        
        elif (direction == "RIGHT"):
            print("RIGHT")
            tempval = modList[zval-1]
            print(" 0 swapped with :", tempval)
            modList[zval] = tempval
            modList[zval-1] = 0

        print(" updated Matrix: ")
        self.debugMatrix(modList)
        return modList
        
    def actionType(self):
        return self.action

    def debugMatrix(self,matrix):
        print('\n'.join(' '.join(map(str, matrix[i:i+n])) for i in range(0, len(matrix), n)))

    
    def state(self):
        return str(self.initial_state)
    
    def debugState(self):
        print(self.initial_state)

    def solved(self, tempState):
        #print("timer pause")
        #time.sleep(5.5)    # pause 5.5 seconds
        print("timer pause") 


        return tempState == self.goal_state     

    #number of steps taken to get to current state
    def g(self):
        return self.g 

    #manhattan distance to get to next state
    '''
    def h(self):
        print("Debugging h:")
        self.debugMatrix(self.initial_state) 
        self.h = self.manhattan_distance()
        return self.h
        #return self.manhattan_distance
        '''
    
    def getH(self):
        return self.manhattan_distance()
    
    def getG(self):
        return self.g

    #will calculate the score for a particular heuristic
    def fscore(self):
        #self.debugFscore()
        return self.g + self.getH()
        #return self.g + self.h
    
    def debugFscore(self):
        print(" F score for :")
        print("DEBUGGING MATRIX:")
        self.debugMatrix(self.initial_state)
        print("g val", self.g)
        g = self.g

        h = self.getH()
        #print(" G type : ", type(g))
        #print(" H type : ", type(h))
        ans = g+h
        print("fscore  => ", ans )
        return None

    def inc_g(self):
        result = self.g +1
        return result

        #def valid_actions(self):
        #return self.valid_actions

    def validActions(self):

        #temp_copy = copy.deepcopy(init_state) #makes a copy of the initial state
        #coordinates = findZeroCoordinates(temp_copy)

        coordinates = self.zeroCoordinates
        xVal = coordinates[0]
        yVal = coordinates[1]

        valid_actions = ["UP","DOWN","LEFT","RIGHT"]

        boundary = self.nSize - 1 
        if(xVal == 0): valid_actions.remove("RIGHT")
        if(xVal == boundary): valid_actions.remove("LEFT")
        if(yVal == 0): valid_actions.remove("DOWN")
        if(yVal == boundary): valid_actions.remove("UP") 

        return  valid_actions
        #return None
        #return valid_actions

    
    #returns a pair that indicates the x and y of 0
    def findZeroCoordinates(self):
        somelist = self.initial_state
        xCtr = 0
        yCtr = 0

        for x in range(self.total_length):
            if(xCtr == self.nSize): #nSize == 3 
                yCtr += 1
                xCtr = 0 
            
            if(somelist[x] == 0):
                break
            xCtr += 1
        return xCtr,yCtr
            


    #might need to modify code to compare against the 2 states instead of inital.self state and goal state.
    def manhattan_distance(self):

        n = self.nSize
        #print("size of n :", n)

        #print(self.initial_state)
        #print(self.goal_state)
        
        #self.debugState()
        
        manhattan_distance = 1
        #manhattan_distance = sum(abs(istate%n - gstate%n) + abs(istate//n - gstate//n) for istate, gstate in ((self.initial_state.index(i), self.goal_state.index(i)) for i in range(0, 9))) #need to double check the manhattan distance heuristic for accuracy
        
        manhattan_distanceX = sum(abs(istate%n - gstate%n) + abs(istate//n - gstate//n) for istate, gstate in ((self.initial_state.index(i), self.goal_state.index(i)) for i in range(0, 9)))

        #print("Manhattan distance: ", manhattan_distance) 
        return manhattan_distanceX



    

    
            
if __name__ == "__main__":
    # do NOT modify below

    # argv[0] represents the name of the file that is being executed
    # argv[1] represents name of input file
    # argv[2] represents name of destination output file
    if len(sys.argv) != 3:
        raise ValueError("Wrong number of arguments!")

    try:
        f = open(sys.argv[1], 'r')
    except IOError:
        raise IOError("Input file not found!")

    lines = f.readlines()
    
    # n = num rows in input file
    n = len(lines)
    # max_num = n to the power of 2 - 1
    max_num = n ** 2 - 1

    # Instantiate a 2D list of size n x n
    init_state = [[0 for i in range(n)] for j in range(n)]
    goal_state = [[0 for i in range(n)] for j in range(n)]
    

    i,j = 0, 0
    for line in lines:
        for number in line.split(" "):
            if number == '':
                continue
            value = int(number , base = 10)
            if  0 <= value <= max_num:
                init_state[i][j] = value
                j += 1
                if j == n:
                    i += 1
                    j = 0

    for i in range(1, max_num + 1):
        goal_state[(i-1)//n][(i-1)%n] = i
    goal_state[n - 1][n - 1] = 0

    puzzle = Puzzle(init_state, goal_state)
    ans = puzzle.solve()

    with open(sys.argv[2], 'a') as f:
        for answer in ans:
            f.write(answer+'\n')







