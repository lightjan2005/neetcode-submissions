class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums2Dict = defaultdict(list)
        print(nums2Dict)
        res = []
        for i in range(len(nums2)):
            nums2Dict[nums2[i]].append(i)

        for i in range(len(nums1)):
            res.append(nums2Dict[nums1[i]][0])
            nums2Dict[nums1[i]].pop()
        
        return res