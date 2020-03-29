"""
You are playing the following Nim Game with your friend: There is a heap of stones on the table,
each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will
be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine
whether you can win the game given the number of stones in the heap.

Example:

Input: 4
Output: false
Explanation: If there are 4 stones in the heap, then you will never win the game;
             No matter 1, 2, or 3 stones you remove, the last stone will always be
             removed by your friend.
"""

"""
    if(n <= 0) return false;
    if(n == 1 || n == 2 || n== 3) return true;
    if(canWinNim(n-1) && canWinNim(n-2) && canWinNim(n-3)) return false;
    return true;
"""

class Solution:
    def canWinNim(self, n):
        return n%4


    def canWinNim2_OverTime(self, n: int) -> bool:
        if n <= 0:
            return False
        if n >= 1 and n <= 3:
            return True
        if self.canWinNim(n-1) and self.canWinNim(n-2) and self.canWinNim(n-3):
            return False
        return True