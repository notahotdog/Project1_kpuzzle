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
        self.einit_state = list(chain.from_iterable(init_state)) #converts nxn matrix to list format [[],[],[]] -> []
        self.egoal_state = list(chain.from_iterable(goal_state)) 
        

    #return a list based on the path traversed to reach the goal state
    def astarsearch(self):

        queue = collections.deque([Node(self.einit_state,self.egoal_state,0,"N")]) #adds the initial state

        ctr = 0
        while queue:

            queue = collections.deque(sorted(list(queue), key= lambda node: node.fscore())) #sorts the queue 
            ctr+= 1
            print("----------------------------------------------------")
            print("Debug queue of actions :", ctr)
            self.debugQueue(queue)
            print("End of debug queue of actions")
            print("----------------------------------------------------")

            tempNode = queue.popleft()
            self.debugNode(tempNode,"C") #node to be assessed
            self.actions.append(tempNode.actionType()) #add to list of actions attempted

            seen = set()
            seen.add(tempNode.state)

            if(tempNode.solved(tempNode.initial_state)):
                self.debugSolved()
                #print("Puzzle solved, list of actions conducted:")
                #print(self.actions)
                return self.actions 
            
            #create a new node to be added into the queue to be decremented from
            else:

                actionCheck = tempNode.validActions() #all available actions for the node being assessed "U,D,L,R"
                self.debugActions(actionCheck)

                #creates child nodes based on list of available actions
                for i in actionCheck:
                    newNode = Node(tempNode.actionSwap(i),self.egoal_state,tempNode.g +1,i) 
                    if newNode.state not in seen:
                        seen.add(newNode.state)
                        queue.appendleft(newNode) 

    #Prints out PATH undertaken to reach goal state
    def debugSolved(self):
        print("Puzzle solved, list of actions conducted:")
        print(self.actions)
        return None


    #DEBUGS the contents inside of the queue
    def debugQueue(self,queue):
        ctr = 0
        for x in (queue):
            ctr+= 1
            print("****")
            print("Matrix Order:", ctr)
            self.debugNode(x,"C")
            print("****")
    
    #DEBUGS the contents of the node s-simple c-complex
    #Takes in two parameters, the node to be assessed and the type of details the user desires
    #"S" => simple debug , "C" => more thorough details
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


    #Allows for two types of functionality (bad practise ik)
    #1.If 0 arguments -> Prints out the PATH that the algo traversed to reach the node
    #2.If 1 arguments ->
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


    def solve(self):
        #TODO
        # implement your search algorithm here
        if (not self.solvable()):
            return ["UNSOLVABLE"]
        

        path = self.astarsearch()  #a star returns the list of path traversed
        return path    


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


    
    #Returns whether or not the puzzle has been solved 
    def solved(self, tempState):
        return tempState == self.goal_state     

