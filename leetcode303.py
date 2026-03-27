class NumArray:

    def __init__(self, nums):
        # self.nums = nums
        n = len(nums)
        self.prefix_nums = [0] * (n+1) # Increasing the length of this because adding 0 at start
        # self.prefix_nums[0] = nums[0] -> We are not doing this because we are getting Index out of bound error. So, adding 0 in first index

        for i in range(0,n):
            self.prefix_nums[i+1] = self.prefix_nums[i] + nums[i]

        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_nums[right + 1] - self.prefix_nums[left]
        


# Your NumArray object will be instantiated and called as such:
#[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
obj = NumArray(nums = [-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(0,2)
param_2 = obj.sumRange(3,4)
param_3 = obj.sumRange(0,4)



'''👨‍🏫 Teacher Mode: Activated!

This is the most important question you could ask. Understanding exactly how this array is built is the entire secret to mastering Prefix Sums.

Think of a Prefix Sum Array like a Running Bank Balance.
Every time you look at a new number in nums, you are making a deposit (or a withdrawal if it's negative). The prefix array just records what your total balance is at that exact moment.

Let's do the math step-by-step!

Our Input: nums = [2, 0, 3, -5, 2, -1]

Step 1: The "Zero" (Before we start)

Before we look at any numbers in the array, what is our sum? It is 0.
We always put a 0 at the very beginning of a prefix array. (I will show you exactly why this 0 is so magical in a minute).

prefix = [0]

Step 2: The Running Total (Adding one by one)

Now, we walk through nums from left to right, adding the current number to our previous total.

Look at nums[0] which is 2:

Previous total was 0.

Math: 0 + 2 = 2.

prefix = [0, 2]

Look at nums[1] which is 0:

Previous total was 2.

Math: 2 + 0 = 2.

prefix = [0, 2, 2]

Look at nums[2] which is 3:

Previous total was 2.

Math: 2 + 3 = 5.

prefix =[0, 2, 2, 5]

Look at nums[3] which is -5:

Previous total was 5.

Math: 5 + (-5) = 0.

prefix = [0, 2, 2, 5, 0]

Look at nums[4] which is 2:

Previous total was 0.

Math: 0 + 2 = 2.

prefix = [0, 2, 2, 5, 0, 2]

Look at nums[5] which is -1:

Previous total was 2.

Math: 2 + (-1) = 1.

prefix = [0, 2, 2, 5, 0, 2, 1]

That is exactly how [0, 2, 2, 5, 0, 2, 1] was created!

If you look at the code I gave you, this exact math is happening in this one line:
self.prefix[i + 1] = self.prefix[i] + nums[i]
(Translation: The next box in my prefix array = The current total + the new number).

🌟 Why do we put a 0 at the very beginning?

You might be thinking: "Why not just make the prefix array the exact same size as nums? Why add that extra 0 at the start?"

Let's look at the Golden Formula again:
Sum = prefix[Right + 1] - prefix[Left]

Imagine LeetCode asks for sumRange(0, 2). They want the sum of the very first 3 numbers (2 + 0 + 3 = 5).

Right is 2. Right + 1 is 3. So we look at prefix[3], which is 5.

Left is 0. So we look at prefix[0], which is 0.

Formula: 5 - 0 = 5. It works perfectly!

What if we DIDN'T have that 0 at the start?
If prefix was just [2, 2, 5, 0, 2, 1]...
To get the sum from index 0 to 2, we would try to do prefix[2] - prefix[-1]. But wait! There is no prefix[-1]!
We would have to write messy if statements like:

code
Python
download
content_copy
expand_less
if left == 0:
    return prefix[right]
else:
    return prefix[right] - prefix[left - 1]

By simply slapping a 0 at the beginning of our prefix array, the formula prefix[right + 1] - prefix[left] works 100% of the time, flawlessly, without any extra if statements!'''