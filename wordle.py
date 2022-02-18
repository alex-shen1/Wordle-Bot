import enchant
import re
from random import shuffle
from sys import exit
d = enchant.Dict("en_US")

# Capital A-Z when converted to ASCII
letters = [chr(n) for n in range(65, 91)]
# Sorted in order of frequency (https://www.lexico.com/explore/which-letters-are-used-most)
letters = ['E', 'A', 'R', 'I', 'O', 'T', 'N', 'S', 'L', 'C', 'U', 'D',
           'P', 'M', 'H', 'G', 'B', 'F', 'Y', 'W', 'K', 'V', 'X', 'Z', 'J', 'Q']


yellow_letters = dict()  # Maps index to letters
banned_letters = set()


def recursive_solve(word, cap=float('inf')):
    if '0' not in word:
        # Make sure the word is valid, contains all expected letters, and does NOT contain
        # eliminated letters
        if d.check(word):
            if all(l in word for l in yellow_letters.keys()):
                # Make sure yelllow are not in yellow spots
                for letter, yellow_positions in yellow_letters.items():
                    positions = set([m.start(0)
                                     for m in re.finditer(letter, word)])
                    # An intersection of sets indicates that the word shouldn't be a valid answer
                    if len(positions & yellow_positions) != 0:
                        # print(f'{word} rejected for including {letter} in wrong spot')
                        return set()
                print(f'{word} accepted as possible candidate')
                return {word}
            else:
                pass
                # print(word, 'did not contain all yellow letters')
        return set()
    else:
        possible_solutions = set()
        temp = word
        i = temp.index('0')
        for letter in letters:
            combo = temp[0:i] + letter
            if len(combo) < 5:  # Covers edge case where 0 is on last character
                combo += temp[i+1:]
            possible_solutions = set.union(
                possible_solutions, recursive_solve(combo, cap=max(0, cap-5)))
            if len(possible_solutions) > cap:
                print(f'{word} - Reached cap of {cap}, terminating')
                return possible_solutions
        return possible_solutions


answer = '00000'  # 0 represents unknown, start off knowing nothing

for i in range(6):
    print(f'Guess {i+1}:')
    guess = input().upper()
    if guess == '~':  # Manual override to terminate program if guess is correct
        print('Congratulations on winning!')
        exit(0)
    print(f'Result of guess {i+1}:')
    result = input().upper()

    assert len(guess) == 5
    assert len(result) == 5
    for j in range(5):
        guessed_letter = guess[j]
        if result[j] == '0':
            if guessed_letter in letters:
                letters.remove(guessed_letter)
        elif result[j] == 'Y':
            if not guessed_letter in yellow_letters.keys():
                yellow_letters[guessed_letter] = set()
            yellow_letters[guessed_letter].add(j)
        elif result[j] == 'G':
            temp = answer[0:j] + guessed_letter
            if len(temp) < 5:
                temp += answer[j+1:]
            answer = temp
        else:
            print('Result string must only contain 0, Y, G')
            exit(1)

    print(
        f'Answer: {answer}; known letters: {yellow_letters}; viable letters: {letters}')
    num_unknowns = len(re.findall("0", answer))
    possible = recursive_solve(answer, cap=(6-num_unknowns) * 10)

    print()
    if len(possible) == 1:
        print('Answer:', next(iter(possible)))
        exit(0)
    else:
        print('Possible answers:', possible)
