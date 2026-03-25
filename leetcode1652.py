class Solution:
    def decrypt(self, code, k: int) :
        result = [None]* len(code)

        for i in range(0,len(code)):
            if k > 0:
                result[i] = sum(code) - code[i]
            elif k == 0:
                result[i] = 0
            elif k < 0:
                # print("Checking when k is less than ",i," ",code[-i-1]," ",code[-i-2])
                # result[i] = code[-i] + code[-i-1]
                result[i] = code[i-1] + code[i-2]

        print(result)

object = Solution()
object.decrypt(code=[5,2,2,3,1], k = 3)
        