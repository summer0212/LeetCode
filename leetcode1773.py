class Solution:
    def countMatches(self, items, ruleKey, ruleValue) :
        count = 0
        for i in range(0,len(items)):
            if ruleKey == "type":

                if ruleValue in items[i][0]:
                    count += 1
            elif ruleKey == "color":
                if ruleValue in items[i][1]:
                    count += 1
            elif ruleKey == "name":
                if ruleValue in items[i][2]:
                    count += 1

        return count

object = Solution()
print(object.countMatches(items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"))
        