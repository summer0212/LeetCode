# Two Sum Problem - Solution Analysis

## Your Current Solution

```python
result = []
nums = [5,2,9,4]
target=7

for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            result.append(i)
            result.append(j)

print(result)
```

## Edge Cases to Test

### ✅ What Works Well:
1. **Normal case**: Finds pairs correctly
2. **Uses different indices**: `range(i+1, len(nums))` prevents using same index twice
3. **Handles empty array**: Won't crash (just returns empty list)
4. **Handles negatives, zeros**: Algorithm works fine

### ⚠️ Potential Issues:

#### 1. **Multiple Pairs Problem**
- **Issue**: Your solution finds ALL pairs that sum to target
- **Example**: `nums = [1,2,3,4,5]`, `target = 6`
  - Pairs: (1,5) and (2,4) both sum to 6
  - Your output: `[0,4,1,3]` (all indices)
  - Standard Two Sum expects: `[0,4]` (just one pair)
- **Fix**: Return immediately after finding first pair

#### 2. **Result Format**
- **Current**: Flat list `[i, j, i2, j2, ...]`
- **Standard**: Usually just `[i, j]` for one pair
- **Question**: Does problem ask for "the indices" or "all pairs"?

#### 3. **No Solution Handling**
- **Current**: Returns `[]` if no solution
- **Usually fine**, but check problem requirements

## Edge Cases Test Results

### Test 1: Normal Case ✅
```
nums = [5, 2, 9, 4], target = 7
Expected: [1, 0] (indices of 2 and 5)
Your result: [1, 0] ✓
```

### Test 2: Multiple Pairs ⚠️
```
nums = [1, 2, 3, 4, 5], target = 6
Pairs: (1,5) and (2,4) both sum to 6
Your result: [0, 4, 1, 3]
Standard: Usually expects [0, 4] or [1, 3]
```

### Test 3: No Solution ✅
```
nums = [1, 2, 3], target = 100
Your result: [] ✓
```

### Test 4: Empty Array ✅
```
nums = [], target = 5
Your result: [] ✓ (doesn't crash)
```

### Test 5: Single Element ✅
```
nums = [5], target = 5
Your result: [] ✓ (needs 2 elements)
```

### Test 6: Two Elements ✅
```
nums = [3, 4], target = 7
Your result: [0, 1] ✓
```

### Test 7: Negative Numbers ✅
```
nums = [-1, -2, 3, 4], target = 2
Works fine ✓
```

### Test 8: Duplicate Numbers ✅
```
nums = [3, 3, 4], target = 6
Your result: [0, 1] ✓ (both 3s)
```

## Recommended Improvements

### Version 1: Return First Pair Only (Standard)
```python
def two_sum(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]  # Return immediately
    return []  # No solution
```

### Version 2: Return All Pairs (If Required)
```python
def two_sum_all_pairs(nums, target):
    result = []
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append([i, j])  # List of pairs
    return result
```

### Version 3: As a Function (Better Practice)
```python
def two_sum(nums, target):
    """Find indices of two numbers that sum to target"""
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Test
if __name__ == '__main__':
    nums = [5, 2, 9, 4]
    target = 7
    result = two_sum(nums, target)
    print(result)  # [1, 0]
```

## Time Complexity
- **Current**: O(n²) - nested loops
- **Space**: O(1) if returning first pair, O(n) if storing all pairs

## Optional: Optimized Hash Table Solution
For better time complexity (O(n) instead of O(n²)):
```python
def two_sum_hash(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```






