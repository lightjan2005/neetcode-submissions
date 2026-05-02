import heapq
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        studentDictionary = defaultdict(list)
        ans = []
        for item in items:
            student, score = item
            studentDictionary[student].append(-score)

        for key in studentDictionary:
            heapq.heapify(studentDictionary[key])

        for key in studentDictionary.keys():
            i = 0
            total = 0
            while i < 5:
                total += -heapq.heappop(studentDictionary[key])
                i += 1
            average = total//5
            ans.append([key,average])

        return sorted(ans)