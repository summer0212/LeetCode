class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dict = {}
        alphabets = "abcdefghijklmnopqrstuvwxyz"

        alphabet_pointer = 0

        for char in key:
            if char != " " and char not in dict:
                
                dict[char] = alphabets[alphabet_pointer]
                alphabet_pointer += 1

        decoded_result = []

        for char in message:
            if char ==" ":
                decoded_result.append(" ")
            else:
                decoded_result.append(dict[char])

        return "".join(decoded_result)
    

object = Solution()
print(object.decodeMessage(key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))