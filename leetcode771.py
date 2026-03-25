class Solution:
    def numJewelsInStones(self, jewels, stones):
        count = 0
        # for stone in stones:
        #     for jewel in jewels:
        #         if jewel == stone:
        #             count += 1
        # return count
        for stone in stones:
            if stone in jewels:
                count += 1
        return count
    
object = Solution()
print(object.numJewelsInStones("aA","aAAbbb"))