# ============================================
# HOW TO FIND REPEATED NUMBERS IN AN INTEGER ARRAY
# ============================================

print("=" * 70)
print("METHOD 1: Using Dictionary/Map (Frequency Counting)")
print("=" * 70)

def findRepeated_method1(nums):
    """
    Count frequency of each number and return numbers that appear more than once
    """
    count_dict = {}
    result = []
    
    # Step 1: Count frequency of each number
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Step 2: Find numbers that appear more than once
    for key, value in count_dict.items():
        if value > 1:
            result.append(key)
    
    return result

# Example
nums1 = [1, 2, 3, 2, 4, 3, 5, 3]
result1 = findRepeated_method1(nums1)
print(f"Input: {nums1}")
print(f"Repeated numbers: {result1}")
print(f"Explanation: 2 appears 2 times, 3 appears 3 times")
print()

print("=" * 70)
print("METHOD 2: Using Set to Track Seen Numbers")
print("=" * 70)

def findRepeated_method2(nums):
    """
    Use a set to track numbers we've seen, add to result if we see it again
    """
    seen = set()
    repeated = set()
    
    for num in nums:
        if num in seen:
            repeated.add(num)
        else:
            seen.add(num)
    
    return list(repeated)

# Example
nums2 = [1, 2, 3, 2, 4, 3, 5, 3]
result2 = findRepeated_method2(nums2)
print(f"Input: {nums2}")
print(f"Repeated numbers: {result2}")
print()

print("=" * 70)
print("METHOD 3: Using Collections.Counter")
print("=" * 70)

from collections import Counter

def findRepeated_method3(nums):
    """
    Use Counter to count frequencies and filter numbers with count > 1
    """
    counter = Counter(nums)
    return [num for num, count in counter.items() if count > 1]

# Example
nums3 = [1, 2, 3, 2, 4, 3, 5, 3]
result3 = findRepeated_method3(nums3)
print(f"Input: {nums3}")
print(f"Repeated numbers: {result3}")
print()

print("=" * 70)
print("METHOD 4: Using List Comprehension with count()")
print("=" * 70)

def findRepeated_method4(nums):
    """
    For each number, count how many times it appears in the list
    Note: Less efficient for large arrays (O(n²))
    """
    result = []
    seen = set()
    
    for num in nums:
        if num not in seen:
            if nums.count(num) > 1:
                result.append(num)
                seen.add(num)
    
    return result

# Example
nums4 = [1, 2, 3, 2, 4, 3, 5, 3]
result4 = findRepeated_method4(nums4)
print(f"Input: {nums4}")
print(f"Repeated numbers: {result4}")
print()

print("=" * 70)
print("METHOD 5: Using Sorting (if you want sorted results)")
print("=" * 70)

def findRepeated_method5(nums):
    """
    Sort the array, then check adjacent elements
    """
    nums_sorted = sorted(nums)
    result = []
    
    for i in range(len(nums_sorted) - 1):
        if nums_sorted[i] == nums_sorted[i + 1]:
            # Only add if not already in result (avoid duplicates in result)
            if not result or result[-1] != nums_sorted[i]:
                result.append(nums_sorted[i])
    
    return result

# Example
nums5 = [1, 2, 3, 2, 4, 3, 5, 3]
result5 = findRepeated_method5(nums5)
print(f"Input: {nums5}")
print(f"Repeated numbers (sorted): {result5}")
print()

print("=" * 70)
print("COMPARISON OF ALL METHODS")
print("=" * 70)

test_array = [1, 2, 3, 2, 4, 3, 5, 3, 2]
print(f"Test array: {test_array}")
print(f"Frequency: 1→1, 2→3, 3→3, 4→1, 5→1")
print(f"Repeated numbers should be: [2, 3]")
print()

print("Method 1 (Dictionary):", findRepeated_method1(test_array))
print("Method 2 (Set):", findRepeated_method2(test_array))
print("Method 3 (Counter):", findRepeated_method3(test_array))
print("Method 4 (List count):", findRepeated_method4(test_array))
print("Method 5 (Sorting):", findRepeated_method5(test_array))
print()

print("=" * 70)
print("WHEN TO USE WHICH METHOD?")
print("=" * 70)
print()
print("✅ Method 1 (Dictionary):")
print("   - Best for most cases")
print("   - Easy to understand")
print("   - O(n) time complexity")
print("   - Can also tell you HOW MANY times each number repeats")
print()
print("✅ Method 2 (Set):")
print("   - Simple and clean")
print("   - O(n) time complexity")
print("   - Good if you just need to know WHICH numbers repeat")
print()
print("✅ Method 3 (Counter):")
print("   - Most Pythonic")
print("   - Very concise code")
print("   - O(n) time complexity")
print()
print("⚠️  Method 4 (count()):")
print("   - Slower for large arrays (O(n²))")
print("   - Not recommended for large datasets")
print()
print("✅ Method 5 (Sorting):")
print("   - Good if you need sorted results")
print("   - O(n log n) time complexity")
print("   - Useful when space is limited")
print()

print("=" * 70)
print("DETAILED WALKTHROUGH: Method 1 (Most Common)")
print("=" * 70)

nums_example = [1, 2, 3, 2, 4, 3, 5]
print(f"Array: {nums_example}")
print()

count_dict = {}
print("Step 1: Building frequency dictionary")
print("-" * 70)

for num in nums_example:
    print(f"Processing number: {num}")
    if num in count_dict:
        count_dict[num] += 1
        print(f"  → {num} already seen, count = {count_dict[num]}")
    else:
        count_dict[num] = 1
        print(f"  → {num} first time, count = 1")
    print(f"  Dictionary so far: {count_dict}")
    print()

print("Final dictionary:", count_dict)
print()

print("Step 2: Finding numbers with count > 1")
print("-" * 70)
result = []
for key, value in count_dict.items():
    if value > 1:
        print(f"  {key} appears {value} times → ADD to result")
        result.append(key)
    else:
        print(f"  {key} appears {value} time → SKIP")

print(f"\nResult: {result}")
print()

print("=" * 70)
print("PRACTICE PROBLEMS")
print("=" * 70)

practice_arrays = [
    [1, 1, 2, 3, 4],
    [5, 5, 5, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 3, 2, 1],
    []
]

for i, arr in enumerate(practice_arrays, 1):
    print(f"Problem {i}: {arr}")
    if arr:
        result = findRepeated_method1(arr)
        print(f"  Repeated numbers: {result if result else 'None'}")
    else:
        print(f"  Repeated numbers: [] (empty array)")
    print()






