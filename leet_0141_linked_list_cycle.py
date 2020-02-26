class Solution:
    def hasCycle(self, head) -> bool:
        hare = tortoise = head
        while tortoise is not None and tortoise.next is not None:
            hare, tortoise = hare.next, tortoise.next.next
            if tortoise == hare:
                return True
        return False