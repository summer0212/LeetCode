# a = [0,1]
# list1 = [9,4,6]

# for i in range(0,len(list1)):
#     a.append(list1[i])

# print(a)

class Solution:
    def largestAltitude(self, gain) :
        altitude = [0, gain[0]]
        j = 1
        for i in range(1,len(gain)):
            
            # print("altitude[j] = " , altitude[j], "gain[i] = " , gain[i])
            altitude.append(altitude[j] + gain[i])
            j += 1

        return max(altitude)

object = Solution()
print(object.largestAltitude(gain = [-4,-3,-2,-1,4,3,2]))

'''Alternate method:
        n = len(gain)
        prefix_sum = [0] * (n+1)
        
        for i in range(0,len(gain)):
            prefix_sum[i+1] = prefix_sum[i] + gain[i]
            
        return max(prefix_sum)'''