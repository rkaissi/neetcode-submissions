class TimeMap:

    def __init__(self):
        self.keymap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keymap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        keys = self.keymap[key]
        if not keys:
            return ""

        res = ""
        l, r = 0, len(keys) - 1
        while l <= r:
            m = (l + r) // 2
            time = keys[m][0]
            if time <= timestamp:
                res = keys[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return res
