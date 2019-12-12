"""
Given a list, right rotate the list by n position.

Examples :

Input : n = 2 
         List_1 = [1, 2, 3, 4, 5, 6]
Output : List_1 = [5, 6, 1, 2, 3, 4]
We get output list after right rotating 
(clockwise) given list by 2.

Input :  n = 3
         List_1 = [3, 0, 1, 4, 2, 3]
Output : List_1 = [4, 2, 3, 3, 0, 1]
"""


def array_cyclic_rotation_solution1(l, n):
    for i in range(n):
        l.insert(0, l.pop())
    return l


List_1 = [5, 3, 4, 1, 2]

print(array_cyclic_rotation_solution1(List_1, 2))
