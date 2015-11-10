class BankruptError(Exception):

    def __init__(self, player, amount):
        self.player = player
        self.amount = amount

    def __unicode__(self):
        return ("{} cannot pay ${}, he only has ${}!"
                .format(self.player.get_name(),
                        self.amount,
                        self.player.get_balance()))


class InputError(Exception):

    def __init__(self, message):
        self.message = message

    def __unicode__(self):
        return self.message
