class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min heap
        # heapq.heapify(nums)

        # while len(nums) > k:
        #     heapq.heappop(nums)
        
        # return nums[0]

        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)

        res = None
        while k > 0:
            res = -heapq.heappop(maxHeap)
            k -= 1
        return res