# ============================================
# EXPLAINING sort(key=) with LeetCode 1636 Example
# ============================================

print("=" * 70)
print("YOUR PROBLEM: Sort by Frequency")
print("=" * 70)
print()

print("Problem: Sort array by frequency")
print("  - If frequencies are same, sort by value (descending)")
print()

nums = [2, 3, 1, 3, 2]
print(f"Input: {nums}")
print()

# Step 1: Count frequencies
nums_dict = {}
for i in range(len(nums)):
    if nums[i] in nums_dict:
        nums_dict[nums[i]] += 1
    else:
        nums_dict[nums[i]] = 1

print("Step 1: Count frequencies")
print(f"  Frequency dictionary: {nums_dict}")
print(f"  Frequency: 1→1, 2→2, 3→2")
print()

print("=" * 70)
print("Step 2: Sort using key=")
print("=" * 70)
print()

print("We need to sort by:")
print("  1. Frequency (ascending - lower frequency first)")
print("  2. Value (descending - higher value first if same frequency)")
print()

print("Solution:")
print("  nums.sort(key=lambda x: (nums_dict[x], -x))")
print()

print("Breaking it down:")
print("-" * 70)
print("  lambda x: (nums_dict[x], -x)")
print()
print("  x = each element in nums")
print("  nums_dict[x] = frequency of x")
print("  -x = negative value (for descending order)")
print()

print("What happens for each element:")
print("-" * 70)

for num in set(nums):  # unique elements
    freq = nums_dict[num]
    key_value = (freq, -num)
    print(f"  Element {num}:")
    print(f"    Frequency: {freq}")
    print(f"    Key value: ({freq}, {-num})")
    print(f"    → Used for sorting")
    print()

print("Sort order:")
print("  - Lower frequency first: 1 comes before 2")
print("  - For same frequency (2,3 both have freq=2): higher value first")
print("    → -2 = -2, -3 = -3, so 3 comes before 2")
print()

# Actually sort
nums_sorted = nums.copy()
nums_sorted.sort(key=lambda x: (nums_dict[x], -x))

print(f"Result: {nums_sorted}")
print()

print("=" * 70)
print("COMPLETE CODE")
print("=" * 70)
print()

complete_code = '''
class Solution:
    def frequencySort(self, nums):
        nums_dict = {}
        
        # Count frequencies
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                nums_dict[nums[i]] += 1
            else:
                nums_dict[nums[i]] = 1
        
        # Sort by frequency, then by value (descending)
        nums.sort(key=lambda x: (nums_dict[x], -x))
        
        return nums
'''

print(complete_code)
print()

print("=" * 70)
print("HOW sort(key=) WORKS STEP BY STEP")
print("=" * 70)
print()

nums_example = [2, 3, 1, 3, 2]
freq_dict = {2: 2, 3: 2, 1: 1}

print(f"Array: {nums_example}")
print(f"Frequencies: {freq_dict}")
print()

print("For each element, calculate key value:")
print("-" * 70)
key_values = []
for num in nums_example:
    key_val = (freq_dict[num], -num)
    key_values.append((num, key_val))
    print(f"  Element {num}: key = {key_val}")

print()
print("Sort by key values (tuples sort lexicographically):")
print("-" * 70)
print("  (1, -1) → frequency=1 (lowest, comes first)")
print("  (2, -2) → frequency=2, value=-2")
print("  (2, -3) → frequency=2, value=-3")
print("  (2, -2) → frequency=2, value=-2")
print("  (2, -3) → frequency=2, value=-3")
print()
print("Sorted order:")
print("  1. (1, -1)  → element 1")
print("  2. (2, -3)  → element 3")
print("  3. (2, -3)  → element 3")
print("  4. (2, -2)  → element 2")
print("  5. (2, -2)  → element 2")
print()

# Verify
result = sorted(nums_example, key=lambda x: (freq_dict[x], -x))
print(f"Final result: {result}")
print()

print("=" * 70)
print("KEY CONCEPTS")
print("=" * 70)
print()

print("1. lambda x: ... creates an anonymous function")
print("   - x is each element")
print("   - Returns value used for sorting")
print()

print("2. (nums_dict[x], -x) returns a tuple")
print("   - Tuples sort by first element, then second")
print("   - (frequency, -value) sorts by freq first, then value")
print()

print("3. Negative value (-x) for descending")
print("   - -3 < -2 (for descending order)")
print()



