class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # alphabet = set('abcdefghijklmnopqrstuvwxyz')
        # sentence_set = set(sentence)

        # return alphabet.issubset(sentence_set)

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for char in alphabet:
            if char in sentence:
                continue
            else:
                return False
        return True
    
object = Solution()
print(object.checkIfPangram(sentence = "cspduleznlxgqqhohsvvxdoloranhqvirefamevwuxjjnjwmwzodsbxocxbojrphonvwkdnpaibajcgntvaiuwfhwcgbjvlwhvmszivogcxvzxwjjjgeekplruvlcftudtceaqddufknmojbwgwisvgowqfppmaqhkhrbqomijhjitgxkpragvgsjxnomnx"))   