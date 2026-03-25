class Solution:
    def minimumBoxes(self, apple, capacity) :

        boxes_used = 0
        total_apples = sum(apple)
        sorted_capacity = sorted(capacity,reverse = True)
        # print("Sorted capacity", sorted_capacity)

        for i in range(0,len(sorted_capacity)):
            total_apples -= sorted_capacity[i] 
            boxes_used += 1

            if total_apples <= 0:
                break
            
        print("Boxes Used", boxes_used)
        return boxes_used



object = Solution()
object.minimumBoxes(apple = [1,3,2], capacity = [4,3,1,5,2])