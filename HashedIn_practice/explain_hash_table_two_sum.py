# ============================================
# EXPLAINING: Hash Table Solution for Two Sum
# ============================================

print("=" * 70)
print("HASH TABLE SOLUTION FOR TWO SUM")
print("=" * 70)
print()

print("The optimized solution uses a hash table (dictionary) for O(n) time!")
print("Instead of checking all pairs, we only need ONE pass through the array.")
print()

# The solution code
def two_sum_hash(nums, target):
    seen = {}  # Dictionary: value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print("=" * 70)
print("CODE BREAKDOWN")
print("=" * 70)
print()

print("def two_sum_hash(nums, target):")
print("    seen = {}  # Dictionary to store: number → its index")
print("    for i, num in enumerate(nums):")
print("        complement = target - num")
print("        if complement in seen:")
print("            return [seen[complement], i]")
print("        seen[num] = i")
print("    return []")
print()

print("=" * 70)
print("KEY CONCEPT: COMPLEMENT")
print("=" * 70)
print()

print("Instead of asking: 'Do any TWO numbers sum to target?'")
print("We ask: 'Have I seen the COMPLEMENT of current number?'")
print()
print("Complement = target - current_number")
print()
print("Example:")
print("  If target = 9 and current number = 2")
print("  Complement = 9 - 2 = 7")
print("  Question: Have I already seen 7?")
print("  If yes → We found a pair! (2 + 7 = 9)")
print()

print("=" * 70)
print("STEP-BY-STEP WALKTHROUGH")
print("=" * 70)
print()

nums = [2, 7, 11, 15]
target = 9

print(f"Example: nums = {nums}, target = {target}")
print()

seen = {}
print("Initial state: seen = {}")
print()

for i, num in enumerate(nums):
    print(f"\n{'='*70}")
    print(f"Step {i+1}: Processing index {i}, number = {num}")
    print(f"{'='*70}")
    
    complement = target - num
    print(f"  Current number: {num}")
    print(f"  Complement needed: {target} - {num} = {complement}")
    print(f"  Question: Is {complement} in 'seen' dictionary? {complement in seen}")
    print(f"  Current 'seen' dictionary: {seen}")
    
    if complement in seen:
        print(f"\n  ✓ FOUND! {complement} is already in 'seen' at index {seen[complement]}")
        print(f"  Pair found: nums[{seen[complement]}] + nums[{i}] = {nums[seen[complement]]} + {nums[i]} = {target}")
        print(f"  Return: [{seen[complement]}, {i}]")
        break
    else:
        print(f"  ✗ Not found. Adding {num} to 'seen' dictionary at index {i}")
        seen[num] = i
        print(f"  Updated 'seen': {seen}")

print()
print("=" * 70)
print("VISUAL EXAMPLE WITH DETAILED STEPS")
print("=" * 70)
print()

nums2 = [5, 2, 9, 4]
target2 = 7

print(f"Example: nums = {nums2}, target = {target2}")
print()
print("We want to find: 2 + 5 = 7")
print()

seen2 = {}
print("Step-by-step process:")
print("-" * 70)

for i, num in enumerate(nums2):
    complement = target2 - num
    print(f"\n[{i}] Processing: nums[{i}] = {num}")
    print(f"    Complement: {target2} - {num} = {complement}")
    print(f"    Check: Is {complement} in seen? {complement in seen2}")
    
    if complement in seen2:
        print(f"    ✓ YES! Found {complement} at index {seen2[complement]}")
        print(f"    ✓ Pair: nums[{seen2[complement]}] ({nums2[seen2[complement]]}) + nums[{i}] ({num}) = {target2}")
        print(f"    ✓ Return: [{seen2[complement]}, {i}]")
        break
    else:
        print(f"    ✗ No, {complement} not in seen")
        seen2[num] = i
        print(f"    → Storing: seen[{num}] = {i}")
        print(f"    → Updated seen: {seen2}")

print()
print("=" * 70)
print("HOW IT WORKS: THE LOGIC")
print("=" * 70)
print()

print("The Key Insight:")
print("  We don't need to check all pairs!")
print("  Instead, for each number, we check if we've seen its complement.")
print()

print("Traditional approach (O(n²)):")
print("  For each number, check ALL other numbers")
print("  Example: [2, 7, 11, 15]")
print("    Check: 2 with 7, 2 with 11, 2 with 15")
print("    Check: 7 with 11, 7 with 15")
print("    Check: 11 with 15")
print("  Total: 6 comparisons for 4 elements")
print()

print("Hash table approach (O(n)):")
print("  For each number, check if complement exists in dictionary")
print("  Dictionary lookup is O(1) - very fast!")
print("  Example: [2, 7, 11, 15]")
print("    Process 2: complement = 5, not in dict → store 2")
print("    Process 7: complement = 0, not in dict → store 7")
print("    Process 11: complement = -4, not in dict → store 11")
print("    Process 15: complement = -8, not in dict → store 15")
print("  But wait, let's trace the correct example...")
print()

print("=" * 70)
print("CORRECT EXAMPLE: [2, 7, 11, 15], target = 9")
print("=" * 70)
print()

