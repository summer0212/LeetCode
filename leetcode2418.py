class Solution:
    def sortPeople(self, names, heights) :
        # mp = dict(zip(names,heights))
        # print(mp)
        mp = {}
        for i in range(len(names)):
            mp[heights[i]] = names[i]
        print(mp)

        sorted_mp = sorted(mp.keys(), reverse=True)
        print(sorted_mp)

        result = []
        for height in sorted_mp:
            result.append(mp[height])
        print(result)
        return result


object =  Solution()
object.sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170])
        