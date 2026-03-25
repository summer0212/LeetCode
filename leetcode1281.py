n = 234
product = 1
sum = 0

while n>0:
    digit = n % 10
    n = n //10
    product = product * digit
    sum += digit
print(product)
print(sum)
