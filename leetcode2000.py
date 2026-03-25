class Solution:
    def reversePrefix(self, word, ch) :

        str = ""
        new_str = ""
        rev_str = ""
        if ch in word:
            stop_index = word.index(ch)

            str = word[: stop_index + 1]


            # for i in word:
            #     str += i
            #     if i == ch:
            #         break
            rev_str = str[::-1]
            new_str = word.replace(str,rev_str)
            print(new_str)
        else:
            print(word)
            return word

object = Solution()
object.reversePrefix("tttttt", "d")
