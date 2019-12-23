
# this is a super slow version
def square_root_1(x):
    if x == 0:
        return 0
    ret_val = x

    while ret_val*ret_val >= x:
        if ret_val*ret_val == x:
            return ret_val
        ret_val -= 1

    return ret_val


# this is a faster version
def square_root_2(x):
    if x == 0:
        return 0
    ret_val = int(x/2)

    while ret_val*ret_val > x or (ret_val+1)*(ret_val+1) < x:
        if ret_val*ret_val > x:
            ret_val -= 1
        elif (ret_val+1)*(ret_val+1) < x:
            ret_val += 1
    return ret_val


# this is an even faster version
def square_root_3(x):
    if x == 0:
        return 0


     # let's use the mid value of x as the first guess
    guess = x / 2

    # we initiate a variable to store the previous guess value
    pre_guess = 0

    while True:
        # to try to make our guess faster, we use the equation to make a guess faster: guess = x / guess
        # but you have use 'guess = (guess + x/ guess) / 2' or "guess = (2*guess + x/guess) / 3"
        # this is because, for example, x=80, then guess is 40, you end up making the guess again to 2
        # however, if we use "guess = (guess + x/ guess) / 2", the result is: (40+2)/2 = 21, quite interesting!!!

        guess = (guess + x / guess) / 2

        # we try to make it converge at this moment, the convergence criteria of this algorithm is guess == pre_guess
        # once it's converged, we return the value
        if int(guess) == int(pre_guess):
            return int(guess)

        # otherwise, we iteratively change the value
        pre_guess = guess



def square_root_4(x):
    if x == 0:
        return 0
    pre_guess = 1

    while True:
        guess = pre_guess - (((pre_guess * pre_guess)-x)/(2*pre_guess))

        if int(guess) == int(pre_guess):
            return int(guess)
        pre_guess = guess



print(square_root_4(2147395599))
