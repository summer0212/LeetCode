class Solution:
    def findWordsContaining(self, words, x):
        result = []
        for i in range(len(words)):
            if x in words[i]:
                result.append(i)
        return result
    
object = Solution()
# object.findWordsContaining(["hello", "world", "leetcode"], "o")  
print(object.findWordsContaining(["hello", "world", "leetcode"], "o"))  # Output: [0, 1]


'''
Edge case for the below given code:
result = []
        
        for word in words:
            print(words.index(word))
            if x in word:
                result.append(words.index(word))

Answer :- Why it fails with duplicates:
index() always returns the first position where it finds the value, not the current position.
When all words are the same, index() always returns 0 (the first occurrence).
So even when you're on the 3rd or 5th word, index() still returns 0 because it finds the first match at the start.

Explain me why for the given output i am getting wrong answer:
[ "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"], x = "a"))

Why is the answer coming like this:
[0, 0, 0, 0, 0, 0, 0, 0, 0]

'''