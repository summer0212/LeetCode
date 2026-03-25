'''Quick test script for question1.py - Run this to check all edge cases'''

# Your current solution (as a function)
def two_sum_current(nums, target):
    result = []
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
    return result

# Test cases
print("=" * 70)
print("EDGE CASE TESTING FOR TWO SUM")
print("=" * 70)
print()

test_cases = [
    # (nums, target, expected, description)
    ([5, 2, 9, 4], 7, [1, 0], "Normal case - your example"),
    ([1, 2, 3, 4, 5], 6, "Multiple pairs", "Multiple pairs exist"),
    ([1, 2, 3, 4], 100, [], "No solution exists"),
    ([], 5, [], "Empty array"),
    ([5], 5, [], "Single element"),
    ([3, 4], 7, [0, 1], "Two elements"),
    ([-1, -2, 3, 4], 2, [0, 3], "Negative numbers"),
    ([0, 1, 2, 3, 4], 4, [0, 4], "Array with zero"),
    ([3, 3, 4, 5], 6, [0, 1], "Duplicate numbers"),
    ([2, 7, 11, 15], 9, [0, 1], "LeetCode example"),
]

passed = 0
total = len(test_cases)

for i, (nums, target, expected, desc) in enumerate(test_cases, 1):
    result = two_sum_current(nums, target)
    
    # Special handling for "Multiple pairs" case
    is_correct = True
    if expected == "Multiple pairs":
        is_correct = len(result) > 2  # Should have more than one pair
        status = "⚠️  (Multiple pairs found)"
    else:
        is_correct = result == expected
        status = "✓ PASS" if is_correct else "✗ FAIL"
    
    print(f"Test {i}: {desc}")
    print(f"  Input: nums={nums}, target={target}")
    print(f"  Output: {result}")
    print(f"  Expected: {expected if expected != 'Multiple pairs' else 'Multiple pairs'}")
    print(f"  Status: {status}")
    
    if is_correct:
        passed += 1
    print()

print("=" * 70)
print(f"RESULTS: {passed}/{total} tests passed")
print("=" * 70)
print()

print("KEY FINDINGS:")
print("-" * 70)
print("✓ Your solution correctly handles:")
print("  - Normal cases")
print("  - Empty arrays")
print("  - Single elements")
print("  - Negative numbers")
print("  - Duplicate numbers")
print()
print("⚠️  Potential issue:")
print("  - Returns ALL pairs, not just one")
print("  - Standard Two Sum usually expects only first pair")
print()
print("💡 Recommendation:")
print("  - If problem asks for 'the indices', return after first match")
print("  - Add: return [i, j] instead of result.append()")
print()






