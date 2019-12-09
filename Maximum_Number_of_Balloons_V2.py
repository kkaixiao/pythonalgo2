

# recursion version of max number of balloons
# I think there's something wrong, but at least the whole logic is built

def maxNumberOfBalloons(text_list, balloon_str='balloon', count = 0):
    if len(text_list) < len(balloon_str):
        return count

    balloon_list_check = list(balloon_str)
    for i in range(len(text_list)):
        char = text_list[i]
        try:
            char_index = balloon_list_check.index(char)
        except ValueError:
            char_index = -1
        if char_index >= 0:
            balloon_list_check.pop(char_index)
            if len(balloon_list_check) == 0:

                return maxNumberOfBalloons(text_list[i:], 'balloon', count+1)





print(maxNumberOfBalloons('loonbalbalballoonlodfoballoballoondfonndballoofddn'))
