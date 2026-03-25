str = "Geeks for geeks"

str = str.lower()
str = str.split() # split method converts the string into list of string, simply like array to char-array
# print(str)
dict = {}

for word in str:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

# print(max(dict))  --> Finding the maximum frequency word

print(dict)