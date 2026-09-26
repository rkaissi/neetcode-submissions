class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [1, 2, 3, 4, 5, 6, 7, 8]
        [6, 7, 8, 1, 2, 3, 4, 5]

        [5,2,3,4,1,6,7,8]

        [1, 2, 3, 4, 5, 6, 7, 8], k = 3
        [6, 7, 8, 1, 2, 3, 4, 5]

        ]


        """
        n = len(nums)
        k %= n
        numMoved = 0
        for i in range(n-1, -1, -1):
            if numMoved == n:
                break
            cur = i
            temp = nums[cur]

            while True:
                nums[(cur + k) % n], temp = temp, nums[(cur + k) % n]
                numMoved += 1
                cur = (cur + k) % n

                if cur == i:
                    break
