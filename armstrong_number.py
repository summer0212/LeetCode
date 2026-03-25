number = 153

n = str(number)
# power = len(n)

def digit_count(number):
    count = 0
    while(number != 0):
        digit = number % 10
        count += 1
        number = number // 10
    return count

def check_if_armstrong_number(number):
    power = digit_count(number)
    n = number
    nw_number = 0
    while(number != 0):
        digit = number % 10
        nw_number = nw_number + (pow(digit,power))
        number = number // 10

    if nw_number == n:
        return True
    else:
        return False
    
print(check_if_armstrong_number(number)) # how do interpreter know ki yahn se shuru krna hai???


