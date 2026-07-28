class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        exception_dict  = {
            "IV" : 4,
            "IX" :9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900
        }

        if s in exception_dict:
            return exception_dict[s]

        s_list = list(s)
        actual_numeric_val = 0

        for i in range(0,len(s_list)):
            if i < len(s_list) - 1 and roman_dict[s_list[i]] < roman_dict[s_list[i + 1]] :
                actual_numeric_val -= roman_dict[s_list[i]]
            else:
                actual_numeric_val += roman_dict[s_list[i]]
        return actual_numeric_val

object = Solution()
print(object.romanToInt("MCMXCIV"))
