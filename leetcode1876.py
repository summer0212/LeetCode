class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        right = 3
        arr = []

        for i in range(0,len(s)):
            try:
                if right <= len(s):
                    arr.append(s[i:right])
                    right += 1
            except Exception as e:
                print(e)

        no_repeats = [elements for elements in arr if len(set(elements)) == len(elements)]

        return len(no_repeats)

object = Solution()
print(object.countGoodSubstrings(s = "aababcabc"))
            

'''Alternate method:
 all_substrings=[]
        
        for left in range(0,(len(s) - 3 + 1)):
            right = left + 3 -1
            
            new_substring = s[left:right + 1]
            
            if len(set(new_substring)) == len(new_substring) :
               
                all_substrings.append(new_substring)
        return len(all_substrings)'''