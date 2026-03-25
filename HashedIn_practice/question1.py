'''Two Sum — Given array nums and target t, return indices of two numbers that sum to t'''

# from unittest import result


result = []

nums = [5,2,9,4]
target=7

for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            result.append(i) # Result = [[0, 1]]
            result.append(j)
        #return result
print(result)