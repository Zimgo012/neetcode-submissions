class MyHashSet:

    def __init__(self):
        self.arr = []

    def add(self, key: int) -> None:
        inArray = False

        for n in self.arr:
            if key == n :
                inArray = True
        if not inArray:
            self.arr.append(key)


    def remove(self, key: int) -> None:
        for n in self.arr:
            if n == key:
                self.arr.remove(n)

    def contains(self, key: int) -> bool:

        for n in self.arr:
            if n == key:
                return True
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)