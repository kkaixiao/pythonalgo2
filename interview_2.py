# This is Python 3

starting_stack_size, max_stable_height, partition = map(int, input().split())



# sum|max|each

def res(starting_stack_size, max_stable_height, partition):
    s = 1
    p = 0

    # sav is the list to save number of piles, each item denotes book number in the pile
    sav = list()
    sav.append(starting_stack_size)

    # s is the variable showing that it is now running
    # while p != 0 or s == 1:
    while p != 0 or s == 1:
        s = 0
        p = 0
        for i in sav:
            # if one item in the pile is greater than stable_height, we'll need to partition it
            if i > max_stable_height:

                # if one item is lower than number_of_partition, we just return starting_stack_size
                # which means, we return starting_stack_size of 1 book
                if i < partition:
                    return starting_stack_size

                # now we calculate t, which is the floor number of this item divided by partition
                t = i // partition

                # now we start a loop, to add all new partitions to the sav list
                # we'll have number (partition) of new partitions, so we add to them
                # for example, suppose current i is 25, partition is 4
                # then we will have t = 6, and we should decompose 25 into 6, 6, 6, 6, 1
                # the following line will append the following thing:
                #  (6, (25-6*(4-1)), 6, (25-6*(4-1)), 6, (25-6*(4-1)))
                # =(6, 7, 6, 7, 6, 7)
                # which is wrong


                # for j in range(partition - 1):
                #     sav.append(t)
                #     sav.append(i - t * (partition - 1))
                #     p += 1
                # sav.remove(i)

                # the correct one should be:
                for j in range(partition-1):
                    sav.append(t)

                    # the partition process will stop if p == 0
                    p += 1

                # we can append the last remaining item after partition
                sav.append(i - t * (partition - 1))

                # we'll remove the item before partition, which is valued by i
                sav.remove(i)



    return len(sav)


print(res(starting_stack_size, max_stable_height, partition))