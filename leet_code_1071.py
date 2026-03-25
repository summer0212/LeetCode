str1 = "ABABAB"
str2 = "ABAB"


def gcdOfStrings(str1: str, str2: str) -> str:
        result = []
        j = 0
        for i in range(len(str1)):
            if j < len(str2) and str1[i] == str2[j]:
                result.append(str1[i])
            j += 1
        return "".join(result)

output = gcdOfStrings(str1, str2)
print(output)