class Solution:
    def reverseWords(self, s):
        result = []
        # result_str = ""

        #Changing the str to list

        s_list = s.split()
        print(s_list)

        for i in range(0,len(s_list)):
            reversed_string = s_list[i][::-1]
            result.append(reversed_string)

        result_str = " ".join(result)
        print(result_str)



object = Solution()
object.reverseWords(s = "Let's take LeetCode contest")