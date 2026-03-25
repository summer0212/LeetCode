class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        min_num = num_str
        max_num = num_str

        max_char = min(num_str)
        max_num = max_num.replace(max_char,'9')
        print("max_num",max_num)

        min_char = max(num_str)
        min_num = min_num.replace(min_char,'0')
        print("min_num",min_num)


        return int(max_num) - int(min_num)

        
object = Solution()
print(object.minMaxDifference(num= 11891))