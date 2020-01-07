class Foo(object):
    # check if first function is running
    running_first = False

    # check if second function is running
    running_second = False

    def __init__(self):
        pass

    def first(self, printFirst):
        # run first
        printFirst()

        # mark first function finished
        self.running_first = True

    def second(self, printSecond):
        # wait to see if first function finished
        while not self.running_first:
            continue

        # run second
        printSecond()

        # mark second finished
        self.running_second = True

    def third(self, printThird):
        # wait to see if second function finished
        while not self.running_second:
            continue

        # run third and finish all
        printThird()


