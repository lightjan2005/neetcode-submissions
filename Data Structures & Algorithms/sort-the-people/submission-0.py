class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        people = []
        ans = []
        for i in range(len(names)):
            people.append([heights[i],names[i]])

        people.sort(reverse=True)
        for p in people:
            ans.append(p[1])
        
        return ans