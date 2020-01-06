import random

from model import Utils
from model.Node import Node, Tree
from model.State import State


class MCTS:

    def __init__(self):
        pass

    @staticmethod
    def step(node: Tree):
        node_selected = MCTS.selection(node)
        node_expanded = MCTS.expansion(node_selected)
        value = MCTS.simulation(node_expanded)
        curr = node_expanded
        node.visited += 1
        while curr.parent:
            curr.visited += 1
            curr.update_win(value, curr.parent.visited+1)
            curr = curr.parent
        curr.update_win(value)


    @staticmethod
    def selection(node: Node) -> Node:
        curr = node
        while curr.children:
            curr = sorted(curr.children.values(), key=lambda x: x.ucb, reverse=True)[0]
        return curr

    @staticmethod
    def expansion(node: Node):
        if node.state.win() is not None:
            return node
        for move in node.state.valid_positions():
            node.add(move)
        return random.choice(list(node.children.values()))

    @staticmethod
    def simulation(node):
        win = node.state.win()
        while win is None:
            idx = random.choice(node.state.valid_positions())
            node = Node(node.state.next(idx), idx)
            win = node.state.win()
        # Utils.print_board(node.state)
        return win


if __name__ == '__main__':
    tt = Tree(State.initial_state())
    for i in range(100):
        MCTS.step(tt)

