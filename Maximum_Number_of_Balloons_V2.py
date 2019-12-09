

# recursion version of max number of balloons

def maxNumberOfBalloons(text_list, balloon_str='balloon', count = 0):
    if len(text_list) < len(balloon_str):
        return count

    balloon_list_check = list(balloon_str)
    for i in range(len(text_list)):
        char = text_list[i]
        char_index = -1
        try:
            char_index = balloon_list_check.index(char)
        except ValueError:
            char_index = -1
        if char_index >= 0:
            balloon_list_check.pop(char_index)
            if len(balloon_list_check) == 0:

                return maxNumberOfBalloons(text_list[i:], 'balloon', count+1)



def cleanString(text, balloon_str='balloon'):
    balloon_list = balloon_str
    text_list = list(text)
    for char in text_list:
        if char not in balloon_list:
            text_list.remove(char)
    return text_list

def is_match(text_list, balloon_str):
    balloon_check_list = list(balloon_str)
    text_list.sort()
    balloon_check_list.sort()
    if balloon_check_list == text_list:
        return True
    else:
        return False


print(maxNumberOfBalloons(cleanString('loonbalballoondballoon')))

# print(is_match(['l', 'a', 'l', 'n', 'o', 'o', 'b'], 'balloon'))
# a= 'abccefg'
# print(a.index('h'))