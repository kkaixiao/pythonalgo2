'''

Given an expression string, write a python program to find whether a given string has balanced parentheses or not.

Examples:

Input : {[]{()}}
Output : Balanced

Input : [{}{}(]
Output : Unbalanced

'''


def balanced_brackets(brackets):
    left_brackets = '{(['
    right_brackets = '})]'
    right_to_left_dict = {'}': '{', ')': '(', ']': '['}

    my_stack = []

    for item in brackets:
        if item in left_brackets:
            my_stack.append(item)
        if item in right_brackets and right_to_left_dict[item] == my_stack[len(my_stack) - 1]:
            my_stack.pop()

    if len(my_stack) == 0:
        return 'Balanced'
    else:
        return 'Unbalanced'


arr1 = '{[]{()}}'  # balanced
arr2 = '[{}{}(]'   # unbalanced
arr3 = '(}(}'      # unbalanced

print(balanced_brackets(arr3))
