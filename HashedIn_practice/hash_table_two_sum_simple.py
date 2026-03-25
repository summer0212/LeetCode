"""
SIMPLE EXPLANATION: Hash Table Two Sum Solution
"""

# The code from your analysis file
def two_sum_hash(nums, target):
    seen = {}  # Dictionary to store: number → its index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# ============================================
# STEP-BY-STEP EXPLANATION
# ============================================

print("=" * 70)
print("WHAT EACH LINE DOES")
print("=" * 70)
print()

print("Line 1: seen = {}")
print("  → Create empty dictionary")
print("  → Will store: {number: index} for numbers we've seen")
print()

print("Line 2: for i, num in enumerate(nums):")
print("  → Loop through array with both index and value")
print("  → i = index (0, 1, 2, ...)")
print("  → num = value at that index")
print()

print("Line 3: complement = target - num")
print("  → Calculate what number we NEED to have seen before")
print("  → If we're at number 2 and target is 9, complement = 7")
print("  → Because 2 + 7 = 9")
print()

print("Line 4: if complement in seen:")
print("  → Check if we've ALREADY seen the complement")
print("  → Dictionary lookup is very fast (O(1))")
print()

print("Line 5: return [seen[complement], i]")
print("  → Found it! Return indices of both numbers")
print("  → seen[complement] = index where we saw the complement")
print("  → i = current index")
print()

print("Line 6: seen[num] = i")
print("  → Didn't find complement, so store current number")
print("  → Save it for future checks")
print()

print("=" * 70)
print("WALKTHROUGH EXAMPLE")
print("=" * 70)
print()

nums = [2, 7, 11, 15]
target = 9

print(f"Array: {nums}")
print(f"Target: {target}")
print(f"Looking for: ? + ? = {target}")
print()

seen = {}
print("Step 1: i=0, num=2")
print(f"  complement = {target} - 2 = {target - 2}")
print(f"  Is 7 in seen? {7 in seen} (seen is empty)")
print(f"  → Store 2: seen[{2}] = 0")
seen[2] = 0
print(f"  → seen = {seen}")
print()

print("Step 2: i=1, num=7")
print(f"  complement = {target} - 7 = {target - 7}")
print(f"  Is 2 in seen? {2 in seen} ✓ YES!")
print(f"  → Found pair! seen[{2}] = {seen[2]}, current i = 1")
print(f"  → Return [{seen[2]}, 1] = [0, 1]")
print(f"  → nums[0] + nums[1] = {nums[0]} + {nums[1]} = {nums[0] + nums[1]} ✓")
print()

print("=" * 70)
print("YOUR EXAMPLE: [5, 2, 9, 4], target = 7")
print("=" * 70)
print()

nums2 = [5, 2, 9, 4]
target2 = 7

print(f"Array: {nums2}")
print(f"Target: {target2}")
print(f"Looking for: 2 + 5 = 7")
print()

seen2 = {}

print("Step 1: i=0, num=5")
complement1 = target2 - 5
print(f"  complement = {target2} - 5 = {complement1}")
print(f"  Is {complement1} in seen? {complement1 in seen2}")
print(f"  → Store 5: seen[5] = 0")
seen2[5] = 0
print(f"  → seen = {seen2}")
print()

print("Step 2: i=1, num=2")
complement2 = target2 - 2
print(f"  complement = {target2} - 2 = {complement2}")
print(f"  Is {complement2} in seen? {complement2 in seen2} ✓ YES!")
print(f"  → Found! seen[{complement2}] = {seen2[complement2]}, current i = 1")
print(f"  → Return [{seen2[complement2]}, 1] = [0, 1]")
print(f"  → nums[0] + nums[1] = {nums2[0]} + {nums2[1]} = {nums2[0] + nums2[1]} ✓")
print()

print("=" * 70)
print("WHY IT'S FASTER")
print("=" * 70)
print()

print("Your original solution (nested loops):")
print("  Time: O(n²) - for array of size n, checks n×(n-1)/2 pairs")
print("  Example: [1,2,3,4,5] → checks 10 pairs")
print()

print("Hash table solution:")
print("  Time: O(n) - only one pass through array")
print("  Example: [1,2,3,4,5] → checks 5 times")
print()

print("For 1000 elements:")
print("  Nested loops: ~500,000 operations")
print("  Hash table: ~1,000 operations")
print("  Hash table is 500x faster!")
print()

print("=" * 70)
print("KEY INSIGHT: THE COMPLEMENT")
print("=" * 70)
print()

print("Instead of: 'Check if num1 + num2 = target'")
print("We think: 'Have I seen (target - current_num) before?'")
print()

print("Example:")
print("  Target = 10, Current number = 3")
print("  Question: Have I seen 7 before? (because 3 + 7 = 10)")
print("  If yes → Found pair!")
print("  If no → Remember 3 for later")
print()

print("=" * 70)
print("VISUAL: HOW DICTIONARY WORKS")
print("=" * 70)
print()

print("Dictionary structure: {number: index}")
print()
print("Example dictionary:")
seen_example = {5: 0, 2: 1}
print(f"  seen = {seen_example}")
print("  Meaning:")
print("    - Number 5 was seen at index 0")
print("    - Number 2 was seen at index 1")
print()

print("When we check: if complement in seen")
print("  Python quickly looks up if that number exists as a KEY")
print("  Dictionary lookup is O(1) - very fast!")
print()

print("=" * 70)
print("TRY IT YOURSELF")
print("=" * 70)
print()

# Test the function
test_cases = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
    ([5, 2, 9, 4], 7),
]

for nums, target in test_cases:
    result = two_sum_hash(nums, target)
    print(f"Input: nums={nums}, target={target}")
    if result:
        print(f"  Result: {result}")
        print(f"  Check: nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]} ✓")
    else:
        print(f"  Result: [] (no solution)")
    print()

print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()

print("The hash table solution:")
print("  1. Uses ONE loop instead of nested loops")
print("  2. For each number, checks if we've seen its complement")
print("  3. Stores each number in a dictionary as we go")
print("  4. Returns immediately when complement is found")
print("  5. Much faster: O(n) instead of O(n²)")
print()






