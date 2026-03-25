def higher_card(card_one, card_two):
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
    

    if card_one in dict and card_two in dict:
        val_one = dict[card_one]
        print(val_one)
        val_two = dict[card_two]
        print(val_two)
        if val_one > val_two: 
            return card_one
        elif val_one == val_two:
            return card_two, card_one
        else : 
            return card_two
        
h=higher_card('K','A')