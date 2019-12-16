
def remove_outer_parentheses(input_str):

    input_list = list(input_str)
    left = '('
    right = ')'
    stack = []
    outer_index_record = []

    i = 0

    while len(input_list) > 0:

        current_char = input_list.pop(0)

        if current_char == left:
            stack.append(i)
            if len(stack) == 1:
                outer_index_record.append(i)

        if current_char == right:
            stack.pop()
            if len(stack) == 0:
                outer_index_record.append(i)

        i += 1

    res = ''
    for i in range(len(input_str)):
        if i not in outer_index_record:
            res += input_str[i]

    return res


S1 = "(()())(())" #out: ()()()
S2 = "(()())(())(()(()))" #out: ()()()()(())
S3 = "()((()))"   #out: (())
S4 = "(()(()))()" #out: ()(())

print(remove_outer_parentheses(S4))