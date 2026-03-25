from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        dict = Counter(s) #AttributeError: 'Counter' object has no attribute 'sorted'
        dict = {}
        result = []
        for char in s:
            if char in dict:
                dict[char] +=1 

            else:
                dict[char] = 1
        '''sorted_dict = sorted(dict,key = dict.get, reverse = True) -> We are changing this line in a way that the sorted list of keys is as per the frequency + if there is a tie in frequency, then we sort the keys in lexicographical order (ascending)'''
        sorted_dict = sorted(dict, key= lambda x:(-dict[x],x))
        '''Key insight: Use a lambda function as the key in sorted() to sort first by frequency (negative for descending) and then by character (for tie-breaking in ascending order). This is Tuple Stratergy ki agar pehle wale me tie hua to dusre wale se sort karega. sorted() looks like this :- ['t', 'r', 'e'] then one by one sorted() hands over "t" to lambda. This function returns a tuple like this :- (-1,'t') and so on'''

        for element in sorted_dict:
            repeated_char = element * dict[element]
            result.append(repeated_char)
        
        
        return "".join(result)


object = Solution()
print(object.frequencySort(s = "tree"))
        
        