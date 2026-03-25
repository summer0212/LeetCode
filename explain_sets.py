# ============================================
# EXPLAINING: seen = set() and repeated = set()
# ============================================

print("=" * 70)
print("WHAT IS A SET IN PYTHON?")
print("=" * 70)
print()

print("A set is a collection that:")
print("  ✓ Stores unique values (no duplicates)")
print("  ✓ Allows fast lookup (checking if something is in it)")
print("  ✓ Order doesn't matter")
print()

# Example of sets
example_set = {1, 2, 3, 2, 4}  # Duplicate 2 is removed
print("Example:")
print(f"  Creating set: {{1, 2, 3, 2, 4}}")
print(f"  Result: {example_set}  ← Duplicate removed!")
print()

print("=" * 70)
print("CREATING EMPTY SETS")
print("=" * 70)
print()

print("seen = set()")
print("  → Creates an empty set named 'seen'")
print("  → Will store numbers we have encountered")
print()

print("repeated = set()")
print("  → Creates an empty set named 'repeated'")
print("  → Will store numbers that appear more than once")
print()

# Show empty sets
seen = set()
repeated = set()

print("Initial state:")
print(f"  seen = {seen}")
print(f"  repeated = {repeated}")
print()

print("=" * 70)
print("WHY USE SETS INSTEAD OF LISTS?")
print("=" * 70)
print()

print("Sets are faster for:")
print("  1. Checking if something exists: 'if x in set' (very fast)")
print("  2. Adding items: 'set.add(x)' (very fast)")
print("  3. Automatically prevents duplicates")
print()

print("Lists are slower for:")
print("  - Checking if something exists: 'if x in list' (slow for large lists)")
print()

print("Example comparison:")
print("-" * 70)

# Using lists
seen_list = []
if 5 not in seen_list:  # Has to check entire list
    seen_list.append(5)
if 5 not in seen_list:  # Has to check entire list again
    seen_list.append(5)  # Would add duplicate!

print("Using lists:")
print(f"  seen_list = {seen_list}")
print(f"  Problem: Can have duplicates, slower lookup")
print()

# Using sets
seen_set = set()
seen_set.add(5)  # Fast!
seen_set.add(5)  # Automatically ignores duplicate
print("Using sets:")
print(f"  seen_set = {seen_set}")
print(f"  Benefit: No duplicates, very fast lookup")
print()

print("=" * 70)
print("HOW IT WORKS IN THE REPEATED NUMBERS ALGORITHM")
print("=" * 70)
print()

print("Code:")
print("  seen = set()        # Track numbers we've seen")
print("  repeated = set()    # Track numbers that repeat")
print()
print("  for num in nums:")
print("      if num in seen:")
print("          repeated.add(num)  # We've seen it before, so it's repeated!")
print("      else:")
print("          seen.add(num)      # First time seeing this number")
print()

print("=" * 70)
print("STEP-BY-STEP WALKTHROUGH")
print("=" * 70)
print()

nums = [1, 2, 3, 2, 4, 3, 5]
seen = set()
repeated = set()

print(f"Array: {nums}")
print()
print("Initial state:")
print(f"  seen = {seen}")
print(f"  repeated = {repeated}")
print()

print("Processing each number:")
print("-" * 70)

for i, num in enumerate(nums):
    print(f"\nStep {i+1}: Processing number {num}")
    print(f"  Is {num} in seen? {num in seen}")
    
    if num in seen:
        print(f"  → YES! We've seen {num} before")
        print(f"  → Add {num} to 'repeated'")
        repeated.add(num)
    else:
        print(f"  → NO! First time seeing {num}")
        print(f"  → Add {num} to 'seen'")
        seen.add(num)
    
    print(f"  Current state:")
    print(f"    seen = {seen}")
    print(f"    repeated = {repeated}")

print()
print("=" * 70)
print("FINAL RESULT")
print("=" * 70)
print()

print(f"Array: {nums}")
print(f"Numbers we saw: {seen}")
print(f"Numbers that repeated: {list(repeated)}")
print()

print("=" * 70)
print("VISUAL EXPLANATION")
print("=" * 70)
print()

print("Think of it like this:")
print()
print("'seen' set = A box where you put numbers you've seen")
print("'repeated' set = A box where you put numbers you've seen TWICE")
print()
print("As you go through the array:")
print("  - Each new number → Put in 'seen' box")
print("  - If number already in 'seen' box → Put in 'repeated' box")
print()

print("Example with [1, 2, 3, 2, 4, 3]:")
print()

seen_box = []
repeated_box = []

nums_vis = [1, 2, 3, 2, 4, 3]
for num in nums_vis:
    if num in seen_box:
        repeated_box.append(num)
        print(f"  Number {num}: Already in 'seen' → Add to 'repeated'")
        print(f"    seen box: {seen_box}")
        print(f"    repeated box: {repeated_box}")
    else:
        seen_box.append(num)
        print(f"  Number {num}: New! Add to 'seen'")
        print(f"    seen box: {seen_box}")
        print(f"    repeated box: {repeated_box}")

print()
print("=" * 70)
print("SET OPERATIONS YOU NEED TO KNOW")
print("=" * 70)
print()

# Create example sets
s = set()
print("Creating empty set:")
print("  s = set()")
print(f"  s = {s}")
print()

print("Adding elements:")
print("  s.add(1)")
s.add(1)
print(f"  s = {s}")
print()

print("  s.add(2)")
s.add(2)
print(f"  s = {s}")
print()

print("  s.add(2)  # Try adding duplicate")
s.add(2)
print(f"  s = {s}  ← Duplicate automatically ignored!")
print()

print("Checking if element exists:")
print(f"  Is 1 in s? {1 in s}")
print(f"  Is 5 in s? {5 in s}")
print()

print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()

print("seen = set()")
print("  → Empty set to track numbers we've encountered")
print("  → Used to remember: 'Have I seen this number before?'")
print()

print("repeated = set()")
print("  → Empty set to track numbers that appear more than once")
print("  → Used to collect: 'Which numbers are duplicates?'")
print()

print("Why sets?")
print("  → Fast lookup (checking 'if x in set' is very fast)")
print("  → No duplicates (can't accidentally add same number twice)")
print("  → Perfect for tracking 'seen' items")
print()






