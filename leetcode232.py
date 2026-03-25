'''This is a classic interview question because it tests your understanding of data structures. We are effectively trying to make a "Line" (Queue) behave like a "Line" using only two "Piles" (Stacks).
The Concept - The Solution: Two Stacks
Imagine two cups, Input Cup (s1) and Output Cup (s2).
1. Pushing: Always put new items into the Input Cup (s1).
s1 = [1, 2, 3] (3 is at the top).
2. Popping: We need to get 1 out. But 1 is at the bottom of s1.
Action: Pour everything from Input Cup into Output Cup.
When you pour, the order reverses!
s1 becomes empty.
s2 becomes [3, 2, 1] (Now 1 is at the top!).
3. The Trick: As long as s2 has items, we can just pop from it freely. We only pour from s1 to s2 when s2 runs out of items.'''

#Stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop() # Python's list.pop() removes the last item
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1] # Look at the last item without removing
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# --------Implementing Queue using 2 Stacks-----------
class MyQueue():
    def __init__(self) :
        self.s1 = Stack() #Input Stack
        self.s2 = Stack() #Output Stack

    def push(self,x:int):
        #Alwaays pushing new data into s1
        self.s1.push(x)
    
    def pop(self):
        # We need to remove from the "front"
        # If s2 is not empty, the "front" is at the top of s2.
        # If s2 IS empty, we must move everything from s1 to s2.
        if self.s2.is_empty():
            while not self.s1.is_empty():
                val = self.s1.pop()
                self.s2.push(val)
        return self.s2.pop()

    def peek(self):
        if self.s2.is_empty():
            while not self.s1.is_empty():
                val = self.s1.pop()
                self.s2.push(val)

        return self.s2.peek()

    def empty(self):
        # It is empty only if BOTH stacks are empty
        return self.s1.is_empty() and self.s2.is_empty()

#----------Step 3: Testing the Code-----------
if __name__ == "__main__":
    obj = MyQueue()

    print("Action: Push 1")
    obj.push(1)
    
    print("Action: Push 2")
    obj.push(2)
    
    print("Action: Peek")
    param_3 = obj.peek()
    print(f"Peek Result: {param_3}") # Should be 1 (First In)
    
    print("Action: Pop")
    param_2 = obj.pop()
    print(f"Pop Result: {param_2}")  # Should be 1
    
    print("Action: Empty?")
    param_4 = obj.empty()
    print(f"Is Empty: {param_4}")    # Should be False (2 is still there)
    
    print("Action: Pop")
    print(f"Pop Result: {obj.pop()}") # Should be 2
    
    print("Action: Empty?")
    print(f"Is Empty: {obj.empty()}") # Should be True



    

    '''Leetcode solution using List as Stack
    class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)
        

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        
        return self.s2.pop()
        

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()'''

    

    