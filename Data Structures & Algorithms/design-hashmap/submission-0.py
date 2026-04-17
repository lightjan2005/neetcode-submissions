class MyHashMap:

    def __init__(self):
        self.key = []
        self.value = []

    def put(self, key: int, value: int) -> None:
        if key in self.key:
            for i in range(len(self.key)):
                if self.key[i] == key:
                    self.value[i] = value
        else:
            self.key.append(key)
            self.value.append(value)

    def get(self, key: int) -> int:
        for i in range(len(self.key)):
            if self.key[i] == key:
                return self.value[i]
        return -1

    def remove(self, key: int) -> None:
        if key in self.key:
            index = self.key.index(key)
            self.value.remove(self.value[index])
            self.key.remove(self.key[index])


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)