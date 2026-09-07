class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        self.visited = {}
        def dfs(i):
            if i == len(nums) or i in self.visited:
                return
            
            self.visited[i] = True

            for j in range(len(nums)):
                if i == j:
                    continue
                if gcd(nums[i], nums[j]) <= 1:
                    continue
                dfs(j)
        

        dfs(0)
        return len(self.visited) == len(nums)