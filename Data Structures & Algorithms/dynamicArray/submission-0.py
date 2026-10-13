
class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    #int get(int i) will return the element at index i. Assume that index i is valid.
    def get(self, i: int) -> int:
        return self.array[i]

    # void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    # # void pushback(int n) will push the element n to the end of the array.
    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.array[self.size] = n
        self.size += 1


    # int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
    def popback(self) -> int:
        numpop = self.array[self.size -1]
        self.array[self.size - 1] = None
        self.size -=1
        return numpop

    # void resize() will double the capacity of the array.
    def resize(self) -> None:
        newCapacity = (self.capacity * 2)
        newarray = [None] * newCapacity

        for i in (range(self.size)):
            newarray[i] = self.array[i]

        self.array = newarray
        self.capacity = newCapacity

    # int getSize() will return the number of elements in the array.
    def getSize(self) -> int:
        return self.size

    # int getCapacity() will return the capacity of the array.
    def getCapacity(self) -> int:
        return self.capacity

