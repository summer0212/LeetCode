str1 = 'abcdef'
str2 = 'defghia'

count = 0

for i in str1:
    if i in str2:
        count += 1
print(count)