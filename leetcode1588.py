class Solution:
    def sumOddLengthSubarrays(self, arr) :
        n = len(arr)

        sum_of_arr = 0

        for i in range(0,n):
            sum_of_arr += arr[i]

        for i in range(0,n,2):
            pass


        