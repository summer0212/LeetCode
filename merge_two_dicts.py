dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# result = {} No need of this

for i in dict2.keys():
    dict1[i] = dict2[i]
print(dict1)
    #The values here are simply being added in dict1 from dict2 from the key 'd'

#Another method using update()

dict1.update(dict2)
print(dict1)