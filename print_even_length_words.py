str = "This is my house"
str2 = ''

# Split a string into a list where each word is a list item

s = str.split(" ")
# print(s) #['This', 'is', 'my', 'house']

for i in s:
    # print(i) 
                    # This
                    # is
                    # my
                    # house
    if len(i) % 2 == 0:
        str2 = str2 + " "+ i
    
print(str2)


        

