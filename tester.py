list_of_lists = [[1, 2], [3, 4], [5]]

# We provide a start value of []
# This is like [] + [1, 2] + [3, 4] + [5]
flat_list = sum(list_of_lists, [])

print(flat_list)
# Output: [1, 2, 3, 4, 5]

# This would cause an error because you can't do 0 + [1, 2]
# sum(list_of_lists) 
# TypeError: unsupported operand type(s) for +: 'int' and 'list'