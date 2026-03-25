class Solution:
    def mostWordsFound(self, sentences):
        count_of_words = 0
        list_of_words = []
        for sentence in sentences:
            print(f"Sentence: {sentence}")
            # Split the sentence into words
            # split() method splits a string by whitespace (spaces, tabs, newlines) by default
            # It returns a list of words
            list_of_words = sentence.split()
            print(f"Words in this sentence: {list_of_words}")
            # count_of_words = len(list_of_words)
            if len(list_of_words) > count_of_words:
                count_of_words = len(list_of_words)
            
            # Update the maximum word count if this sentence has more words
            # if len(list_of_words) > count_of_words:
            #     count_of_words = len(list_of_words)
        
        return count_of_words


object = Solution()
print(object.mostWordsFound(["w jrpihe zsyqn l dxchifbxlasaehj","nmmfrwyl jscqyxk a xfibiooix xolyqfdspkliyejsnksfewbjom","xnleojowaxwpyogyrayfgyuzhgtdzrsyococuqexggigtberizdzlyrdsfvryiynhg","krpwiazoulcixkkeyogizvicdkbrsiiuhizhkxdpssynfzuigvcbovm","rgmz rgztiup wqnvbucfqcyjivvoeedyxvjsmtqwpqpxmzdupfyfeewxegrlbjtsjkusyektigr","o lgsbechr lqcgfiat pkqdutzrq iveyv iqzgvyddyoqqmqerbmkxlbtmdtkinlk","hrvh efqvjilibdqxjlpmanmogiossjyxepotezo","qstd zui nbbohtuk","qsdrerdzjvhxjqchvuewevyzlkyydpeeblpc"]))
        