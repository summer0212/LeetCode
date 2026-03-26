nums = [-2, 0, 3, -5, 2, -1]

#prefix_sum = [0,-2,-2, 1, -4, -2, -3]

# result = [0] * (len(nums)+ 1)
result = []
store = 0
for num in nums:
    # store = num + result[i]
    store += num
    result.append(store)

print(result)
