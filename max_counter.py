
def max_counter(m,n):
    dict = {}
    for item in m:
        dict[item] = 0

    for item in m:
        if dict[item] != 0:
            dict[item] += 1
        else:
            dict[item] = 1


    return dict

print(max_counter([3, 4, 4, 6, 1, 4, 4], 5))