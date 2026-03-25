'''Two Sum — Given array nums and target t, return indices of two numbers that sum to t'''

# Improved version - Returns only the first pair found

def two_sum(nums, target):
    """
    Find indices of two numbers that sum to target.
    Returns [i, j] if found, [] if no solution exists.
    """
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]  # Return immediately after finding first pair
    return []  # No solution found

# Test with your example
if __name__ == '__main__':
    nums = [5, 2, 9, 4]
    target = 7
    result = two_sum(nums, target)
    print(f"Input: nums={nums}, target={target}")
    print(f"Output: {result}")
    print(f"Explanation: nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {target}")






