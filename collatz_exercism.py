def steps(number):

    if not isinstance(number, int) or number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    count = 0

    while(number > 0):
        if number == 1:
            return 0
        
        elif number % 2 == 0:
            number = number // 2
            count += 1
            if number == 1:
                return count

        else :
            number = (number*3) + 1
            count += 1
            if number == 1:
                return count

    
print(steps(1))