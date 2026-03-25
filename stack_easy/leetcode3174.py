class Solution:
    def clearDigits(self, s: str) -> str:
        s_list = list(s)
        
        i = 0
        while i < len(s_list):
            if s_list[i].isdigit() and i > 0 and s_list[i-1].isalpha():
                s_list.pop(i)
                s_list.pop(i-1)
                i = max(0, i-1)
            else:
                i += 1
        
        # Converting string to list
        new_str = "".join(s_list)
        print(new_str)
        return new_str


object = Solution()
object.clearDigits(s = "abc")


#----------------Error done at start----------------
#Using for loop will not help as the value of i cannot be controlled so using while-loop
# for i in range(0, len(s_list)):
        #     print("Value of i :", i)
        #     print(len(s_list), "length printing")
        #     if s_list[i].isdigit() == True :
        #         if  s_list[i - 1].isalpha() == True:
        #             s_list.pop(i)
        #             s_list.pop(i-1)
        #             # print(s_list)
        #             i = 0
        #         print("In here")
        #     # print(s)
        #     else :
        #         continue

        # print(s_list)