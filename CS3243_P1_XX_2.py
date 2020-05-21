# CS3243 Introduction to Artificial Intelligence
# Project 1: k-Puzzle

import os
import sys
import math
from copy import deepcopy
import collections
import copy

# Running script on your own - given code can be run with the command:
# python file.py, ./path/to/init_state.txt ./output/output.txt

class Puzzle(object):
    def __init__(self, init_state, goal_state):
        # you may add more attributes if you think is useful
        self.init_state = init_state
        self.goal_state = goal_state
        self.actions = list()

    def astarsearch(self):

        #pass the goal state and the initial state

        queue = collections.deque([Node(init_state,goal_state,0,"N")]) #add the initial state
        #seen = set()
        #seen.add()

        while queue:

            #sort the deque
            queue = collections.deque(sorted(list(queue), key= lambda node: node.fscore))

            tempNode = queue.popleft()
            self.actions.append(tempNode.actionType)


            if(self.solved(self.init_state)):
                return self.actions #can be changed later on
            
            else:

                #create a new node to be added into the queue to be decremented from
                #tempNode.valid_action
                actionCheck = tempNode.valid_action #all available actions
                for i in actionCheck:
                    #create a modified node
                    newNode = Node(tempNode.actionSwap(tempNode,i),goal_state,tempNode.inc_g,i)
                    queue.appendleft(newNode) 


    def solve(self):
        #TODO
        # implement your search algorithm here
        if (not self.solvable()):
            return ["UNSOLVABLE"]
        
        #need to do solve the puzzle

        path = self.astarsearch() #list of the path traversed    
        return path    

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

    def find_zero(self, state, n):
        for i in range(n):
            for j in range(n):
                if (state[i][j] == 0):
                    return n - i


    
    #checks whether puzzle has been solved - need to ensure values inside are equal
    def solved(self, tempState):
        return tempState == self.goal_state     

class  Node(object):
    

    def __init__(self, initial_state,goal_state,g,action): #initial state and the g value
        self.initial_state = initial_state
        # you may add more attributes if you think is useful
        self.total_length = len(initial_state) #length of list
        self.nSize = int(abs(math.sqrt(len(initial_state)))) #n definition of matrix
        self.g = 0; 
        type(initial_state)
        self.zeroCoordinates = self.findZeroCoordinates
        self.action = action #actionType 
        self.valid_actions = self.validActions


    def actionSwap(modList,direction):
        zval = modList.index(0)
        if(direction == "U"):
            print("UP")
            tempval = modList[zval-nSize]
            print("tempval :", tempval)
            modList[zval] = tempval
            modList[zval-nSize] = 0
        
        elif (direction == "D"):
            print("DOWN")
            tempval = modList[zval+nSize]
            print("tempval :", tempval)
            modList[zval] = tempval
            modList[zval+nSize] = 0
        
        elif (direction == "R"):
            print("RIGHT")
            tempval = modList[zval+1]
            print("tempval :", tempval)
            modList[zval] = tempval
            modList[zval+1] = 0
        
        elif (direction == "L"):
            print("LEFT")
            tempval = modList[zval+1]
            print("tempval :", tempval)
            modList[zval] = tempval
            modList[zval-1] = 0

        return modList
        
    def actionType(self):
        return self.action


    #number of steps taken to get to current state
    def g(self):
        return g 

    def inc_g(self):
        self.g += 1

    #manhattan distance to get to next state
    def h(self):
        return self.manhattan_distance
    
    #will calculate the score for a particular heuristic
    def fscore(self):
        return self.g + self.h

    def validActions(self):

        #temp_copy = copy.deepcopy(init_state) #makes a copy of the initial state
        #coordinates = findZeroCoordinates(temp_copy)

        coordinates = zeroCoordinates
        xVal = coordinates[0]
        yVal = coordinates[1]

        valid_actions = ["U","D","L","R"]

        boundary = nSize - 1 
        if(xVal == 0): valid_actions.remove("L")
        if(xVal == boundary): valid_actions.remove("R")
        if(yVal == 0): valid_actions.remove("U")
        if(yVal == boundary): valid_actions.remove("D") 

        return self.valid_actions

    
    #returns a pair that indicates the x and y of 0
    def findZeroCoordinates(self):
        somelist = self.initial_state
        xCtr = 0
        yCtr = 0

        for x in range(total_length):
            if(xCtr == nSize): #nSize == 3 
                yCtr += 1
                xCtr = 0 
            
            if(somelist[x] == 0):
                break
            xCtr += 1
        return xCtr,yCtr
            


    #might need to modify code to compare against the 2 states instead of inital.self state and goal state.
    def manhattan_distance(self):

        n = self.nSize
        print("size of n :", n)
        
        manhattan_distance = sum(abs(istate%n - gstate%n) + abs(istate//n - gstate//n) for istate, gstate in ((self.init_state.index(i), self.goal_state.index(i)) for i in range(0, n+1))) #need to double check the manhattan distance heuristic for accuracy

        #print("Manhattan distance: ", manhattan_distance) 
        return manhattan_distance



    

    
            
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







