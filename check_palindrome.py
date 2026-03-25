str = "amway"
str2 = ""

# Then first -1 represents the last index, then the second -1 represents the condition where to stop, and the last -1 represents how much move after iteration
for i in range(len(str) -1,-1,-1):
    str2 = str2 + str[i]

if str2 == str:
    print("palindrome")
else:
    print("Not palindrome")