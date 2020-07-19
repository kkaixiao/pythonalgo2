"""
Given an array A of non-negative integers, return an array consisting of all the even elements
of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.



Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
"""


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even, odd = [], []

        for num in A:
            odd.append(num) if num % 2 else even.append(num)

        even.extend(odd)

        return even

    # binary search approach, looks cool, but not so fast
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        left, right = 0, len(A) - 1

        while left < right:

            while A[left] % 2 == 0 and left < right:
                left += 1

            while A[right] % 2 == 1 and left < right:
                right -= 1

            A[left], A[right] = A[right], A[left]

        return A

    # the third method without combining lists in the end
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        j = 0
        for i in range(len(A)):
            if A[i]%2==0:
                A[i], A[j] = A[j], A[i]
                j+=1
        return A