str = "afghanistan"
str2 = ""

for i in range(len(str)):
    # print(i)
    even_dig = i % 2 
    
    if even_dig == 0:
        str2 = str2 + str[i]
print(str2)