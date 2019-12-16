
def remove_outer_parentheses(input_str):

    input_list = list(input_str)
    left = '('
    right = ')'
    stack = []

    i = 0
    res = ''
    while len(input_list) > 0:

        current_char = input_list.pop(0)

        if current_char == left:
            stack.append(i)

            if len(stack) > 1:
                res += current_char

        if current_char == right:
            stack.pop()
            if len(stack) > 0:
                res += current_char

        i += 1

    return res


S1 = "(()())(())" #out: ()()()
S2 = "(()())(())(()(()))" #out: ()()()()(())
S3 = "()((()))"   #out: (())
S4 = "(()(()))()" #out: ()(())

print(remove_outer_parentheses(S4))