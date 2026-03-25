#Ways to extract values in a dictionary:
# 1. loop on dict.keys()
# 2. loop on dict.values()
# 3. use '+' or append for concatinating
# 4.We can also use dict.extent 
# 5. difference between append and extend : append will directly attach the values whether it is a list or single element but extend will extract the elements from the list and then add

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

result = []

for key in test_dict.keys():
    result.append(test_dict[key])
    #res.append(test_dict[key])

print(result)