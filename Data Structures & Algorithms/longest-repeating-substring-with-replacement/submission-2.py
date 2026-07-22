class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left, right = 0, 0

        while right < len(s):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            popularIncidence = max(hashmap.values())
            length = right - left + 1
            if length - popularIncidence > k:
                hashmap[s[left]] -= 1
                left += 1
            right += 1
        return right - left