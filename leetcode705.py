class MyHashSet:

    def __init__(self):
        self.result = []
        

    def add(self, key: int) -> None:
        if key not in self.result:
            self.result.append(key)

        

    def remove(self, key: int) -> None:
        if key in self.result:
            self.result.remove(key)
        

    def contains(self, key: int) -> bool:
        if key in self.result:
            return True
        return False
    
    def show(self):
        print(self.result)
        


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.add(2)
obj.add(53)
obj.add(9)

obj.remove(9)
# print(param_3 = obj.contains(53))
print(obj.contains(53))
obj.show()