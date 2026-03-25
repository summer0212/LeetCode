class Solution:
    def minimumSum(self, num: int) -> int:
        str_num = str(num)
        print("Using split()",str_num.split(","))
        list_of_num = list(str_num)
        digits_of_num = sorted(list_of_num)
        print(digits_of_num)

        new1 = digits_of_num[0] + digits_of_num[2]
        new2 = digits_of_num[1] + digits_of_num[3]

        print(new1,new2)
        return int(new1) + int(new2)

''' Alternate logic:
        str_num = str(num)
        num_list = list(str_num)
        
        sorted_num_list = sorted(num_list)
        
        new1_list = "".join([sorted_num_list[1], sorted_num_list[2]])
        new2_list = "".join([sorted_num_list[0], sorted_num_list[3]])
        
        new1 = int(new1_list)
        new2 = int(new2_list)
        
        # print(new1,new2 )
        
        return abs(new1+new2)'''

object = Solution()
print(object.minimumSum( num = 4009))
        