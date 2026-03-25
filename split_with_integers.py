# ============================================
# Using split() with Integers
# ============================================

print("=" * 70)
print("CAN YOU USE split() ON AN INTEGER?")
print("=" * 70)
print()

print("❌ NO! split() only works on STRINGS, not integers")
print()

num = 2294
print(f"num = {num}")
print(f"type(num) = {type(num)}")
print()

print("Trying num.split() will give ERROR:")
print("-" * 70)
print("  num.split()  → AttributeError: 'int' object has no attribute 'split'")
print()

print("=" * 70)
print("SOLUTION: Convert to String First")
print("=" * 70)
print()

print("Step 1: Convert integer to string")
print("-" * 70)
num = 2294
num_str = str(num)
print(f"num = {num}")
print(f"num_str = str({num}) = '{num_str}'")
print(f"type(num_str) = {type(num_str)}")
print()

print("Step 2: Now you can use split()")
print("-" * 70)
# But split() needs a separator! For digits, we typically want to split each digit

# Method 1: Split doesn't work directly on digits without separator
# We need to think about what we want to split

print("What do you want to do?")
print()
print("Option 1: Convert to string and access individual characters")
print("-" * 70)
num = 2294
num_str = str(num)
print(f"num = {num}")
print(f"num_str = '{num_str}'")

# To get individual digits, you can:
digits_list = list(num_str)  # Convert string to list of characters
print(f"digits_list = list(num_str) = {digits_list}")

# Or convert back to integers
digits_int = [int(d) for d in num_str]
print(f"digits_int = [int(d) for d in num_str] = {digits_int}")
print()

print("Option 2: If you have a string with separators, use split()")
print("-" * 70)
num_str_separated = "22 94"  # String with space separator
result = num_str_separated.split()
print(f"num_str_separated = '{num_str_separated}'")
print(f"num_str_separated.split() = {result}")
print()

num_str_comma = "2,2,9,4"  # String with comma separator
result_comma = num_str_comma.split(',')
print(f"num_str_comma = '{num_str_comma}'")
print(f"num_str_comma.split(',') = {result_comma}")
print()

print("=" * 70)
print("COMMON USES: Getting Individual Digits")
print("=" * 70)
print()

num = 2294
print(f"Integer: {num}")
print()

print("Method 1: Convert to string, then to list")
print("-" * 70)
digits_str = list(str(num))
print(f"  list(str({num})) = {digits_str}")
print(f"  → List of strings: {digits_str}")
print()

print("Method 2: Convert to string, then to list of integers")
print("-" * 70)
digits_int = [int(d) for d in str(num)]
print(f"  [int(d) for d in str({num})] = {digits_int}")
print(f"  → List of integers: {digits_int}")
print()

print("Method 3: Using map()")
print("-" * 70)
digits_map = list(map(int, str(num)))
print(f"  list(map(int, str({num}))) = {digits_map}")
print(f"  → List of integers: {digits_map}")
print()

print("=" * 70)
print("EXAMPLE: Your Number 2294")
print("=" * 70)
print()

num = 2294
print(f"Given: num = {num}")
print()

print("Convert to string:")
num_str = str(num)
print(f"  str({num}) = '{num_str}'")
print()

print("Get individual digits (as strings):")
digits_as_strings = list(num_str)
print(f"  list('{num_str}') = {digits_as_strings}")
print()

print("Get individual digits (as integers):")
digits_as_ints = [int(d) for d in str(num)]
print(f"  [int(d) for d in str({num})] = {digits_as_ints}")
print()

print("Sum of digits:")
sum_digits = sum([int(d) for d in str(num)])
print(f"  sum([int(d) for d in str({num})]) = {sum_digits}")
print(f"  → 2 + 2 + 9 + 4 = {sum_digits}")
print()

print("=" * 70)
print("WHEN WOULD YOU USE split() ON NUMBERS?")
print("=" * 70)
print()

print("Scenario 1: Number as string with separators")
print("-" * 70)
date_str = "2024-12-25"
parts = date_str.split('-')
print(f"date_str = '{date_str}'")
print(f"date_str.split('-') = {parts}")
print()

print("Scenario 2: Number with spaces")
print("-" * 70)
num_with_spaces = "229 4"
parts = num_with_spaces.split()
print(f"num_with_spaces = '{num_with_spaces}'")
print(f"num_with_spaces.split() = {parts}")
print()

print("Scenario 3: Reading from input (which is a string)")
print("-" * 70)
print("user_input = input('Enter numbers: ')  # Returns string")
print("numbers = user_input.split()  # Split by spaces")
print()

print("=" * 70)
print("COMPARISON TABLE")
print("=" * 70)
print()

print("Task: Get individual digits from integer 2294")
print()
print("Method                     | Result")
print("-" * 70)
print("num.split()                | ❌ ERROR (int has no split)")
print("str(num).split()           | ['2294'] (no separator, stays as one)")
print("list(str(num))             | ['2', '2', '9', '4'] ✓")
print("[int(d) for d in str(num)] | [2, 2, 9, 4] ✓ (integers)")
print()

print("=" * 70)
print("PRACTICAL EXAMPLES")
print("=" * 70)
print()

num = 2294
print(f"Working with: {num}")
print()

# Example 1: Count digits
print("Example 1: Count number of digits")
digits = list(str(num))
print(f"  Number of digits: {len(digits)}")
print()

# Example 2: Reverse number
print("Example 2: Reverse the number")
reversed_digits = list(str(num))
reversed_digits.reverse()
reversed_num = int(''.join(reversed_digits))
print(f"  Reversed: {reversed_num}")
print()

# Example 3: Sum of digits
print("Example 3: Sum of all digits")
sum_of_digits = sum([int(d) for d in str(num)])
print(f"  Sum: {sum_of_digits}")
print()

# Example 4: Product of digits
print("Example 4: Product of all digits")
product = 1
for d in str(num):
    product *= int(d)
print(f"  Product: {product}")
print()

print("=" * 70)
print("QUICK REFERENCE")
print("=" * 70)
print()

print("To get individual digits from integer:")
print("  num = 2294")
print("  digits = [int(d) for d in str(num)]  # [2, 2, 9, 4]")
print()

print("To split a string containing numbers:")
print("  num_str = '22 94'")
print("  parts = num_str.split()  # ['22', '94']")
print()

print("Remember:")
print("  ✓ split() works on STRINGS")
print("  ✓ Convert int to string first: str(num)")
print("  ✓ To split digits, use list(str(num)) or list comprehension")
print()



