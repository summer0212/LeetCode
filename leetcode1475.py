class Solution:
    def finalPrices(self, prices):
        result = []

        for i in range(0,len(prices)):
            if prices[i] > prices[i+1]:
                result.append(prices[i+1] - prices[i])

            elif prices[i] < prices[i+1] and prices[i+1] <= prices[i]:
                result.append(prices[i])
            
            else :
                min_price = min(prices)
                result.append(prices[i] - min_price)
        
        print(result)

        # def finalPrices(self, prices: List[int]) -> List[int]:
        # n = len(prices)
        # for i in range(n):
        #     price = prices[i]
        #     for j in range( i + 1, n):
        #         if prices[j] <= price:
        #             price = price - prices[j]
        #             break
        #     prices[i] = price
        # return prices

object = Solution()
object.finalPrices(prices = [1,2,3,4,5])
        