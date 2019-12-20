import collections


def repeated_n_times(A):
    count = collections.Counter(A)
    print(count)
    for k in count:
        if count[k] > 1:
            return k


A1 = [1,2,3,3]
A2 = [2,1,2,5,3,2]
A3 = [5,1,5,2,5,3,5,4]


print(repeated_n_times(A3))