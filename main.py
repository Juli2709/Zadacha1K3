def card_number(card):
    return '*' * len(card[:-4]) + card[-4:]
card = input()
print(card_number(card))

