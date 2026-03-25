class Solution:
    def scoreOfString(self, s: str) -> int:
        # length = len(s)
        # # print("Length of string:", length)
        # # print(ord(s[0]))
        # total = 0
        # for i in range(0,length-1):
        #     print(ord(s[i]), ord(s[i+1]))
        #     total += abs(ord(s(i)) - ord(s(i+1)))
        # return total

        ascii_s = []
        sum = 0
        diff_val = 0
        for char in s:
            ascii_s.append(ord(char))
        print(ascii_s) #[104, 101, 108, 108, 111]
        
        for i in range(0,(len(ascii_s) - 1)):
            diff_val = abs(ascii_s[i] - ascii_s[i+1])
            sum += diff_val
        return sum

obj = Solution()
print(obj.scoreOfString("hello")  )# Example usage

# We can skip the second for loop and use a pairwise() function to generate an iterator that return consecutive, overlapping pairs from an iterable. Refer -> itertools.pairwise()
'''Syntax  : 
        from itertools import pairwise

        data = [1, 2, 3, 4, 5]
        for pair in pairwise(data):
            print(pair)

    Output : 
        (1, 2)
        (2, 3)
        (3, 4)
        (4, 5)
    
'''