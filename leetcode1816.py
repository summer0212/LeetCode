

class Solution:
    def truncateSentence(self, s, k) :
        s_list = s.split()
        result = []
        # for i in range(k):
        #     result.append(s_list[i])
        # str_result = str(result)
        # print(str_result)

        result = s_list[0:k]
        final_sentence = " ".join(result)
        return final_sentence

object = Solution()
print(object.truncateSentence(s = "Hello how are you Contestant", k = 4))
        