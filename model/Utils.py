import pickle

import numpy as np


def win_positions():
    return np.array(([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                     [1, 4, 7], [2, 5, 8], [2, 4, 6], [0, 4, 8]))


def empty_array():
    return np.zeros(shape=9)


def print_board(state):
    blank = np.chararray(shape=(9,), unicode=True)
    for i in range(state.position.size):
        if state.position[i] == 1:
            blank[i] = "X"
        elif state.position[i] == -1:
            blank[i] = 'O'

    string = ("{:^3s}█{:^3s}█{:^3s}\n"
              "▄▄▄█▄▄▄█▄▄▄\n"
              "{:^3s}█{:^3s}█{:^3s}\n"
              "▀▀▀█▀▀▀█▀▀▀\n"
              "{:^3s}█{:^3s}█{:^3s}\n".format(*blank))
    print(string)


def save_tree(tree, file=None):
    file = file if file else "tree.dat"
    with open(file, 'wb') as fp:
        pickle.dump(tree, fp)


def load_tree(file=None):
    file = file if file else "tree.dat"
    with open(file, 'rb') as fp:
        return pickle.load(fp)
