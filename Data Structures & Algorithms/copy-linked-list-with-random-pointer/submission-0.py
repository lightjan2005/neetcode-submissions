class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        listMap = {}

        cur = head
        # loop through the current linked list
        while cur:
            if cur not in listMap:
                listMap[cur] = Node(cur.val)
            cur = cur.next

        curNode = head
        while curNode:
            copy = listMap[curNode]
            copy.next = listMap.get(curNode.next)
            copy.random = listMap.get(curNode.random)
            curNode = curNode.next
        
        return listMap[head]