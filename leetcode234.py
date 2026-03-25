from typing import Optional


class ListNode:
    def __init__(self, val= 0, next = None) :
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head:Optional[ListNode]):
        nums = []

        current = head

        while current is not None:
            nums.append(current.val)
            current = current.next

        return nums == nums[::-1]

#creating nodes manually
node1=ListNode(1)
node2=ListNode(2)
node3=ListNode(2)
node4=ListNode(1)

#2. Linking the nodes together
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None





object = Solution()
print(object.isPalindrome(head = node1))

        