from errors import BankruptError
import utils


class Player:

    def __init__(self, pk, name, amount, quantifier):
        self.pk = pk
        self.name = name
        self.balance = utils.quantify(amount, quantifier)

    def get_pk(self):
        return self.pk

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def get_balance_display(self):
        if self.balance >= 1000.0:
            return str(self.balance / 1000.0) + 'M'
        else:
            return str(self.balance) + 'K'

    def modify_balance(self, amount, quantifier):
        money = utils.quantify(amount, quantifier)
        if self.balance + money < 0.0:
            raise BankruptError(self, money)
        else:
            self.balance += money
