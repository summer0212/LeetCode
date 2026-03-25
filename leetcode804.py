# # from morse_code import MorseCode
# from morse_code import encrypt


# # morse = MorseCode()

# class Solution:
#     def uniqueMorseRepresentations(self, words):
#         empty_dict = {}
#         empty_str = ""
#         empty_list = []
#         output = 0

#         for i in range(0,len(words)):
#             # word_morse = ""
#             for j in words[i]:
#                 # Convert each character to morse code
#                 char_morse = encrypt(j)
#                 empty_str += char_morse
#             empty_dict[words[i]] = empty_str
#             empty_str = ""
#             # print(empty_dict) #{'gin': '..-. .... -- ', 'zen': '-.-- -.. -- ', 'gig': '..-. .... ..-. ', 'msg': '.-.. .-. ..-. '}
        
#         unique_morse = set(empty_dict[words[i]])
#         print("unique_morse", unique_morse)

#         output = len(unique_morse)
#         return output
            
            
            
            
            
            
            
            
            
            
#             #     if char_morse:
#             #         word_morse += char_morse.strip() + " "  # Add space between characters
#             # print(f"Word '{words[i]}' -> Morse: '{word_morse.strip()}'")
#             # empty_list.append(word_morse.strip())  # Store the complete morse word

        


# object = Solution()
# print(object.uniqueMorseRepresentations(words = ["gin","zen","gig","msg"]))

#------------------------------------------------------------------------------------
                #New method without morse-code library

class Solution:
    def uniqueMorseRepresentations(self, words):
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        empty_str = ""
        empty_list = []
        

        for i in range(0,len(words)):
            empty_str = ""  # Reset empty_str for each new word
            for j in words[i]:
                print("printing j", j)
                empty_str += morse_code[ord(j) - 97]
            empty_list.append(empty_str)
        print("final list", empty_list)

        output = set(empty_list)
        print("set used in output", output)
        return len(output)

object = Solution()
print(object.uniqueMorseRepresentations(words = ["gin","gig"]))
        



     