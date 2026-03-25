class Solution:
    def reverseDegree(self, s):
        sum = 0
        mul = 1
        s_lowercase = s.lower()
        map = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        value = 26
        for char in alphabet:
            map[char] = value
            value -= 1
        # print(map)

        for i in range(0,len(s_lowercase)):
            mul = map[s_lowercase[i]] * (i+1)
            print(mul)
            sum += mul
        print(sum)
        return sum

object = Solution()
object.reverseDegree("abc")