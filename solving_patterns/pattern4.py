#         1   
#       2   2   
#     3   3   3   
#   4   4   4   4   
# 5   5   5   5   5  


n = 5
for i in range(n):
    for space in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(i+1,"  ", end="")
    print()