class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.size = 0
        self.arr = [0]*capacity 

    def get(self, i: int) -> int:
        if i <= self.size:
            return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.capacity == 0:
            raise IndexError("Array is Empty")
 
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [0]*self.capacity
        k = 0
        for i in self.arr:
            new_arr[k] = i
            k += 1
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return (self.capacity)