nums_correct = [2, 7, 11, 15]
target_correct = 9

seen_correct = {}
print("Processing each element:")
print()

for i, num in enumerate(nums_correct):
    complement = target_correct - num
    print(f"  [{i}] Number = {num}, Complement = {target_correct} - {num} = {complement}")
    
    if complement in seen_correct:
        print(f"      ✓ Found complement {complement} at index {seen_correct[complement]}!")
        print(f"      ✓ Answer: [{seen_correct[complement]}, {i}]")
        break
    else:
        seen_correct[num] = i
        print(f"      → Store {num} in dictionary at index {i}")
        print(f"      → seen = {seen_correct}")
    print()

print("=" * 70)
print("DATA STRUCTURE: DICTIONARY (Hash Table)")
print("=" * 70)
print()

print("seen = {}  is a dictionary (hash table)")
print()
print("Dictionary structure:")
print("  Key: The number (value from array)")
print("  Value: The index where we saw that number")
print()
print("Example:")
print("  seen = {2: 0, 7: 1}")
print("  Means: We saw number 2 at index 0")
print("         We saw number 7 at index 1")
print()

print("Why use dictionary?")
print("  ✓ Fast lookup: 'if complement in seen' is O(1)")
print("  ✓ Stores both number and its index")
print("  ✓ Easy to check if we've seen a number before")
print()

print("=" * 70)
print("COMPARISON: BRUTE FORCE vs HASH TABLE")
print("=" * 70)
print()

print("BRUTE FORCE (Your original solution):")
print("  Time: O(n²) - nested loops")
print("  Space: O(1) - no extra space")
print("  Code:")
print("    for i in range(len(nums)-1):")
print("        for j in range(i+1, len(nums)):")
print("            if nums[i] + nums[j] == target:")
print("                return [i, j]")
print()

print("HASH TABLE (Optimized):")
print("  Time: O(n) - single loop")
print("  Space: O(n) - dictionary storage")
print("  Code:")
print("    seen = {}")
print("    for i, num in enumerate(nums):")
print("        complement = target - num")
print("        if complement in seen:")
print("            return [seen[complement], i]")
print("        seen[num] = i")
print()

print("For array of size 1000:")
print("  Brute force: ~500,000 operations")
print("  Hash table: ~1,000 operations")
print("  Hash table is MUCH faster for large arrays!")
print()

print("=" * 70)
print("PRACTICE: TRACE THROUGH EXAMPLES")
print("=" * 70)
print()

def two_sum_hash_with_trace(nums, target):
    """Version with detailed trace output"""
    seen = {}
    print(f"\nInput: nums = {nums}, target = {target}")
    print("Tracing execution:")
    print()
    
    for i, num in enumerate(nums):
        complement = target - num
        print(f"  Step {i+1}: nums[{i}] = {num}")
        print(f"    Complement = {target} - {num} = {complement}")
        print(f"    Check: Is {complement} in seen? {complement in seen}")
        
        if complement in seen:
            print(f"    ✓ FOUND! Complement {complement} was seen at index {seen[complement]}")
            print(f"    ✓ Result: [{seen[complement]}, {i}]")
            return [seen[complement], i]
        else:
            seen[num] = i
            print(f"    → Add to seen: seen[{num}] = {i}")
            print(f"    → seen = {seen}")
    
    print("    ✗ No solution found")
    return []

# Practice examples
print("Example 1:")
two_sum_hash_with_trace([3, 3], 6)
print()

print("Example 2:")
two_sum_hash_with_trace([3, 2, 4], 6)
print()

print("Example 3:")
two_sum_hash_with_trace([-1, -2, -3, -4, -5], -8)
print()

print("=" * 70)
print("COMMON MISTAKES TO AVOID")
print("=" * 70)
print()

print("1. Adding to dictionary BEFORE checking:")
print("   ❌ WRONG:")
print("      seen[num] = i")
print("      if complement in seen:  # Will always find current num!")
print()
print("   ✓ CORRECT:")
print("      if complement in seen:  # Check first")
print("          return [seen[complement], i]")
print("      seen[num] = i  # Add after checking")
print()

print("2. Using wrong index:")
print("   ❌ WRONG: return [seen[complement], num]")
print("   ✓ CORRECT: return [seen[complement], i]")
print()

print("3. Not handling empty result:")
print("   ✓ Always return [] if no solution found")
print()

print("=" * 70)
print("FINAL SUMMARY")
print("=" * 70)
print()

print("Hash Table Solution:")
print("  1. Create empty dictionary 'seen'")
print("  2. For each number in array:")
print("     a. Calculate complement = target - current_number")
print("     b. Check if complement is in 'seen'")
print("     c. If yes → Return [index of complement, current index]")
print("     d. If no → Add current number to 'seen' dictionary")
print("  3. Return [] if no solution found")
print()

print("Benefits:")
print("  ✓ Fast: O(n) time complexity")
print("  ✓ Only one pass through array")
print("  ✓ Simple logic once you understand complement")
print()

print("Key Insight:")
print("  We don't need to check all pairs!")
print("  Just check if we've seen the complement of current number.")
print()






