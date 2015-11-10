def quantify(amount, quantifier):
    print("Amount: {}".format(amount))
    amount = int(amount)
    if quantifier == "M":
        amount *= 1000.0
    return amount
