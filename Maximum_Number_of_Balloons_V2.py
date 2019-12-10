

# recursion version of max number of balloons
# The bugs should be removed


def max_number_of_balloons(text_list, balloon_str='balloon', count=0):
    if len(text_list) < len(balloon_str):
        return count

    balloon_list_check = list(balloon_str)

    for _, char in enumerate(balloon_str):
        balloon_list_check.remove(char)
        if char in text_list:
            text_list.remove(char)

            if len(balloon_list_check) == 0:
                return max_number_of_balloons(text_list, 'balloon', count+1)


def clean_string(text, balloon_str='balloon'):
    balloon_list = balloon_str
    text_list = list(text)
    for char in text_list:
        if char not in balloon_list:
            text_list.remove(char)
    return ''.join(text_list)

input_str = 'abfereerhoolnlbsdfdbabalooolnllnooaoolln'

print(max_number_of_balloons(list(clean_string(input_str))))
