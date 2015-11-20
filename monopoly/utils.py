def quantify(amount, quantifier):
    amount = float(amount)
    if quantifier == "M":
        amount *= 1000.0
    return amount
