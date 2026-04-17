class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        curMax = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2,-1,-1):
            if arr[i] > curMax:
                tmp = curMax
                curMax = arr[i]
                arr[i] = tmp
            else:
                arr[i] = curMax
        
        return arr