'''
for problem definition, check out the following url:
https://app.codility.com/programmers/task/number_of_disc_intersections/

'''


class DiscLog():
    def __init__(self, x, start_end):
        self.x = x
        self.start_end = start_end


def disc_intersections_1(arr):
    disc_history = []
    for i in range(len(arr)):
        disc_history.append(DiscLog(i-arr[i], 1))
        disc_history.append(DiscLog(i+arr[i], -1))
    disc_history.sort(key=lambda d: (d.x, -d.start_end))
    intersections = 0
    active_intersections = 0

    for log in disc_history:
        active_intersections += log.start_end
        if log.start_end > 0:
            intersections += (active_intersections - 1)

        if intersections > 1000000:
            return -1
    return intersections


class Disc():
    def __init__(self, start_x, end_x):
        self.start_x = start_x
        self.end_x = end_x


def disc_intersections_2(arr):
    disc_list = []
    for i in range(len(arr)):
        disc_list.append(Disc(i-arr[i], i+arr[i]))

    disc_list.sort(key=lambda d: (d.start_x, d.end_x))
    count = 0
    for i in range(len(disc_list)):
        # print(disc_list[i].start_x, disc_list[i].end_x)
        for item in disc_list[i+1:]:
            if disc_list[i].end_x > item.start_x:
                count += 1
            if count > 1000000:
                return -1
    return count


discs1 = [1, 5, 2, 1, 4, 0]
print(disc_intersections_2(discs1))


