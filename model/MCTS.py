import random

from model import Node, State, Tree


class MCTS:

    def __init__(self):
        pass

    @staticmethod
    def step(node: Node):
        node_selected = MCTS.selection(node)
        node_expanded = MCTS.expansion(node_selected)
        value = MCTS.simulation(node_expanded)
        curr = node_expanded
        while curr.parent:
            curr.update_win(value, curr.parent.visited+1)
            curr = curr.parent

    @staticmethod
    def selection(node: Node) -> Node:
        node.visited += 1
        curr = node
        while curr.children:
            curr = sorted(curr.children.values(), key=lambda x: x.ucb, reverse=True)[0]
            if curr.state.win() is not None:
                return curr
        return curr

    @staticmethod
    def expansion(node: Node):
        if len(node.state.valid_positions()) > 0:

            for move in node.state.valid_positions():
                node.add(move)
            return random.choice(list(node.children.values()))
        return node

    @staticmethod
    def simulation(node):
        while (state := node.state.win()) is None:
            idx = random.choice(node.state.valid_positions())
            node = Node(node.state.next(idx))
        return state


if __name__ == '__main__':
    tt = Tree(State.initial_state())
    for i in range(5000):
        MCTS.step(tt)
    MCTS.step(tt)
    MCTS.step(tt)
    MCTS.step(tt)
