import random


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'card({self.rank},{self.suit})'


class Deck(Card):
    # digits = [x for x in range(6,11)]
    # print(digits)
    rus_rank_list = {'V', 'Q', 'K', 'A'}
    rus_rank_list.update([x for x in range(6, 11)])
    print( rus_rank_list)
    # rus_rank_list = {'6', '7','8','9','10','V', 'Q', 'K', 'A'}
    suit_list = {"b", "c", "d", "e"}

    def __init__(self, rank = "", suit="", card_type="rus"):
        super().__init__(rank, suit)
        self.card_set = []
        for i in (self.rus_rank_list):
            for j in (self.suit_list):
                card = Card(i, j)
                self.card_set.append(card)

    def __str__(self):
        result: str =''
        for item in self.card_set:
            result += item.__str__()
        return result

    def get_random_card(self):
        if not self.card_set:
            return None
        item = random.choice(self.card_set)
        self.card_set.remove(item)
        return item


my_desk = Deck()
print(my_desk)
i = 1
while True:
    if not my_desk:
        break
    my_card = my_desk.get_random_card()
    if my_card is None:
        break
    print(i, my_card)
    i +=1

