from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) :

        if len(p) > len(s):
            return []
        
        p_dict = Counter(p)
        window_dict = Counter()
        result = []
        left = 0
        k = len(p)

        for right in range(len(s) ):
            char_in = s[right]
            window_dict[char_in] += 1

            

            if (right - left + 1) > k:
                char_out = s[left]
                window_dict[char_out] -= 1

                if window_dict[char_out] == 0:
                    del window_dict[char_out]

                left += 1

            if (right - left + 1) == k:
                if window_dict == p_dict:
                    result.append(left)

        return result
    
object = Solution()
print(object.findAnagrams( s = "abab", p = "ab"))

'''You are making an excellent connection! You are remembering the exact formula we used for the Fixed-Size Sliding Window earlier.

The short answer is: Yes, you absolutely can use range(len(s) - k + 1)!

However, there is a very important catch: If you use that limit, your loop variable represents the left pointer (the starting index of the window), not the right pointer.

Let me explain the difference, and then I will show you how to write the code using your exact logic.

The Two Ways to Write a Fixed Window

Way 1: The "Right Pointer" Lead (What I wrote)

for right in range(len(s)):

Concept: The right pointer steps through every single letter of the string. The left pointer drags behind it to keep the window size at k.

Way 2: The "Left Pointer" Lead (Your idea)

for left in range(len(s) - k + 1):

Concept: We calculate exactly how many valid starting positions exist. We place the left pointer there, and the right pointer is just calculated as left + k - 1.

How to code your idea (The "Pro" Fixed Window)

If we use your loop boundary, we should initialize the very first window manually before the loop starts. Then, the loop just shifts the window by 1 step at a time.

Here is how your logic beautifully translates into code:

code
Python
download
content_copy
expand_less
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        if k > len(s):
            return[]
            
        p_count = Counter(p)
        result =[]
        
        # 1. Build the dictionary for the VERY FIRST window (indices 0 to k-1)
        window_count = Counter(s[:k])
        
        # Check if the first window is an anagram
        if window_count == p_count:
            result.append(0)
            
        # 2. Use YOUR loop limit! 
        # We start at index 1 because we already checked index 0 above.
        for left in range(1, len(s) - k + 1):
            
            # The character falling out of the window (on the left)
            char_out = s[left - 1]
            
            # The new character coming into the window (on the right)
            # If left is 1, and k is 3, the new right char is at index 1 + 3 - 1 = 3
            char_in = s[left + k - 1]
            
            # 3. Slide the dictionary!
            # Remove the old character
            window_count[char_out] -= 1
            if window_count[char_out] == 0:
                del window_count[char_out]
                
            # Add the new character
            window_count[char_in] += 1
            
            # 4. Check if we have an anagram
            if window_count == p_count:
                result.append(left) # 'left' is exactly our starting index!
                
        return result
Why your idea is actually the industry standard!

Many experienced programmers prefer the code I just wrote above (your idea) for Fixed-Size Windows because:

There is no need for a dynamic right - left + 1 > k check inside the loop. The window size is mathematically guaranteed.

left is explicitly the loop variable, which makes doing result.append(left) feel incredibly natural.

A Quick Warning (The TLE Trap):
If you use for left in range(len(s) - k + 1):, you might be tempted to do this inside the loop:
window_count = Counter(s[left : left + k])

Do not do that! That recreates the dictionary from scratch every single loop. If the string is 100,000 letters long, it will cause a Time Limit Exceeded error. Always use the "add one, remove one" slide technique shown above to keep it lightning-fast (
𝑂
(
𝑁
)
O(N)
)!'''