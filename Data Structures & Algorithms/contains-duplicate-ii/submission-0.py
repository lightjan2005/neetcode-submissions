class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen = set()
        for i in range(k):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])
        
        l = 0
        for i in range(k, len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])
                seen.remove(nums[l])
                l += 1

        return False