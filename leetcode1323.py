class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)
        # output = []

        # for char in str_num:
        #     if char == '6':
        #         temp = str_num.replace(char,'9',1)
        #         print(temp)
        #         output.append(int(temp))

        #     elif char == '9':
        #         temp = str_num.replace(char,'6',1)
        #         print(temp)

        #         output.append(int((temp)))
        output = str_num.replace('6',"9",1)

        return int(output)
    

object = Solution()
print(object.maximum69Number(num = 9999))

'''Notes:- Using replace() , will replace ALL occurrences of 6 with 9.f the input is 66, your code would output 99. While 99 is bigger, the question says you can change at most ONE digit. So for 66, the answer should be 96 (changing only the first one).Syntax+ string.replace(oldvalue, newvalue, count). IN SIMPLE TERMS, CHANGE THE FIRST 6 YOU GET....
Step-by-Step Algorithm
    Convert to String: We cannot iterate through an integer easily. Convert num to a string or a list of characters.
    Iterate (Left to Right): Loop through the digits.
    Check Condition: Is the current digit a '6'?
    Action:
    If yes, change only that digit to '9'.
    BREAK the loop immediately (we only get one change).
    Return: Convert the modified string/list back to an integer.
    
    Alternate logic:
    class Solution:
    def maximum69Number (self, num):
        list_num = list(str(num))
        
        for element in range(0,len(list_num)):
            if list_num[element] == "6":
                print("True")
                list_num[element] = "9"
                break
        str_result = "".join(list_num)
            
        return int(str_result)
        
        
object=Solution()
print(object.maximum69Number(num = 9999))'''