import numpy as np

from model import *
from model import Utils


class State:

    def __init__(self, position):
        self.position = position
        self.turn = 1 if not self.position.sum() else -1

    def valid_positions(self):
        return np.where(self.position == 0)[0]

    def win(self):
        x = np.where(self.position == 1)[0]
        o = np.where(self.position == -1)[0]
        if any([False if np.setdiff1d(pos, x).size else True for pos in
                Utils.win_positions()]):
            return 1
        elif any([False if np.setdiff1d(pos, o).size else True for pos in
                  Utils.win_positions()]):
            return -1
        elif self.valid_positions().size == 0:
            return 0
        else:
            return None

    @property
    def min_turn(self):
        return self.turn == -1

    @property
    def max_turn(self):
        return self.turn == 1

    def next(self, next_pos: int = None):

        if next_pos is not None:
            copy = np.copy(self.position)
            copy[next_pos] = self.turn
            return State(copy)
        else:
            return State(np.copy(self.position))

    @staticmethod
    def initial_state():
        return State(Utils.empty_array())

    def __eq__(self, other):
        return np.all(other.position == self.position)

    def __str__(self):
        return str(self.position)
