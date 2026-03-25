# print(bin(9))
# print(9 ^ 14)
class Solution:
    def decode(self, encoded, first) :
        arr = []
        # arr[0] = first
        arr.append(first)
        for i in range(0,len(encoded)):
            xored_val = encoded[i] ^ arr[i]
            arr.append(xored_val)
        return arr
        print(arr)

encoded = [1,2,3]
first = 1
object = Solution()
object.decode(encoded,first)
        