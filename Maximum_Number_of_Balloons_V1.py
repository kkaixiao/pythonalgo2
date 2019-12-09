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



print(maxNumberOfBalloons('loonbalxballpoonballtdoo'))