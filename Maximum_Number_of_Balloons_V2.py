

# recursion version of max number of balloons
# I think there's something wrong, but at least the whole logic is built

def maxNumberOfBalloons(text_list, balloon_str='balloon', count=0):
    if len(text_list) < len(balloon_str):
        return count

    balloon_list_check = list(balloon_str)

    for _, char in enumerate(balloon_str):
        balloon_list_check.remove(char)
        if char in text_list:
            text_list.remove(char)

        if len(balloon_list_check) == 0:
            return maxNumberOfBalloons(text_list, 'balloon', count+1)


def cleanString(text, balloon_str='balloon'):
    balloon_list = balloon_str
    text_list = list(text)
    for char in text_list:
        if char not in balloon_list:
            text_list.remove(char)
    return ''.join(text_list)

input_str = 'abfereerhoolnlbsdfdbabalooolnllnooaoolln'

print(maxNumberOfBalloons(list(cleanString(input_str))))
