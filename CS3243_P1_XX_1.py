# CS3243 Introduction to Artificial Intelligence
# Project 1: k-Puzzle

import os
import sys

# Running script on your own - given code can be run with the command:
# python file.py, ./path/to/init_state.txt ./output/output.txt


class Puzzle(object):
    def __init__(self, init_state, goal_state):
        # you may add more attributes if you think is useful
        self.init_state = init_state
        self.goal_state = goal_state
        self.actions = list()

        '''
        Code Idea:
        [[2, 3, 6],
        [1, 5, 8],
        [4, 7, 0]]

        [[2, 3, 6],
        [1, 5, 8],
        [4, 0, 7]]

        [[2, 3, 6],
        [1, 5, 0],
        [4, 7, 8]]

        # Node class:
        2D matrix
        ij position of 0 (ex: (3, 3))
        method for all possible moves of shifting around 0 
        method for checking goal state - scan through the whole matrix and stop when any number is out of place
        check if node has been visited 
        parent null - check for initial state
        attribute previous move - to keep track of LEFT, RIGHT
        Another method in Puzzle class, to backtrack, use stack possibly
        Frontier would be a queue
        '''

    class Node:
        def __init__(self, curr_state, parent, prev_move, position_of_zero):
            self.currState = curr_state
            self.parent = parent
            self.prevMove = prev_move
            self.positionOfZero = position_of_zero

        def is_goal_state(self):
            return self.puzzle == Puzzle.goal_state


def solve(self):
    #TODO
    # implement your search algorithm here
    # root node
    root = Puzzle.Node(Puzzle.init_state, None, None, 2)
    return ["LEFT", "RIGHT"] # sample output

    # you may add more functions if you think is useful  

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

    print(init_state)
    print("")
    print(goal_state)

    puzzle = Puzzle(init_state, goal_state)
    ans = puzzle.solve()

    with open(sys.argv[2], 'a') as f:
        for answer in ans:
            f.write(answer+'\n')            






