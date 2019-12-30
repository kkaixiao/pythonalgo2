def remove_adjacent_duplicates(chars):
    if len(chars) <= 1:
        return chars
    else:
        list_chars = list(chars)
        for i in range(len(list_chars)-1):
            if list_chars[i] == list_chars[i+1]:
                for _ in range(2):
                    list_chars.pop(i)
                return remove_adjacent_duplicates(''.join(list_chars))
        return chars


def remove_adjacent_duplicates2(chars):
    if len(chars) <= 1:
        return chars
    else:
        for i in range(len(chars)-1):
            if chars[i] == chars[i+1]:
                chars = chars[:i] + chars[i:].replace(chars[i], '', 2)
                return remove_adjacent_duplicates(chars)
        return chars


def remove_adjacent_duplicates3(chars):

    if len(chars) <= 1:
        return chars

    count = 0
    stack = []


    while count < len(chars):
        if len(stack) == 0:
            stack.append(chars[count])
        elif len(stack) >= 1:
            stack.append(chars[count])
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
        count += 1

    return ''.join(stack)



def remove_adjacent_duplicates4(chars):
    if len(chars) <= 1:
        return chars

    temp_s = ''

    for count in range(len(chars)):
        if len(temp_s) == 0:
            temp_s += chars[count]
        else:
            temp_s += chars[count]
            if temp_s[-1] == temp_s[-2]:
                temp_s = temp_s[:-2]

    return temp_s

str1= 'abbaca'
print(remove_adjacent_duplicates4(str1))

# a = []
# print(a[-1])
# s = 'abcde'
# print(s[-1], s[:-2])
