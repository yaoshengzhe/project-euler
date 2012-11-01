#! /usr/bin/python

import sys

class CardRank:
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIRS = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9

    def __init__(self):
        self.card_rank_coll = ['HIGH_CARD',
                               'ONE_PAIR',
                               'TWO_PAIRS',
                               'THREE_OF_A_KIND',
                               'STRAIGHT',
                               'FLUSH',
                               'FULL_HOUSE',
                               'FOUR_OF_A_KIND',
                               'STRAIGHT_FLUSH',
                               'ROYAL_FLUSH']

    def get_card_rank(self, index):
        return self.card_rank_coll[index]

# return (type, list of card in descending order to compare)
def parse_five_hand_dealt(card_coll):
    if len(card_coll) != 5:
        raise Exception('We expect exact five cards. ' + str(card_coll))

    same_color = True
    color_table = {}
    card_table = {}
    type = CardRank.HIGH_CARD
    same_card_num = 1
    for card in card_coll:

        color_table[ card[1] ] = True
        if len(color_table.keys()) > 1:
            same_color = False
        val = None
        if card[0] == 'T':
            val = 10
        elif card[0] == 'J':
            val = 11
        elif card[0] == 'Q':
            val = 12
        elif card[0] == 'K':
            val = 13
        elif card[0] == 'A':
            val = 14
        else:
            val = int(card[0])

        card_table[val] = card_table.get(val, 0) + 1
        if card_table[val] > same_card_num:
            same_card_num = card_table[val]

    reversed_card_table = {}
    for k, v in card_table.items():
        reversed_card_table[v] = reversed_card_table.get(v, [])
        reversed_card_table[v].append(k)

    remain_card = []

    if same_card_num == 4:
        remain_card.extend(reversed_card_table[4])
        remain_card.extend(reversed_card_table[1])
        assert len(remain_card) == 2
        return (CardRank.FOUR_OF_A_KIND, remain_card)

    elif same_card_num == 3:
        if reversed_card_table.get(2, None) is None:
            remain_card.extend(reversed_card_table[1])
            remain_card.sort(reverse=True)
            remain_card.insert(0, reversed_card_table[3][0])
            assert len(remain_card) == 3
            return (CardRank.THREE_OF_A_KIND, remain_card)
        else:
            remain_card.extend(reversed_card_table[3])
            remain_card.extend(reversed_card_table[2])
            assert len(remain_card) == 2
            return (CardRank.FULL_HOUSE, remain_card)

    elif same_card_num == 2:
        if len(reversed_card_table[2]) == 2:
            remain_card.extend(reversed_card_table[2])
            remain_card.sort(reverse=True)
            remain_card.extend(reversed_card_table[1])
            assert len(remain_card) == 3
            return (CardRank.TWO_PAIRS, remain_card)
        else:
            remain_card.extend(reversed_card_table[2])
            remain_card.extend(sorted(reversed_card_table[1], reverse=True))
            assert len(remain_card) == 4
            return (CardRank.ONE_PAIR, remain_card)
    else:
        card_coll = sorted(reversed_card_table[1], reverse=True)

        if same_color:
            if card_coll[0] - card_coll[4] == 4:
                if card_coll[0] == 14:
                    return (CardRank.ROYAL_FLUSH, [14])
                else:
                    return (CardRank.STRAIGHT_FLUSH, [card_coll[0]])
            else:
                return (CardRank.FLUSH, card_coll)
        else:
            if card_coll[0] - card_coll[4] == 4:
                return (CardRank.STRAIGHT, [card_coll[0]])
            else:
                return (CardRank.HIGH_CARD, card_coll)

def compare_card_coll(a, b):
    if len(a) != len(b):
        raise Exception('Two card collection have different number of elements.')

    for i in range(len(a)):
        if a[i] > b[i]:
            return 1
        elif a[i] < b[i]:
            return -1
    return 0

def foo():
    count = 0

    for card_coll in [line.split() for line in sys.stdin.readlines()]:

        player_1 = parse_five_hand_dealt(card_coll[:5])
        player_2 = parse_five_hand_dealt(card_coll[5:])

        if player_1[0] > player_2[0]:
            #print 'player 1 win'
            #print CardRank().get_card_rank(player_1[0]), player_1[1]
            #print CardRank().get_card_rank(player_2[0]), player_2[1]

            count += 1
        elif player_1[0] == player_2[0] and compare_card_coll(player_1[1], player_2[1]) > 0:
            #print 'player 1 win'
            #print CardRank().get_card_rank(player_1[0]), player_1[1]
            #print CardRank().get_card_rank(player_2[0]), player_2[1]

            count += 1

            #print 'player 1 lose'
            #print CardRank().get_card_rank(player_1[0]), player_1[1]
            #print CardRank().get_card_rank(player_2[0]), player_2[1]

    return count

def main():
    print foo()

if __name__ == '__main__':
    main()
