def maxNumberOfBalloons(text, balloon_str='balloon'):
    balloon_list_check = list(balloon_str)
    count = 0

    for _, char in enumerate(text):
        if char in balloon_list_check:
            balloon_list_check.remove(char)

        if len(balloon_list_check) == 0:
            count += 1
            balloon_list_check = list(balloon_str)

    return count


def cleanString(text, balloon_str='balloon'):
    text_list = list(text)
    for char in text_list:
        if char not in balloon_str:
            text_list.remove(char)

    return str(text_list)

print(maxNumberOfBalloons(cleanString('loonbalxballpoonballtdoon')))