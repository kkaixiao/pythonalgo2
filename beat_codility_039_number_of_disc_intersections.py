'''
for problem definition, check out the following url:
https://app.codility.com/programmers/task/number_of_disc_intersections/

'''


class DiscLog():
    def __init__(self, x, start_end):
        self.x = x
        self.start_end = start_end


def disc_intersections(arr):
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


discs1 = [1, 5, 2, 1, 4, 0]
print(disc_intersections(discs1))


