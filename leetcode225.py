'''mplement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

The Rules (Queue Translation):
| Queue Operation | Python deque Equivalent |
| :--- | :--- |
| push(x) (Back) | q.append(x) |
| pop() (Front) | q.popleft() (Crucial: We pop from the left/start) |
| peek() (Front) | q[0] (Look at index 0) |
| empty() | not q |
'''

from collections import deque

class MyStack:
    def __init__(self) -> None:
        # We use two queues
        self.q1 = deque()
        self.q2 = deque()

    def push(self,x:int):
        # 1. Put new element in the empty q2 -> kyuki jo naya aaya hai wo sbse saamne hona chahiye
        self.q2.append(x) #you can use the .append() method for a Python collections.deque object. The method adds a single element to the right end (or tail) of the deque in an efficient, thread-safe manner with O(1) time complexity. 

        #2.Move all the elements from q1 to q2,everything added behind the new elements 
        while self.q1:
            val = self.q1.popleft()## Remove from front of q1
            self.q2.append(val)# Add to back of q2

        #3. Swap the names of q1 to q2 because from now on all the new numbers will be added here and the pop, psh,etc. will be done on this q2 queue only
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        # Since we did the hard work in push, the element is ready at the front
        return self.q1.popleft()

    def top(self):
        #Look at the front element
        return self.q1[0]

    def empty(self):
        return not self.q1

#-------TESTING----------
if __name__ == "__main__":

    obj = MyStack()

    print("Pushing 1")
    obj.push(1) # Queue is [1]
    
    print("Pushing 2")
    obj.push(2) # Queue becomes [2, 1]
    
    print(f"Top: {obj.top()}") # Should be 2
    
    print(f"Pop: {obj.pop()}") # Should be 2. Queue becomes [1]
    
    print(f"Empty?: {obj.empty()}") # False





        

