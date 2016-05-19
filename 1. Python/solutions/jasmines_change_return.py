total = int(input("Please enter change: "))

COINS = [("quarters", 25), ("centivos", 20), ("dimes", 10), ("nickels", 5), ("pennies", 1)]

def getResultAndRemainder(coin_value):
    """Given a coin value, return a tuple of the number of coins and the remaining value"""
    return (total // coin_value, total % coin_value)

for coin_name, coin_value in COINS:
    result, total = getResultAndRemainder(coin_value)
    print(result, " ", coin_name)
