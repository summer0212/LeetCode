import re

s = "c1 O$d@eeD o1c"
str_filtered = ""  
s2 = ""  

pattern = r'[^a-zA-Z0-9]'

for i in s:
    # print(i)
    if not re.match(pattern, i):
        str_filtered += i

str_filtered = str_filtered.lower()
print(str_filtered)

for j in range(len(str_filtered) -1,-1,-1):
    s2 += str_filtered[j]
print(s2)

if s2 == str_filtered:
    print("OK")
else:
    print("NOT Ok")