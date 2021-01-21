deck = input().split()
num_shuffle = int(input())

half = len(deck)//2

for i in range(num_shuffle):
    new_deck = []
    for index in range(half):
        first_card = deck[index]

        first_card_second_deck = index + half
        second_card = deck[first_card_second_deck]

        new_deck.append(first_card)
        new_deck.append(second_card)
    deck = new_deck

print(new_deck)


