class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l, r = 0, 0
        newArr = []

        m = len(nums1)
        n = len(nums2)

        while l < m and r < n:
            if nums1[l] >= nums2[r]:
                newArr.append(nums2[r])
                r += 1
            else:
                newArr.append(nums1[l])
                l += 1

        while l < m:
            newArr.append(nums1[l])
            l += 1
        while r < n:
            newArr.append(nums2[r])
            r += 1
        
        totalLength = m + n
        mid = totalLength // 2
        if totalLength % 2 == 0:
            return float((newArr[mid] + newArr[mid-1]) / 2)
        else:
            return newArr[mid]
            
        return 0