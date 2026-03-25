class Solution:
    def rangeSumBST(self, root, low, high) :
        result = 0
        print(root)
        for i in range(len(root)):
            if root[i] >= low and root[i] <= high:
                result = result + root[i]
        return result
    
obj = Solution()
print(obj.rangeSumBST([10,5,15,3,7,18],7,15))