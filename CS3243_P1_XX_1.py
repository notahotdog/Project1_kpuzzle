# CS3243 Introduction to Artificial Intelligence
# Project 1: k-Puzzle

import copy
import os
# from Queue import PriorityQueue # its queue in Python3, but assignment using Python 2.7
import sys

# Running script on your own - given code can be run with the command:
# python file.py, ./path/to/init_state.txt ./output/output.txt


class Puzzle(object):
    def __init__(self, init_state, goal_state):
        # you may add more attributes if you think is useful
        self.init_state = init_state
        self.goal_state = goal_state
        self.size = len(init_state)
        self.actions = list()


    def solve(self):
        # TODO
        # implement your search algorithm here

        # Check if puzzle is solvable
        if (not self.solvable()):
            return ["UNSOLVABLE"]

        # Initializing root node, frontier, and explored set of nodes
        zero_pos = self.find_zero()
        root = Node(self.init_state, None, None, zero_pos)
        frontier = list()
        frontier.append(root)
        explored = dict()

        if (self.is_goal_state(root.curr_state)):
            return []

        while (not frontier):
            node = frontier.pop(0)

            hash_num = hash(node.curr_state)
            explored[hash_num] = node.curr_state
            
            row = node.zero_position[0]
            col = node.zero_position[1]

            # LEFT
            if (col != self.size - 1):
                # getting the next state
                next_state = copy.deepcopy(node.curr_state)
                number_to_swap = next_state[row][col + 1]
                next_state[row][col + 1] = 0
                next_state[row][col] = number_to_swap

                child = Node(next_state, node, "LEFT", (row, col + 1))
                key = hash(next_state)
                if (key not in explored):
                    if (self.is_goal_state(child)):
                        # goal state reached, need to backtrack
                        return self.backtrack(child)
                    else:     
                        frontier.append(child)
            
            # RIGHT
            if (col != 0):
                # getting the next state
                next_state = copy.deepcopy(node.curr_state)
                number_to_swap = next_state[row][col - 1]
                next_state[row][col - 1] = 0
                next_state[row][col] = number_to_swap

                child = Node(next_state, node, "RIGHT", (row, col - 1))
                key = hash(next_state)
                if (key not in explored):
                    if (self.is_goal_state(child)):
                        # goal state reached, need to backtrack
                        return self.backtrack(child)
                    else:     
                        frontier.append(child)

            # UP
            if (row != self.size - 1):
                # getting the next state
                next_state = copy.deepcopy(node.curr_state)
                number_to_swap = next_state[row + 1][col]
                next_state[row + 1][col] = 0
                next_state[row][col] = number_to_swap

                child = Node(next_state, node, "UP", (row + 1, col))
                key = hash(next_state)
                if (key not in explored):
                    if (self.is_goal_state(child)):
                        return self.backtrack(child)
                    else:     
                        frontier.append(child)

            # DOWN    
            if (row != 0):
                # getting the next state
                next_state = copy.deepcopy(node.curr_state)
                number_to_swap = next_state[row - 1][col]
                next_state[row - 1][col] = 0
                next_state[row][col] = number_to_swap

                child = Node(next_state, node, "DOWN", (row - 1, col))
                key = hash(next_state)
                if (key not in explored):
                    if (self.is_goal_state(child)):
                        return self.backtrack(child)
                    else:     
                        frontier.append(child)
        
        return ["UNSOLVABLE"]
        # return ["LEFT", "RIGHT"]  # sample output

    # you may add more functions if you think is useful

    '''
    1. If the grid width is odd, then the number of inversions in a solvable situation is even.
    2. If the grid width is even, and the blank is on an even row counting from the bottom, 
    then the number of inversions in a solvable situation is odd.
    3. If the grid width is even, and the blank is on an odd row counting from the bottom 
    then the number of inversions in a solvable situation is even.
    '''
    # returns if an n by n puzzle is solvable
    def solvable(self):
        cpy = []
        inversions = 0
        for i in range(self.size):
            cpy.extend(self.init_state[i])
        for i in range(self.size**2):
            for j in range(i + 1, self.size**2):
                if ((cpy[i] > cpy[j]) and (cpy[j] != 0)):
                    inversions += 1

        if (self.size % 2 == 1 and inversions % 2 == 0):
            return True
        elif (self.size % 2 == 0):
            row = self.find_zero()[1] - self.size
            if (inversions % 2 == 0):
                if (row % 2 == 1):
                    return True
            else:
                if (row % 2 == 0):
                    return True
        return False

    # returns void and adds the prev moves directly onto actions in Puzzle instance
    def backtrack(self, node):
        result = list()
        while(node.parent != None):
            result.insert(0, node.prev_move)
            node = node.parent
        return result

    def find_zero(self):
        for i in range(self.size):
            for j in range(self.size):
                if (self.init_state[i][j] == 0):
                    return (i, j)    
    
    def is_goal_state(self, state):
        # can just directly equate matrices change later
        for i in range(self.size):
            for j in range(self.size):
                if (state[i][j] != self.goal_state[i][j]):
                    return False
        return True            

class Node:
    def __init__(self, curr_state, parent, prev_move, zero_position):
        self.curr_state = curr_state
        self.parent = parent
        self.prev_move = prev_move
        self.zero_position = zero_position


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
