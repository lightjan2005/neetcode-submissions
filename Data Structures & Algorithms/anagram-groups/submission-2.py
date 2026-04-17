class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = []
        ansSet = set()

        for i, s in enumerate(strs):
            newString = "".join(sorted(s))
            if newString not in ansSet:
                ansSet.add(newString)
                ans.append([s])
            else:
                for arr in ans:
                    if "".join(sorted(arr[0])) == newString:
                        arr.append(s)


        return ans
