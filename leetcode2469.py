class Solution:
    def convertTemperature(self, celsius) :
        ans = []
        # ans = list(range(2))
        kelvin = round(celsius + 273.15 , 5)
        fah = round(celsius * 1.80 + 32.00 , 5)
        ans = [kelvin , fah]
        print(ans)
        return ans

obj = Solution()
obj.convertTemperature(56.34)