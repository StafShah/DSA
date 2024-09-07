from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.d:
            self.d.move_to_end(key)
            return self.d[key] 
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key] = value
            self.d.move_to_end(key)

        else:
            if len(self.d) == self.cap:
                self.d.popitem(False)

            self.d[key] = value
            self.d.move_to_end(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)