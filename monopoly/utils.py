def quantify(amount, quantifier):
    amount = int(amount)
    if quantifier == "M":
        amount *= 1000.0
    return amount
