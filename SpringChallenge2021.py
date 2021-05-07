import sys
import math
import enum

# creating a class cell so that we can store info for each cell
class Cell:
    def __init__(self, cellIndex,richness,neighbors):
        self.cellIndex = cellIndex
        self.richness = richness
        self.neighbors = neighbors

# creating a class tree so that we can store info for each tree
class Tree:
    def __init__(self, cellIndex, size, isMine, isDormant):
        self.cellIndex = cellIndex
        self.size = size
        self.isMine = isMine
        self.isDormant = isDormant

# creating a class actiontype to describe the different actions we can do
class ActionType(enum.Enum):
    WAIT = "WAIT"
    GROW = "GROW"
    SEED = "SEED"
    COMPLETE = "COMPLETE"

# creating a class action to do actions
class Action:
    def __init__(self, type, targetId=None,originId=None):
        self.type = type
        self.targetId = targetId
        self.originId = originId
    def __str__(self):
        if self.type == ActionType.WAIT:
            return "WAIT"
        elif self.type == ActionType.SEED:
            return f"SEED {self.originId} {self.targetId}"
        else: 
            return f"{self.type.name} {self.targetId}"
    @staticmethod
    def parse(action_string: str):
        split = action_string.split(" ")
        if split[0] == ActionType.WAIT.name:
            return Action(ActionType.WAIT)
        if split[0] == ActionType.GROW.name:
            return Action(ActionType.GROW,split[2],split[1])
        if split[0] == ActionType.SEED.name:
            return Action(ActionType.SEED,split[1]) 
        else:
            return Action(ActionType.COMPLETE, int(split[1]))

# class for Game play
class Game:
    def __init__(self):
        self.day = 0
        self.nutrients = 0
        self.mySun = 0
        self.myScore = 0
        self.oppSun = 0
        self.oppScore = 0
        self.oppIsWaiting = 0
        self.trees = []
        self.board =[]
        self.possibleActions = []
    def computeNextAction(self):
        return self.possibleActions[0]

# create a new instance of game
game = Game()

# code for cells
number_of_cells = int(input())
for i in range(number_of_cells):
    index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
    game.board.append(Cell(index,richness,(neigh_0,neigh_1,neigh_2,neigh_3,neigh_4,neigh_5)))

# game loop
while True:
    day = int(input())
    nutrients = int(input())
    game.day, game.nutrients = day, nutrients
    sun, score = [int(i) for i in input().split()]
    game.mySun = sun
    game.myScore = score
    inputs = input().split()
    opp_sun = int(inputs[0])  
    opp_score = int(inputs[1]) 
    opp_is_waiting = inputs[2] != "0"  # whether your opponent is asleep until the next day
    game.oppSun = opp_sun
    game.oppScore = opp_score
    game.oppIsWaiting = opp_is_waiting
    number_of_trees = int(input()) 
    game.trees.clear()
    for i in range(number_of_trees):
        inputs = input().split()
        cell_index = int(inputs[0])  # location of this tree
        size = int(inputs[1])  # size of this tree: 0-3
        is_mine = inputs[2] != "0"  # 1 if this is your tree
        is_dormant = inputs[3] != "0"  # 1 if this tree is dormant
        game.trees.append(Tree(cell_index,size,is_mine==1,is_dormant))
    number_of_possible_actions = int(input())
    for i in range(number_of_possible_actions):
        if game.mySun > 4:
            for j in range(number_of_trees):
                game.possibleActions.clear()
                tree = game.trees[j]
                if tree.isMine == 1:
                    idx = tree.cellIndex
                    game.possibleActions.append(Action(ActionType.COMPLETE,idx))
                    print(Action(ActionType.COMPLETE,idx))
                    possible_action = input()
                    # print(Action.parse(game.computeNextAction))


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


