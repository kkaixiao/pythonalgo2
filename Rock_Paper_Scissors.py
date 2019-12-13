# scissors

from random import randint


def play_rock_paper_scissors():
    matrix_hands = {0: 'Rock', 1: 'Paper', 2: 'Scissors'}
    matrix_results = {0: 'won', 1: 'tie', 2: 'lost'}

    matrix_combination = {'00': 1, '11': 1, '22': 1, '01': 2, '02': 0, '10': 0, '12': 2, '20': 2, '21': 0}

    your_hand = randint(0, 2)

    computer_hand = randint(0, 2)

    res = matrix_combination[str(your_hand) + str(computer_hand)]

    return matrix_hands[your_hand], matrix_hands[computer_hand], matrix_results[res]


result = play_rock_paper_scissors()

print('Your hand is: ' + result[0])
print('Computer hand is: ' + result[1])
print('You ' + result[2] + '.')
