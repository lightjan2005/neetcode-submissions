class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        dif = (arr[-1]-arr[0])//len(arr)
        
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] != dif:
                return arr[i] - dif
            

        return arr[0]