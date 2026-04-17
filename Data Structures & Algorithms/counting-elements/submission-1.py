class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        numDict = Counter(arr)
        ans = 0

        for i in range(len(arr)):
            if (arr[i] + 1) in numDict:
                ans += 1

        return ans