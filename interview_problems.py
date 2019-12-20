
# solution function for question #1


def question_1(str_input):
    return str_input[0] + str(len(str_input) - 2) + str_input[len(str_input)-1]


# solution function for question #2

def question_2(str_input, num):
    res = [None] * len(str_input)
    for i in range(len(str_input)):
        res[i] = substitute_2(str_input, num, i)

    return res


# supporting function for question #2
def substitute_2(str_input2, num, pos):
    # res = [None] * len(str_input2)
    arr_str = list(str_input2)
    arr_str[pos] = str(num)
    return ''.join(arr_str)


# solution function for question #3
def question_3(str_input3):
    res = []
    # i = 2
    for i in range(1, len(str_input3) + 1):
        for j in range(len(str_input3) - i + 1):
            res.append(substitute_3(str_input3, j, i))

    return res


# supporting function for question #3
def substitute_3(str_input3, start_ndx, num):
    res = str_input3[:start_ndx] + str(num) + str_input3[start_ndx + num:]
    return res





def question_3_output_str_recursion(str_input3, start_ndx=0, num=1, res=None):

    if res is None:
        res = []

    if num == len(str_input3) and (num - start_ndx) == len(str_input3):
        print('base')
        return res
    else:
        # for cur_num in range(-1, len(str_input3) + 1):

            # print(cur_str, start_ndx, num, res)
            # res.append(cur_str)
            # start_ndx += 1
            # print(substitute_3(str_input3, start_ndx + 1, num), start_ndx, num)
            # print(res)

            res.append(substitute_3(str_input3, start_ndx, num))
            print(num, start_ndx)
            return question_3_output_str_recursion(str_input3, start_ndx+1, num+1, res)


            # start_ndx = -1

def substitute_3_recursion(str_input3, num, start_ndx=-1, res=None):
    if res is None:
        res = []
    if start_ndx == (len(str_input3) - 1):
        print('base', start_ndx, num)
        res.append(str(num))
    elif start_ndx == (len(str_input3) - 2):

        slice = str_input3[:start_ndx+1] + str(num) + str_input3[start_ndx + num:]
        print('base2', str_input3, start_ndx, num, slice)
        res.append(str_input3[:start_ndx+1] + str(num) + str_input3[start_ndx + num:])
    else:
        print('reur', start_ndx, num)
        res.extend(substitute_3_recursion(str_input3, num, start_ndx+1, res))
    return res



# print(question_1('vendasta'))
#
# print(question_2('food', 2))

# print(question_3('food'))

# print(question_3_output_str_recursion('food'))

print(substitute_3_recursion('food', 4, -1, []))






