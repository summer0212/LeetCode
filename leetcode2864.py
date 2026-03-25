class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        sorted_s = sorted(s,reverse=True) #Sorting based on ASCII values-> '0' has ASCII value 48, '1' has ASCII value 49
        # print(sorted_s)

        for i in range(len(sorted_s)-1, -1, -1):
            if sorted_s[i] == '1':
                sorted_s[i], sorted_s[-1] = sorted_s[-1], sorted_s[i]
                break
            
        print(sorted_s) 
        return ''.join(sorted_s)




object = Solution()
print(object.maximumOddBinaryNumber(s='0101'))

'''Logic:- After swapping all the '0' are coming in last and we have to find out the position where we get 1. 
            s = "0101"
lets sort it in a way that all 1's will be in front and 0's at last.

            s = "1100"
Since we have to return greatest odd number, there should be 
atleast one 1 at the end, so lets just swap only one 1 at the last.

But the catch is which 1 should we actually swap.

Lets find it out:

Lets swap with the first positioned 1 in the string.
            s = "1100"  =>  s = "0101"

Lets just try once more to swap it with the last positioned 
1 we have.
            s = "1100" =>  s = "1001"

Here we goooo, 
if we swapped with the last positioned 1 we are getting 
the greatest odd number.

Even if we had only one 1, this logic will still give desired output.

'''