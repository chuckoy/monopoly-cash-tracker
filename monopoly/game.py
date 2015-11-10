import argparse
import re
import sys

from errors import BankruptError
from gui import GUI
from player import Player
import utils


def main(argv):
    num_players = ''
    players = ''
    initial_money = ''
    parser = argparse.ArgumentParser(
        description='Monopoly Calculator (go paperless!)')
    parser.add_argument('num_players', metavar='num_players',
                        type=int, nargs=1,
                        help='The number of players that will play')
    parser.add_argument('players', metavar='players', nargs=1,
                        help='The (comma-separated) names of the players ' +
                             'who will play')
    parser.add_argument('initial_money', metavar='initial_money', nargs=1,
                        help='The amount of money players will start with ' +
                             'in millions or thousands.\n' +
                             'Format: <amount>(M/m/K/k)')
    args = parser.parse_args()

    num_players = args.num_players[0]
    players = args.players[0].split(",")
    for i, player in enumerate(players):
        players[i] = player.strip()
    if len(players) != int(num_players):
        print("Players given and number of players don't match!")
        sys.exit()

    initial_money = args.initial_money[0]
    valid_input = re.match(r'\d+\s*(M|m|K|k)', initial_money)
    if not valid_input:
        print("Wrong inital money format! Add quantifier at end!")
        sys.exit()
    amount = initial_money[:-1]
    quantifier = initial_money[-1].upper()

    monopoly = Monopoly(num_players, players, amount, quantifier)


class Monopoly:

    def __init__(self, num_players, players, amount, quantifier):
        self.num_players = int(num_players)
        self.players = []
        self.pooled_money = 0
        for pk, player in enumerate(players):
            self.players.append(Player(pk, player, int(amount), quantifier))
        self.play()

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
        print(type(self.pooled_money))
        print(type(utils.quantify(amount, quantifier)))
        self.pooled_money += utils.quantify(amount, quantifier)

    def collect_pool_money(self, name):
        print(self.pooled_money)
        print(type(self.pooled_money))
        player = self.find_player(name)
        player.modify_balance(self.pooled_money, 'K')

if __name__ == "__main__":
    main(sys.argv[1:])
