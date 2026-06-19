class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1Count = Counter(nums1)
        nums2Count = Counter(nums2)
        ans = [[] for i in range(2)]
        for num in nums2:
            if num not in nums1Count and num not in ans[1]:
                ans[1].append(num)

        for num in nums1:
            if num not in nums2Count and num not in ans[0]:
                ans[0].append(num)

        return ans