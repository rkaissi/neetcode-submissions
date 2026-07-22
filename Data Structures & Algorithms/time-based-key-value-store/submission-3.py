class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key] = self.hashmap.get(key, []) + [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        li = self.hashmap.get(key, [(0, "")])
        res = ""

        l, r = 0, len(li) - 1

        while l <= r:
            m = (l + r) // 2

            if li[m][0] <= timestamp:
                res = li[m][1]
                l = m + 1
            else:
                r = m - 1
        return res