#Node class 
#Takes in 4 arguments - initial state, goal state, the path cost, action undertaken to reach that node
class  Node(object):
    def __init__(self, initial_state,goal_state,g,action): 
        self.initial_state = initial_state
        self.goal_state = goal_state


        # you may add more attributes if you think is useful
        
        self.total_length = len(initial_state) #length of list
        self.nSize = int(abs(math.sqrt(len(initial_state)))) #n definition of matrix
        self.g = g #this should be an int but somehow its a instance method

        self.zeroCoordinates = self.findZeroCoordinates()
        self.action = action #actionType 
    

    #Takes in a node to be swapped and the direction of the swap
    def actionSwap(self,direction):
        print(" ")
        print(" Initial state before actionSwap:", self.initial_state)
        zval = self.initial_state.index(0)
        nSize = self.nSize

        modList = copy.deepcopy(self.initial_state) 

        if(direction == "U"):
            print("UP")
            tempval = modList[zval-nSize]
            #print(" 0 swapped with :", tempval)
            modList[zval] = tempval
            modList[zval-nSize] = 0
        
        elif (direction == "D"):
            print("DOWN")
            tempval = modList[zval+nSize]
            #print(" 0 swapped with :", tempval)
            modList[zval] = tempval
            modList[zval+nSize] = 0
        
        elif (direction == "R"):
            print("RIGHT")
            tempval = modList[zval+1]
            #print(" 0 swapped with :", tempval)
            modList[zval] = tempval
            modList[zval+1] = 0
        
        elif (direction == "L"):
            print("LEFT")
            tempval = modList[zval-1]
            #print(" 0 swapped with :", tempval)
            modList[zval] = tempval
            modList[zval-1] = 0

        print(" Updated Matrix after actionSwap: ")
        self.debugMatrix(modList)
        return modList
        
    def actionType(self):
        return self.action

    #prints out the matrix 
    def debugMatrix(self,matrix):
        print('\n'.join(' '.join(map(str, matrix[i:i+n])) for i in range(0, len(matrix), n)))

    
    def state(self):
        return str(self.initial_state)
    
    def debugState(self):
        print(self.initial_state)

    def solved(self, tempState):
        #self.timerPause(5.5) # Uncomment if you want to slow down the execution
        return tempState == self.goal_state     

    #Insert time Pauses to allow for readability
    #takes in n - length of time for a pause
    def timerPause(self,n):
            print("Timer pause start". n)
            time.sleep(n) #pauses timer for n seconds
            print("Timer pause start". n)

    #Path cost 
    def g(self):
        return self.g 

    def getH(self):

        #TODO - IMPLEMENT HEURISTIC function

        return self.manhattan_distance()
    
    #will calculate the score for a particular heuristic
    def fscore(self):
        self.debugFscore()
        return self.g + self.getH()
    
    #prints the f/g/h score for a state
    def debugFscore(self):
        print(" F score for :")
        print("DEBUGGING MATRIX:")
        self.debugMatrix(self.initial_state)

        g = self.g
        h = self.getH()

        ans = g+h

        print("g val: ", g)
        print("h val: ", h)
        print("fscore => ", ans )
        return None

    #returns the list of valid actions for a node
    def validActions(self):

        coordinates = self.zeroCoordinates
        xVal = coordinates[0]
        yVal = coordinates[1]

        valid_actions = ["U","D","L","R"]

        boundary = self.nSize - 1 
        if(xVal == 0): valid_actions.remove("L")
        if(xVal == boundary): valid_actions.remove("R")
        if(yVal == 0): valid_actions.remove("U")
        if(yVal == boundary): valid_actions.remove("D") 

        return  valid_actions

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
            


    def manhattan_distance(self):
        
        n = self.nSize
        print("size of n :", n)
        print(self.initial_state)
        print(self.goal_state)
        

        if (self.parent == None):
            #compute for start state
            manhattan_distanceX = sum(abs(istate%n - gstate%n) + abs(istate//n - gstate//n) for istate, gstate in ((self.initial_state.index(i), self.goal_state.index(i)) for i in range(1, n**2)))

        else:
            #zeroCoordinate of current state contains number that was moved in parent node's initial_state
            nX = self.zeroCoordinates[0]
            nY = self.zeroCoordinates[1]
            numIndex = (nY * n) + nX
            num = self.parent.initial_state[numIndex]
            #Find the coordinates of num in the goal state
            gX = (num - 1) % n
            gY = (num - 1) // n
            manhattan_distanceX = self.parent.getH()
            if (self.action == "UP"):
                if (gY >= nY):
                    #Moved num up even though goal is below
                    manhattan_distanceX += 1
                else:
                    #Moved num towards goal
                    manhattan_distanceX -= 1
            elif (self.action == "DOWN"):
                if (gY <= nY):
                    #Moved num down even though goal is above
                    manhattan_distanceX += 1
                else:
                    #Moved num towards goal
                    manhattan_distanceX -= 1
            elif (self.action == "LEFT"):
                if (gX >= nX):
                    #moved num left even though goal is right
                    manhattan_distanceX += 1
                else:
                    #Moved num towards goal
                    manhattan_distanceX -= 1
            else:
                #Action is RIGHT
                if (gX <= nX):
                    #Moved num right even though goal is left
                    manhattan_distanceX += 1
                else:
                    #Moved num towards goal
                    manhattan_distanceX -= 1
            

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







