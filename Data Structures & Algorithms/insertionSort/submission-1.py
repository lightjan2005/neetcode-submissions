# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs) == 0:
            return []
        res = []
        insertArr = pairs[:]
        res.append(pairs[:])

        for i in range(1,len(pairs)):
            cur = insertArr[i]
            j = i - 1
            while j >= 0 and insertArr[j].key > cur.key:
                insertArr[j + 1] = insertArr[j]
                j -= 1
            insertArr[j + 1] = cur
            res.append(insertArr[:])

        return res