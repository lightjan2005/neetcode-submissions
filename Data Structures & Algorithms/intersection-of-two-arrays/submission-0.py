class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        num1Count = Counter(nums1)
        
        for num in nums2:
            if num in num1Count:
                res.add(num)

        return list(res)