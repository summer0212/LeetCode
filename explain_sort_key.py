# ============================================
# EXPLAINING: sort(key=)
# ============================================

print("=" * 70)
print("WHAT IS sort(key=)?")
print("=" * 70)
print()

print("sort(key=function) lets you control HOW elements are sorted")
print("The 'key' function is applied to each element to determine sort order")
print()

print("=" * 70)
print("BASIC SYNTAX")
print("=" * 70)
print()

print("Syntax:")
print("  list.sort(key=function)")
print("  sorted(list, key=function)")
print()

print("The key function:")
print("  - Is applied to EACH element")
print("  - Returns a value used for sorting")
print("  - Elements are sorted by this returned value")
print()

print("=" * 70)
print("EXAMPLE 1: Sort by Length of Strings")
print("=" * 70)
print()

words = ["apple", "pie", "banana", "cat"]
print(f"Original: {words}")
print()

# Sort by length
words_sorted = sorted(words, key=len)
print(f"sorted(words, key=len) = {words_sorted}")
print()

print("How it works:")
print("  - key=len applies len() to each word")
print("  - 'apple' → 5")
print("  - 'pie' → 3")
print("  - 'banana' → 6")
print("  - 'cat' → 3")
print("  - Sort by these values: 3, 3, 5, 6")
print("  - Result: ['pie', 'cat', 'apple', 'banana']")
print()

print("=" * 70)
print("EXAMPLE 2: Sort by Absolute Value")
print("=" * 70)
print()

numbers = [-5, 2, -1, 4, -3]
print(f"Original: {numbers}")
print()

# Sort by absolute value
numbers_sorted = sorted(numbers, key=abs)
print(f"sorted(numbers, key=abs) = {numbers_sorted}")
print()

print("How it works:")
print("  - key=abs applies abs() to each number")
print("  - -5 → 5")
print("  - 2 → 2")
print("  - -1 → 1")
print("  - 4 → 4")
print("  - -3 → 3")
print("  - Sort by: 1, 2, 3, 4, 5")
print("  - Result: [-1, 2, -3, 4, -5]")
print()

print("=" * 70)
print("EXAMPLE 3: Sort Tuples by Second Element")
print("=" * 70)
print()

pairs = [(1, 5), (2, 3), (3, 8), (4, 1)]
print(f"Original: {pairs}")
print()

# Sort by second element
pairs_sorted = sorted(pairs, key=lambda x: x[1])
print(f"sorted(pairs, key=lambda x: x[1]) = {pairs_sorted}")
print()

print("How it works:")
print("  - key=lambda x: x[1] gets second element of each tuple")
print("  - (1, 5) → 5")
print("  - (2, 3) → 3")
print("  - (3, 8) → 8")
print("  - (4, 1) → 1")
print("  - Sort by: 1, 3, 5, 8")
print("  - Result: [(4, 1), (2, 3), (1, 5), (3, 8)]")
print()

print("=" * 70)
print("EXAMPLE 4: Using Lambda Functions")
print("=" * 70)
print()

students = [
    ("Alice", 25),
    ("Bob", 20),
    ("Charlie", 30)
]
print(f"Original: {students}")
print()

# Sort by age (second element)
students_sorted = sorted(students, key=lambda x: x[1])
print(f"Sorted by age: {sorted(students, key=lambda x: x[1])}")
print()

# Sort by name length
students_sorted_name = sorted(students, key=lambda x: len(x[0]))
print(f"Sorted by name length: {students_sorted_name}")
print()

print("Lambda explanation:")
print("  lambda x: x[1]")
print("    - x is each element (tuple)")
print("    - x[1] is the second element (age)")
print("    - Returns age for sorting")
print()

print("=" * 70)
print("EXAMPLE 5: Sort List of Dictionaries")
print("=" * 70)
print()

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30}
]
print("Original:")
for p in people:
    print(f"  {p}")
print()

# Sort by age
people_sorted = sorted(people, key=lambda x: x["age"])
print("Sorted by age:")
for p in people_sorted:
    print(f"  {p}")
print()

print("=" * 70)
print("KEY POINTS")
print("=" * 70)
print()

