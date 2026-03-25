def square(number):

    # if not isinstance(number , int) or number > 64:
    #     raise ValueError("square must be between 1 and 64")
    
    if  number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")


    grains = pow(2, (number-1))
    return grains


def total():
    total_grains = pow(2, 64)
    return total_grains

print(square(3))
print(total())
