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
        frontier = list(root)
        explored = dict()

        if (self.is_goal_state(root)):
            return []

        while (frontier):
            node = frontier.pop(0)

            hash_num = hash(node.curr_state)
            explored[hash_num] = node.curr_state
            
            row = node.zero_position[0]
            col = node.zero_position[1]

            # LEFT
            if (row != 0):
                # getting the next state
                next_state = node.curr_state # needs to be changed
                child_left = Node(next_state, node, "LEFT", (row - 1, col))
                key = hash(next_state)
                if (key not in explored):
                    if (self.is_goal_state(child_left)):
                        # goal state reached, need to backtrack
                        print("goal state reached")
                        break
                    else:     
                        frontier.append(child_left)

            # RIGHT
            if (row != self.size):
                # getting the next state
                next_state = node.curr_state # needs to be changed
                child_right = Node(next_state, node, "RIGHT", (row + 1, col))
                key = hash(next_state)
                if (key not in explored):
                    if (self.is_goal_state(child_right)):
                        # goal state reached, need to backtrack
                        print("goal state reached")
                        break
                    else:     
                        frontier.append(child_right)

            # UP
            if (col != 0):
                # getting the next state
                next_state = node.curr_state # needs to be changed
                child_up = Node(next_state, node, "UP", (row, col - 1))
                key = hash(next_state)
                if (key not in explored):
                    if (self.is_goal_state(child_up)):
                        # goal state reached, need to backtrack
                        print("goal state reached")
                        break
                    else:     
                        frontier.append(child_up)

            # DOWN    
            if (col != self.size):
                # getting the next state
                next_state = node.curr_state # needs to be changed
                child_down = Node(next_state, node, "DOWN", (row, col + 1))
                key = hash(next_state)
                if (key not in explored):
                    if (self.is_goal_state(child_down)):
                        # goal state reached, need to backtrack
                        print("goal state reached")
                        break
                    else:     
                        frontier.append(child_down)

        return ["LEFT", "RIGHT"]  # sample output

    # you may add more functions if you think is useful

    # yet to implement solvable function
    def solvable(self):
        return True

    def find_zero(self):
        for i in range(self.size):
            for j in range(self.size):
                if (self.init_state[i, j] == 0):
                    return (i, j)    
    
    def is_goal_state(self, state):
        for i in range(self.size):
            for j in range(self.size):
                if (state[i][j] != self.init_state[i][j]):
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
