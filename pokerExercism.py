def get_rounds(number):
    return [number, number+1, number+2]

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    if number in rounds:
        return True
    return False

def card_average(hand):
    avg = sum(hand) / len(hand)
    return avg

def approx_average_is_average(hand):
    element_one = hand[0]
    last_one = hand[len(hand) - 1]
    stratergy_one = (element_one + last_one) / 2
    median = len(hand) // 2
    median_element = hand[median]
    avg = sum(hand) // len(hand)
    if avg == stratergy_one or avg == median_element:
        return True
    return False

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    # sum_even_places = sum(hand[0::2])
    # print(sum_even_places)
    # sum_odd_places = sum(hand[1::2])
    # print(sum_odd_places)
    # # elements = len(hand)//2
    # # print(elements)
    # avg_even = sum_even_places / elements
    # avg_odd = sum_odd_places / elements
    # if avg_even == avg_odd:
    #     return True
    # return False
    sum_even = 0
    count_even = 0
    sum_odd = 0
    count_odd = 0
    for index in range(len(hand)):
        if index % 2 == 0:
            sum_even += hand[index]
            count_even += 1
        else:
            sum_odd += hand[index]
            count_odd += 1

    avg_even = sum_even // count_even
    avg_odd = sum_odd // count_odd

    if avg_even == avg_odd:
        return True
    return False 

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    # print(hand[:-1])
    if hand[2] == 11:
        hand[2] = 11 * 2
    return hand

    

# # print(get_rounds(27))
# print(concatenate_rounds([27, 28, 29], [35, 36]))
# print(list_contains_round([27, 28, 29, 35, 36], 36))
# print(card_average([5, 6, 7]))
print(approx_average_is_average([2, 3, 4, 7, 8]))
# print(average_even_is_average_odd([1, 2, 3, 4]))
# print(maybe_double_last([5, 9, 10]))