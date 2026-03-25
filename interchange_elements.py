list = ['a','b','c','d']
temp = ''
len = len(list)
temp = list[len - 1]
list[len - 1] = list[0]
list[0] = temp
print(list)