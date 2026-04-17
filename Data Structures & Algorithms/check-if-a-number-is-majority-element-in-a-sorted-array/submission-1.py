class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        
        def lowerBound(nums: List[int], target: int)-> int:

            start = 0
            end = len(nums)-1
            index = len(nums)

            while start <= end:
                mid = (start + end)//2
                if nums[mid] >= target:
                    end = mid - 1
                    index = mid
                else:
                    start = mid + 1
            
            return index

        def upperBound(nums: List[int], target: int)->int:
            start = 0
            end = len(nums)-1
            index = len(nums)

            while start <= end:
                mid = (start + end)//2
                if nums[mid] > target:
                    end = mid - 1
                    index = mid
                else:
                    start = mid + 1
            return index

        firstIndex = lowerBound(nums, target)
        lastIndex = upperBound(nums, target)
        return lastIndex - firstIndex > len(nums)//2