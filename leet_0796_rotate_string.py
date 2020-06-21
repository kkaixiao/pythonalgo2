


class Solution:

    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        A += A
        if A.find(B)>=0:
            return True
        else:
            return False


    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A + A


    def rotateString(self, A: str, B: str) -> bool:

        if not len(A) and not len(B):
            return True
        elif not len(A) or not len(B):
            return False
        if len(B) < len(A):
            return False


        A = A * 2
        if B in A:
            return True
        else:
            return False