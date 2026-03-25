class Solution:
    def maximumWealth(self, accounts):
        customer_wealth = []
        sum = 0
        max_wealth = 0
        for i in range(len(accounts)):
            sum = 0
            for j in range(len(accounts[i])):
                sum += accounts[i][j]
            customer_wealth.append(sum)
        print(customer_wealth,"Customer-wealth total for all")
        
        for k in range(len(customer_wealth)):
            if max_wealth < customer_wealth[k]:
                max_wealth = customer_wealth[k]
        print(max_wealth)
        return max_wealth
    
object = Solution()
object.maximumWealth([[1,5],[7,3],[3,5]])