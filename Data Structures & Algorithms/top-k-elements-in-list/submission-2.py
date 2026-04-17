class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}
        ans = []
        countArr = [[]for i in range(len(nums)+1)]

        for num in nums:
            # count the number of occurances per number in list
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        

        # loop through the nums array again and populate the countArr
        for num, occurances in dic.items():
            countArr[occurances].append(num)
        
        
        for i in range(len(countArr)-1,0,-1):
            for n in countArr[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans

        return ans
        