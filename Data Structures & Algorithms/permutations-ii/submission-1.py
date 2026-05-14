class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        count = Counter(nums)

        def dfs(i, arr):
            if i == len(nums):
                res.add(tuple(arr.copy()))
                return

            for j in range(len(nums)):
                if count[nums[j]] > 0:
                    count[nums[j]] -= 1
                    arr.append(nums[j])
                    dfs(i+1, arr)
                    count[nums[j]] += 1
                    arr.pop()
        
        dfs(0,[])
        return list(res)