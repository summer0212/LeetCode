class Solution:
    def convertDateToBinary(self, date) :
        date_list = date.split('-')
        binary_date = []
        for i in date_list:
           i = int(i)
           binary_date.append(bin(i)[2:])
        # print(binary_date)
        result = '-'.join(binary_date)
        return str(result)

            




object = Solution()
print(object.convertDateToBinary("2025-02-06"))