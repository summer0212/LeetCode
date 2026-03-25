class Solution:
    def sortSentence(self, s: str) -> str:
        '''print("Checking list func", list(str)) -> we cannot use list because sentence cannot be directly converted to a list. Using split is the only option with the delimiter .splt()'''

        words = s.split() #['is2', 'sentence4', 'This1', 'a3']
        ans = [None] * len(words)

        for word in words:
            index = int(word[-1])

            actual_word = word[:-1]

            ans[index - 1] = actual_word

        return " ".join(ans)


object = Solution()
print(object.sortSentence(s = "is2 sentence4 This1 a3"))

'''Another alternate method :-
def sortSentenceBruteForce(s):
    words = s.split() # ["is2", "sentence4", "This1", "a3"]
    count = len(words)
    result = []
    
    # Outer loop: Look for 1, then 2, then 3...
    for i in range(1, count + 1):
        target = str(i)
        
        # Inner loop: Scan all words to find the target
        for word in words:
            if word.endswith(target):
                # We found the word for position 'i'
                actual_word = word[:-1] # Remove last char
                result.append(actual_word)
                break
                
    return " ".join(result)
'''