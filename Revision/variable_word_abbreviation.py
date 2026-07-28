class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # Explorer 1 (for word) and Explorer 2 (for abbr)
        i = 0
        j = 0
        
        # Walk as long as BOTH explorers are still on their paths
        while i < len(word) and j < len(abbr):
            
            # CASE 1: Explorer 2 sees a LETTER
            if abbr[j].isalpha():
                # Do the letters match?
                if word[i] != abbr[j]:
                    return False
                # They match! Take 1 step forward.
                i += 1
                j += 1
                
            # CASE 2: Explorer 2 sees a NUMBER
            else:
                # Rule: Leading zeros are invalid
                if abbr[j] == '0':
                    return False
                
                # Eat the whole number
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = (num * 10) + int(abbr[j])
                    j += 1
                    
                # Warp Explorer 1 forward by 'num' steps
                i += num
                
        # FINAL CHECK: Did BOTH explorers reach the exact end of their strings perfectly?
        # If 'i' is larger than len(word), Explorer 1 fell off the cliff!
        return i == len(word) and j == len(abbr)
    
'''Note:- Why this is a masterpiece:
No extra memory: You didn't split the string or create new lists. Space Complexity is 
O
(
1
)
O(1)
.
Lightning fast: Both explorers only move forward. Time Complexity is 
O
(
N
)
O(N)
.
The Math Trick: Doing num = (num * 10) + int(char) is a classic computer science trick for building numbers from strings. It is much faster than doing string += char and casting it later!'''