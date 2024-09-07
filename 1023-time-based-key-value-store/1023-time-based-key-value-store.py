from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.hMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hMap:
            self.hMap[key] = SortedDict()
        self.hMap[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hMap:
            return ""
        
        time_dict = self.hMap[key]
        idx = time_dict.bisect_right(timestamp) - 1
        
        if idx == -1:
            return ""
        
        return time_dict.values()[idx]
