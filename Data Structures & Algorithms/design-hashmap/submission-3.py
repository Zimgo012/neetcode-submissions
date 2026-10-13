class MyHashMap:

    def __init__(self):
        self.arrK = []
        self.arrV = []

    def put(self, key: int, value: int) -> None:
        
        if key in self.arrK:
            i = self.arrK.index(key)
            self.arrV[i] = value
            return
        self.arrK.append(key)
        self.arrV.append(value)


    def get(self, key: int) -> int:

        if key in self.arrK:
            i = self.arrK.index(key)
            return self.arrV[i]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        if key in self.arrK:
            i = self.arrK.index(key)
            self.arrV.pop(i)
            self.arrK.pop(i)



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)