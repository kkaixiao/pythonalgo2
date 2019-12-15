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

    detect_stack = []

    for item in brackets:
        if item in left_brackets:
            detect_stack.append(item)
        if item in right_brackets and len(detect_stack) == 0:
            return 'Unbalanced'
        if item in right_brackets and right_to_left_dict[item] == detect_stack[len(detect_stack) - 1]:
            detect_stack.pop()

    if len(detect_stack) == 0:
        return 'Balanced'
    else:
        return 'Unbalanced'


arr1 = '{[]{()}}'       # balanced
arr2 = '[{}{}(]'        # unbalanced
arr3 = '(}(}'           # unbalanced
arr4 = '({)}'           # unbalanced
arr5 = '[)'             # unbalanced
arr6 = '{{{[]}}}}'      # unbalanced

print(balanced_brackets(arr6))
