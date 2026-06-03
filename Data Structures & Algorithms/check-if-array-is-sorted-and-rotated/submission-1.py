class Solution:
    def check(self, nums: List[int]) -> bool:
        flag = 0

        # find first number
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                if flag == 0:
                    flag = 1
                else:
                    return False
                
        return False if nums[-1] > nums[0] and flag == 1 else True