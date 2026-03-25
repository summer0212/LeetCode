prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
diff = []
temp_diff = []

# --------why this is error?-------

for i in range(0,len(prices)-1):
    for j in range(i+1,len(prices)):
        temp_diff.append(prices[j] - prices[i])
    print(temp_diff)
    
    max_diff = max(temp_diff)
    diff.append(max_diff)
    temp_diff = [] 

    print(diff)

# print(diff)

# ----------without error---------
# for i in range(0,len(prices)):
#     temp_diff = []
#     for j in range(i+1, len(prices)):
#         temp_diff.append(prices[j] - prices[i])

#     if temp_diff:
#         max_diff = max(temp_diff)
#         diff.append(max_diff)
#     else:
#         diff.append(0)

# print(diff)
# result =max(diff)
# print(result)