print("1. key= is a parameter, not a method")
print("   ✓ sorted(list, key=function)")
print("   ✓ list.sort(key=function)")
print()

print("2. The key function is applied to each element")
print("   - Sort happens based on the RETURNED value")
print("   - Original elements stay the same")
print()

print("3. Common key functions:")
print("   - len → Sort by length")
print("   - abs → Sort by absolute value")
print("   - str.lower → Sort strings case-insensitive")
print("   - lambda → Custom sorting logic")
print()

print("4. sort() vs sorted():")
print("   - list.sort(key=...) → Modifies original list")
print("   - sorted(list, key=...) → Returns new sorted list")
print()

print("=" * 70)
print("COMPARISON: With vs Without key")
print("=" * 70)
print()

words = ["apple", "Pie", "banana", "Cat"]
print(f"Original: {words}")
print()

print("Without key (default alphabetical):")
words_default = sorted(words)
print(f"  sorted(words) = {words_default}")
print("  → Sorts by ASCII values (uppercase before lowercase)")
print()

print("With key (case-insensitive):")
words_case_insensitive = sorted(words, key=str.lower)
print(f"  sorted(words, key=str.lower) = {words_case_insensitive}")
print("  → Sorts ignoring case")
print()

print("=" * 70)
print("PRACTICAL EXAMPLE: Sort by Multiple Criteria")
print("=" * 70)
print()

students = [
    ("Alice", 20, "A"),
    ("Bob", 20, "B"),
    ("Charlie", 25, "A"),
    ("David", 20, "C")
]
print("Original (name, age, grade):")
for s in students:
    print(f"  {s}")
print()

# Sort by age, then by grade
students_sorted = sorted(students, key=lambda x: (x[1], x[2]))
print("Sorted by age, then grade:")
for s in students_sorted:
    print(f"  {s}")
print()

print("How it works:")
print("  key=lambda x: (x[1], x[2])")
print("  → Returns tuple (age, grade)")
print("  → Sort by age first, then by grade")
print()

print("=" * 70)
print("COMMON PATTERNS")
print("=" * 70)
print()

examples = [
    ("Sort numbers by value", "sorted([3,1,4,2])", sorted([3,1,4,2])),
    ("Sort by absolute value", "sorted([-3,1,-4,2], key=abs)", sorted([-3,1,-4,2], key=abs)),
    ("Sort strings by length", "sorted(['a','aaa','aa'], key=len)", sorted(['a','aaa','aa'], key=len)),
    ("Sort by second element", "sorted([(1,3),(2,1)], key=lambda x: x[1])", sorted([(1,3),(2,1)], key=lambda x: x[1])),
]

print("Common sorting patterns:")
print("-" * 70)
for desc, code, result in examples:
    print(f"{desc}:")
    print(f"  {code}")
    print(f"  → {result}")
    print()

print("=" * 70)
print("QUICK REFERENCE")
print("=" * 70)
print()

print("Basic usage:")
print("  sorted(list, key=function)")
print("  list.sort(key=function)")
print()

print("Built-in functions as key:")
print("  key=len         → Sort by length")
print("  key=abs         → Sort by absolute value")
print("  key=str.lower   → Sort strings case-insensitive")
print()

print("Lambda functions as key:")
print("  key=lambda x: x[1]           → Sort by second element")
print("  key=lambda x: x['age']       → Sort by dictionary key")
print("  key=lambda x: (x[1], x[2])   → Sort by multiple criteria")
print()

print("=" * 70)
print("YOUR LEEtCODE 1636 EXAMPLE")
print("=" * 70)
print()

# This is likely a problem about sorting by frequency
nums = [1, 1, 2, 2, 2, 3]
print(f"Array: {nums}")
print()

# Count frequencies
from collections import Counter
freq = Counter(nums)
print(f"Frequencies: {dict(freq)}")
print()

# Sort by frequency (ascending), then by value (descending if same freq)
sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))
print(f"Sorted by frequency, then by value: {sorted_nums}")
print()

print("Explanation:")
print("  key=lambda x: (freq[x], -x)")
print("  → Sort by (frequency, -value)")
print("  → Lower frequency first")
print("  → For same frequency, higher value first (negative for descending)")
print()



