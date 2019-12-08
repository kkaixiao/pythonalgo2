# This is Python 3

starting_stack_size, max_stable_height, partition = map(int, input().split())



# sum|max|each
def res(starting_stack_size, max_stable_height, partition):
    s = 1
    p = 0
    sav = list()
    sav.append(starting_stack_size)
    while p != 0 or s == 1:
        s = 0
        p = 0
        for i in sav:
            if i > max_stable_height:
                if (i < partition):
                    return starting_stack_size
                t = i // partition
                for j in range(partition - 1):
                    sav.append(t)
                    sav.append(i - t * (partition - 1))
                    p += 1
                sav.remove(i)
    return len(sav)


print(res(starting_stack_size, max_stable_height, partition))