class Solution:
    def restoreString(self, s, indices) :
        # initializing a list with fixed index values
        output = [None] * len(s)
        # p`rint(output)
        for i in range(0,len(indices)):
            output[indices[i]] = s[i]
            print(output)

        result = "".join(output)
        return result


object = Solution()
print(object.restoreString( s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
        