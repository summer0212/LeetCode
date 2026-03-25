class Solution:
    def minimumDifference(self, nums, k: int) -> int:
        if k == 1:
            return 0
        
        sorted_nums = sorted(nums)
        result = []

        for i in range(0,len(nums)-k +1):
            right = i + k -1

            diff = sorted_nums[right] - sorted_nums[i]

            result.append(diff)

        return min(result)
    
object = Solution()
print(object.minimumDifference(nums = [9,4,1,7], k = 2))
        

'''Notes:
This is a fantastic question. Setting the boundaries of a for loop is one of the most common places people get stuck in Sliding Window problems.

You are wondering: "Why len(sorted_nums) - k + 1? Why not just k + 1?"

The short answer is: k tells us how BIG the window is, but it does NOT tell us how MANY windows there are.

Let’s use a visual example to prove exactly why k + 1 will fail, and why that "extra calculation" is necessary.

The Visual Example

Imagine we have an array of 7 students, and we need to pick 3 of them.
nums =[10, 20, 30, 40, 50, 60, 70]

Length (N) = 7

Window size (k) = 3

We need to slide our window of size 3 from the left side all the way to the right side. Let's look at every possible starting index (i):

i = 0: [10, 20, 30] (Valid)

i = 1: [20, 30, 40] (Valid)

i = 2: [30, 40, 50] (Valid)

i = 3: [40, 50, 60] (Valid)

i = 4: [50, 60, 70] (Valid. We hit the end!)

Notice that our starting pointer i went from 0 up to 4.

What happens if we use your idea (range(k + 1))?

If k = 3, then k + 1 = 4.
Your loop for i in range(4): would run for i = 0, 1, 2, 3.
You completely missed the last window (i = 4)!

Worse, what if nums had 100 elements, and k = 3?
If you use range(k + 1), your loop will only check the first 4 windows, and it will completely ignore the remaining 94 windows!

The Math: Finding the "Stopping Point"

We need a formula that tells Python: "Stop sliding when the right edge of the window hits the end of the array."

The array length is N.

The window size is k.

If we put a window of size k at the very end of the array, where does its left edge (i) sit?

Formula: Last Starting Index = N - k

Let's test it with our example (N = 7, k = 3):
Last Starting Index = 7 - 3 = 4.
Exactly as we saw visually, index 4 is the very last place our window can start!

Because Python's range(x) stops before x, if we want the loop to include the number 4, we must write range(5).
Hence, the final formula is:
range((N - k) + 1)

Summary

k is how wide your hands are.

len(nums) is how long the table is.

len(nums) - k + 1 calculates exactly how many steps you can take along the table before your hands fall off the edge!'''