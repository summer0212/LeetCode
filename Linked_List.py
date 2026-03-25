
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

#Connecting the nodes with arrows
node1.next = node2 #node1 points to the node2
node2.next = node3 
node3.next = None ## node3 points to nothing (End of list)

#Defining the Head 
head = node1 # The head is just a label for the starting point

def print_linked_list(head):
    result = "head" #Just in case no nodes are there we get the value of head
    # Initialize the "Walker" pointer at the start
    current = head

     # THE LOOP: Keep going as long as 'current' is not None
    while current is not None:
        #1. Access the data: Add the arrow and the value to our string
        result = result + "->" + str(current.val)

        #2. MOST IMPORTANT Line:- Move the pointer forward
        #This is like saying i = i + 1 in a normal step
        print("Just checking here",str(current.next))
        current = current.next

    #While the loop breaks, it means current is None(end of list)
    result = result + "-> None"
    print(result)

print_linked_list(head)




