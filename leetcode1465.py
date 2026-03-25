class Solution:
    def maxArea(self, h, w, horizontalCuts, verticalCuts) :
        MOD = 10 ** 9 + 7

        all_h_cuts = [0] + horizontalCuts + [h]
        all_v_cuts = [0] + verticalCuts + [w]

        all_h_cuts.sort()
        all_v_cuts.sort()

        max_h_diff = 0

        max_w_diff = 0

        h_diff = []
        for i in range(0,len(all_h_cuts)-1):
            j = i+1
            h_diff.append(all_h_cuts[j] - all_h_cuts[i])

        max_h_diff = max(h_diff)

        v_diff = []
        for i in range(0,len(all_v_cuts)-1):
            j = i+1
            v_diff.append(all_v_cuts[j] - all_v_cuts[i])

        max_w_diff = max(v_diff)

        result = (max_h_diff * max_w_diff) % MOD

        return result


        

        # print(all_h_cuts, all_v_cuts)

object = Solution()
print(object.maxArea(h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]))
        