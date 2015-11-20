import argparse
import re
import sys

from gui import GUI
from player import Player
import utils


def main(argv):
    players = ('A', 'B', 'C', 'D')
    amount = '15'
    quantifier = 'M'
    parser = argparse.ArgumentParser(
        description='Monopoly Calculator (go paperless!)')
    parser.add_argument('-players', metavar='players', nargs=1,
                        help='The (comma-separated) names of the players ' +
                             'who will play')
    parser.add_argument('-initial_money', metavar='initial_money', nargs=1,
                        help='The amount of money players will start with ' +
                             'in millions or thousands.\n' +
                             'Format: <amount>(M/m/K/k)')
    args = parser.parse_args()

    if args.players:
        players = args.players[0].split(",")
        for i, player in enumerate(players):
            players[i] = player.strip()

    if args.initial_money:
        initial_money = args.initial_money[0]
        valid_input = re.match(r'\d+\.{0,1}\d*(M|m|K|k)', initial_money)
        valid_input = True
        if not valid_input:
            print("Wrong inital money format! Add quantifier at end!")
            sys.exit()
        amount = initial_money[:-1]
        quantifier = initial_money[-1].upper()

    monopoly = Monopoly(players, amount, quantifier)
    monopoly.play()


class Monopoly:

    def __init__(self, players, amount, quantifier):
        self.num_players = len(players)
        self.players = []
        self.pooled_money = 0
        for pk, player in enumerate(players):
            self.players.append(Player(pk, player, float(amount), quantifier))

    def play(self):
        gui = GUI(self)

    def get_players(self):
        return self.players

    def get_player_names(self):
        names = []
        for player in self.players:
            names.append(player.get_name())
        return names

    def get_player_monies(self):
        monies = []
        for player in self.players:
            monies.append(player.get_balance())
        return monies

    def get_num_players(self):
        return self.num_players

    def find_player(self, name):
        for player in self.players:
            if player.get_name() == name:
                return player
        return

    def add_money(self, name, amount, quantifier):
        player = self.find_player(name)
        player.modify_balance(float(amount), quantifier)
        self.pooled_money = 0

    def deduct_money(self, name, amount, quantifier):
        player = self.find_player(name)
        player.modify_balance(float(amount) * -1, quantifier)

    def pool_money(self, amount, quantifier):
        self.pooled_money += utils.quantify(amount, quantifier)
        print('total pooled money: ', self.pooled_money)

    def collect_pool_money(self, name):
        player = self.find_player(name)
        player.modify_balance(self.pooled_money, 'K')
        self.pooled_money = 0
        print('total pooled money: ', self.pooled_money)

if __name__ == "__main__":
    main(sys.argv[1:])
