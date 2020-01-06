import time
from abc import ABC

from model.MCTS import MCTS
from model.Node import Tree, Node
from model.State import State
from model.Utils import print_board


class Game:
    def __init__(self, players):
        self.players = players
        self.tt = Tree(State.initial_state())

    def start(self):
        turn = 0
        while self.tt.state.win() is None:
            current_player = self.players[turn % 2]
            turn += 1
            print_board(self.tt.state)
            move = current_player.play_move(self.tt)
            self.tt = Node(self.tt.state.next(move), move=move)

        print_board(self.tt.state)
        if self.tt.state.win() == 1:
            print("X has won the game!")
        elif self.tt.state.win() == -1:
            print("O has won the game!")
        else:
            print("The game was a draw.")


class Player(ABC):

    def __init__(self):
        pass

    def play_move(self, node):
        pass


class HumanPlayer(Player):

    def __init__(self):
        super().__init__()

    def play_move(self, node):
        while (selected := int(input(
            "Select a position: ")) - 1) not in node.state.valid_positions():
            continue
        return selected


class ComputerPlayer(Player):

    def __init__(self):
        super().__init__()

    def play_move(self, node):
        start = time.time_ns()
        while time.time_ns() - start < 1000028200:
            MCTS.step(node)

        move = \
            sorted(node.children.values(), key=lambda x: x.percent,
                   reverse=True)[
                0].move
        return move


if __name__ == '__main__':
    while True:
        game = Game(players=[ComputerPlayer(), HumanPlayer()])
        game.start()
