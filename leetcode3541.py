class Solution:
    def maxFreqSum(self, s):
        vowel_dict = {}
        consonant_dict = {}
        for char in s:
            if char.lower() in 'aeiou':
                if char.lower() in vowel_dict:
                    vowel_dict[char.lower()] += 1
                else:
                    vowel_dict[char.lower()] = 1
            else:
                if char.lower() in consonant_dict:
                    consonant_dict[char.lower()] += 1
                else:
                    consonant_dict[char.lower()] = 1

        if vowel_dict == {}:
            max_vowel = 0
        else:
            max_vowel = max(vowel_dict.values())
        if consonant_dict == {}:
            max_consonants = 0
        else:
            max_consonants = max(consonant_dict.values())
        return max_vowel + max_consonants


object = Solution()
print(object.maxFreqSum("aeiaeia"))


            