class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Sorting
        # nums.sort()
        # return nums[-k]
        # ------------------------
        
        # Min heap
        # heapq.heapify(nums)

        # while len(nums) > k:
        #     heapq.heappop(nums)
        
        # return nums[0]
        # ------------------------

        # Max heap
        # maxHeap = [-n for n in nums]
        # heapq.heapify(maxHeap)

        # res = None
        # while k > 0:
        #     res = -heapq.heappop(maxHeap)
        #     k -= 1
        # return res
        # ------------------------

        # Quick select
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            nums[p], nums[r] = nums[r], nums[p]
            if k < p:
                return quickSelect(l, p - 1)
            elif k > p:
                return quickSelect(p + 1, r)
            else:
                return nums[p]
        
        return quickSelect(0, len(nums) - 1)