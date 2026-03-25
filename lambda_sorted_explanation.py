# ============================================
# EXPLAINING: sorted(friends, key=lambda x: order.index(x))
# ============================================

print("=" * 60)
print("BREAKING DOWN: sorted(friends, key=lambda x: order.index(x))")
print("=" * 60)

# Setup
order = [3, 1, 2, 5, 4]
friends = [1, 3, 4]

print("\nGiven:")
print(f"  order = {order}")
print(f"  friends = {friends}")
print()

# ============================================
# PART 1: Understanding Lambda
# ============================================
print("=" * 60)
print("PART 1: What is lambda?")
print("=" * 60)
print()
print("Lambda syntax: lambda argument: expression")
print()
print("Example 1: Simple lambda")
square = lambda x: x * 2
print(f"  lambda x: x * 2")
print(f"  square(5) = {square(5)}")
print()
print("Example 2: Lambda with method call")
get_index = lambda x: order.index(x)
print(f"  lambda x: order.index(x)")
print(f"  For x=1: order.index(1) = {get_index(1)}")
print(f"  For x=3: order.index(3) = {get_index(3)}")
print()

# ============================================
# PART 2: How sorted() works with key parameter
# ============================================
print("=" * 60)
print("PART 2: How sorted() with key parameter works")
print("=" * 60)
print()
print("sorted(list, key=function) means:")
print("  1. Apply the 'key' function to each element")
print("  2. Sort based on the returned values")
print("  3. Return elements in sorted order")
print()

# ============================================
# PART 3: Step-by-step breakdown
# ============================================
print("=" * 60)
print("PART 3: Step-by-step breakdown of the statement")
print("=" * 60)
print()

print("Statement: sorted(friends, key=lambda x: order.index(x))")
print()

print("Step 1: What does lambda x: order.index(x) do?")
print("  - x is each element from friends list")
print("  - order.index(x) finds the position of x in order list")
print()

print("Step 2: For each friend, what is order.index(friend)?")
for i, friend in enumerate(friends):
    index = order.index(friend)
    print(f"  friends[{i}] = {friend}")
    print(f"    → order.index({friend}) = {index} (position in order list)")
    print()

print("Step 3: How does sorted() use these indices?")
print("  sorted() creates pairs: (friend, index_in_order)")
pairs = [(friend, order.index(friend)) for friend in friends]
for friend, idx in pairs:
    print(f"    ({friend}, {idx})")
print()

print("Step 4: sorted() sorts by the index (second value in pair)")
print("  Original pairs:", pairs)
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print("  Sorted by index:", sorted_pairs)
print()

print("Step 5: Extract just the friends (first value in pair)")
result = [friend for friend, _ in sorted_pairs]
print("  Result:", result)
print()

# ============================================
# PART 4: Visual walkthrough
# ============================================
print("=" * 60)
print("PART 4: Visual walkthrough")
print("=" * 60)
print()

print("Original: friends = [1, 3, 4]")
print("          order  = [3, 1, 2, 5, 4]")
print()
print("For each friend, find its index in order:")
print()

friend_1 = 1
idx_1 = order.index(friend_1)
print(f"  friend = {friend_1}")
print(f"    → Where is {friend_1} in order?")
print(f"    → order = [3, 1, 2, 5, 4]")
print(f"    →           ↑ index {idx_1}")
print(f"    → order.index({friend_1}) = {idx_1}")
print()

friend_3 = 3
idx_3 = order.index(friend_3)
print(f"  friend = {friend_3}")
print(f"    → Where is {friend_3} in order?")
print(f"    → order = [3, 1, 2, 5, 4]")
print(f"    →         ↑ index {idx_3}")
print(f"    → order.index({friend_3}) = {idx_3}")
print()

friend_4 = 4
idx_4 = order.index(friend_4)
print(f"  friend = {friend_4}")
print(f"    → Where is {friend_4} in order?")
print(f"    → order = [3, 1, 2, 5, 4]")
print(f"    →                     ↑ index {idx_4}")
print(f"    → order.index({friend_4}) = {idx_4}")
print()

print("Now sort friends by their indices:")
print(f"  [{friend_1} (index {idx_1}), {friend_3} (index {idx_3}), {friend_4} (index {idx_4})]")
print(f"  Sort by indices: [{idx_3}, {idx_1}, {idx_4}]")
print(f"  Result: [{friend_3}, {friend_1}, {friend_4}]")
print()

# ============================================
# PART 5: The actual code execution
# ============================================
print("=" * 60)
print("PART 5: Running the actual code")
print("=" * 60)
print()

result = sorted(friends, key=lambda x: order.index(x))
print(f"sorted(friends, key=lambda x: order.index(x))")
print(f"Result: {result}")
print()

# ============================================
# PART 6: Equivalent without lambda
# ============================================
print("=" * 60)
print("PART 6: Equivalent code without lambda")
print("=" * 60)
print()

print("Instead of using lambda, we can define a regular function:")
print()

def get_order_position(x):
    """Returns the index of x in the order list"""
    return order.index(x)

result_with_function = sorted(friends, key=get_order_position)

print("  def get_order_position(x):")
print("      return order.index(x)")
print()
print("  sorted(friends, key=get_order_position)")
print(f"  Result: {result_with_function}")
print()
print("Both approaches give the same result!")
print()

# ============================================
# PART 7: Summary
# ============================================
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print()
print("sorted(friends, key=lambda x: order.index(x))")
print()
print("1. lambda x: order.index(x)")
print("   → Creates a function that takes x and returns order.index(x)")
print()
print("2. sorted(friends, key=...)")
print("   → Sorts friends list")
print("   → Uses the lambda function to determine sort order")
print("   → For each friend, finds its position in order list")
print("   → Sorts friends based on their positions in order")
print()
print("3. Result:")
print("   → Friends are reordered based on where they appear in order list")
print(f"   → {friends} → {result}")
print()






