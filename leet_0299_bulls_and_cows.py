'''
You are playing the following Bulls and Cows game with your friend: You write down a number and ask
your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that
 indicates how many digits in said guess match your secret number exactly in both digit and position
 (called "bulls") and how many digits match the secret number but locate in the wrong position
 (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret
 number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate
 the bulls and B to indicate the cows.

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, and their
 lengths are always equal.

'''

# this is an array version, a little messy and inefficient, but works anyway
def bulls_cows(secret, guess):

    num_bulls = 0

    non_bull_secret = []
    non_bull_guess = []

    for i in range(len(secret)):
        if secret[i] == guess[i]:
            num_bulls += 1
        else:
            non_bull_secret.append(secret[i])
            non_bull_guess.append(guess[i])

    num_cows = 0
    idx = 0
    dyna_secret = list(non_bull_secret)
    while len(dyna_secret) > 0 and idx < len(non_bull_secret):
        if non_bull_guess[idx] in dyna_secret:
            dyna_secret.remove(non_bull_guess[idx])
            num_cows += 1
        elif non_bull_secret[idx] == non_bull_guess[idx]:
            dyna_secret.remove(non_bull_guess[idx])
        idx += 1

    return str(num_bulls) + 'A' + str(num_cows) + 'B'

# this is a string operation version, accelerated
def bulls_cows2(secret, guess):
    if secret == '':
        return '0A0B'

    num_bulls = 0
    num_cows = 0

    non_bull_secret = ''
    non_bull_guess = ''

    for i in range(len(secret)):
        if secret[i] == guess[i]:
            num_bulls += 1
        else:
            non_bull_secret += secret[i]
            non_bull_guess += guess[i]

    for char in non_bull_guess:
        found_idx = non_bull_secret.find(char)

        if found_idx > -1:
            non_bull_secret = non_bull_secret.replace(non_bull_secret[found_idx], '', 1)
            num_cows += 1

    return str(num_bulls) + 'A' + str(num_cows) + 'B'


# this is a dictionary version
def bulls_cows3(secret, guess):
    non_bull_secret_dict = {}
    non_bull_guess_dict = {}
    for s in secret + guess:
        non_bull_secret_dict[s] = 0
        non_bull_guess_dict[s] = 0

    num_bulls = 0
    num_cows = 0
    for i in range(len(guess)):
        if secret[i] == guess[i]:
            num_bulls += 1
        else:
            # we count all numbers of non-bull characters
            non_bull_secret_dict[secret[i]] += 1
            non_bull_guess_dict[guess[i]] += 1

    # for each key in non-bull guess dictionary, if it can be found in non-bull secret dictionary
    # it can be a cow, however we should remove the duplicates
    for item in non_bull_guess_dict:
        num_cows += min(non_bull_guess_dict[item], non_bull_secret_dict[item])

    return str(num_bulls) + 'A' + str(num_cows) + 'B'


# this is a string version along with min() operation，super fast
def bulls_cows4(secret, guess):


    num_bulls = 0
    num_cows = 0

    non_bull_secret = ''
    non_bull_guess = ''

    for i in range(len(secret)):
        if secret[i] == guess[i]:
            num_bulls += 1
        else:
            non_bull_secret += secret[i]
            non_bull_guess += guess[i]

    # for all letters in non-bull guesses, we can use set to avoid duplication
    for char in set(list(non_bull_guess)):

        if non_bull_secret.find(char) > -1:
            num_cows += min(non_bull_secret.count(char), non_bull_guess.count(char))

    return str(num_bulls) + 'A' + str(num_cows) + 'B'

# expect "1A3B"
# secret1 = "1807"
# guess1 =  "7810"

# expect "1A1B"
# secret1 = "1123"
# guess1 =  "0111"

# expect "0A4B"
secret1 = "1122"
guess1 =  "2211"

# expect "0A1B"
# secret1 = "1122"
# guess1 =  "0001"

# expect "3A0B"
# secret1 = "1122"
# guess1 =  "1222"

print(bulls_cows4(secret1, guess1))