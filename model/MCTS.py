import random

from model.Node import Node, Tree


class MCTS:

    def __init__(self):
        pass

    @staticmethod
    def step(node: Tree):
        node_selected = MCTS.selection(node)
        node_expanded = MCTS.expansion(node_selected)
        value = MCTS.simulation(node_expanded)
        curr = node_expanded
        while curr.parent:
            curr.visited += 1
            curr.update_win(value, curr.parent.visited+1)
            curr = curr.parent
        curr.visited += 1
        curr.update_win(value)


    @staticmethod
    def selection(node: Node) -> Node:
        curr = node
        while curr.children:
            curr = max(curr.children.values(), key=lambda x: x.ucb)
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
        while (win := node.state.win()) is None:
            idx = random.choice(node.state.valid_positions())
            node = Node(node.state.next(idx), idx)
        return win

