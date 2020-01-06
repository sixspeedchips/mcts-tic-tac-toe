import math

from model.State import State


class Node:

    def __init__(self, state: State, parent=None, move=-1):
        self.state = state
        self.children = {}
        self.parent = parent
        self.wins = 0
        self.visited = 0
        self.percent = 0
        self.parent_played = 0
        self.move = move
        self.ucb = float('inf')

    def add(self, pos):
        if pos in self.children.keys():
            return self.children[pos]
        else:
            next_node = Node(self.state.next(pos), self, move=pos)
            self.children[pos] = next_node
            return next_node

    def update_win(self, val, parent_visited=None):
        if self.state.min_turn:
            if val == 1:
                self.wins += 1
        else:
            if val == -1:
                self.wins += 1

        self.percent = self.wins / self.visited
        if parent_visited:
            self.ucb = self.percent + math.sqrt(2 * math.log2(parent_visited) / self.visited)

    def __eq__(self, other):
        return self.state == other.state

    def __str__(self):
        return f'{self.wins} / {self.visited} / {self.percent} / {self.ucb}'


class Tree(Node):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
