class Solution:
    def findThePrefixCommonArray(self, A, B) :
        n = len(A)
        frequency = [0] * (n+1)
        common_counter = 0
        result = []

        for i in range(0,n):
            num_a = A[i]
            frequency[num_a] += 1

            if frequency[num_a] == 2:
                common_counter += 1

            num_b = B[i]
            frequency[num_b] += 1

            if frequency[num_b] == 2:
                common_counter += 1

            result.append(common_counter)
        
        return result
    
object = Solution()
print(object.findThePrefixCommonArray(A = [1,3,2,4], B = [3,1,2,4]))

        