import math
import random

from model import State


class Node:

    def __init__(self, state: State, parent=None):
        self.state = state
        self.children = {}
        self.parent = parent
        self.wins = 0
        self.visited = 0
        self.percent = 0
        self.parent_played = 0
        self.ucb = float('inf')

    def add(self, pos):
        if pos in self.children.keys():
            return self.children[pos]
        else:
            next_node = Node(self.state.next(pos), self)
            self.children[pos] = next_node
            return next_node

    def update_win(self, val, parent_visited):
        self.visited += 1
        if self.state.max_turn:
            if val == 1:
                self.wins += 1
        if self.state.min_turn:
            if val != 1:
                self.wins += 1
        self.ucb = self.wins / self.visited + math.sqrt(2 * math.log2(parent_visited) / self.visited)

    def __eq__(self, other):
        return self.state == other.state

    def __str__(self):
        return f'{self.wins} / {self.visited} / {self.ucb:.3f}'


class Tree(Node):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
