card_values = {
    2: 1,
    3: 1,
    4: 1,
    5: 1,
    6: 1,
    10: -1,
    "J": -1,
    "Q": -1,
    "K": -1,
    "A": -1,
}


def count(cards):
    total = 0
    for card in cards:
        if card in card_values:
            total += card_values[card]
    return total


print(count([5, 9, 10, 3, "J", "A", 4, 8, 5]))  # ➞ 1
print(count(["A", "A", "K", "Q", "Q", "J"]))  # ➞ -6
print(count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]))  # ➞ 5
