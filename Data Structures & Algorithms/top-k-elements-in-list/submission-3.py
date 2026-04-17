class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numCount = Counter(nums)
        ans = []
        countArr = [[] for i in range(len(nums)+1)]

        for num,occurances in numCount.items():
            countArr[occurances].append(num)

        for i in range(len(countArr)-1,-1,-1):
            for n in countArr[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans

        return ans