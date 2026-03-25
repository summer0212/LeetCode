def value_of_ace(card_one, card_two):
    
    condition = card_one + card_two + 11

    if condition > 21:
        return 1
    else:
        return 11
    


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    list = ["A","K","Q","J","10"]
    for card in list:
        if card_one in list and card_two in list:
            return True
        else:
            return False
        
def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    dict = {
        "A" :1,
        "K" : 10,
        "J" : 10,
        "Q" : 10,
        "2" :2,
        "3" :3,
        "4" : 4,
        "5" :5,
        "6" :6,
        "7" : 7,
        "8" : 8,
        "9" : 9,
        "10" : 10
    }

   
    value_one = dict[card_one]
    value_two = dict[card_two]

    if value_one == value_two:
        return True
    else:
        return False
        

        
# print(is_blackjack("10", 'A'))
print(can_split_pairs('Q','2'))