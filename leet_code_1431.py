def kidsWithCandies(candies, extraCandies: int) :
        result = []
        duplicate_candies = list(candies)
        print(duplicate_candies)
        for i in range(len(duplicate_candies)):
            duplicate_candies[i] += extraCandies
            if duplicate_candies[i] >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result


candies = [12,1,12]
extraCandies = 10
output = kidsWithCandies(candies , extraCandies)
print(output)