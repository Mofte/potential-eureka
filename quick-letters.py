#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, time
from timeit import default_timer as timer
from datetime import timedelta

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
divider = '\n' + '-' * 50 + '\n'
play_a_game = ''
ready = ''

print(divider)

print('Be quick or be... slow.')

print(divider)

while play_a_game != 'n' and play_a_game != 'y':
    play_a_game = input('Do you want to play a game? (y/n) ')
    print(divider)
    if play_a_game == 'n':
        print('Okay... :-(')
        print(divider)
        exit()
    elif play_a_game == 'y':
        print('Great! :-)')

print(divider)

print('Simply press the letter that appears on the screen and confirm it with enter. That\'s it.')

print(divider)

while ready != 'n' and ready != 'y':
    ready = input('Ready? (y/n) ')
    print(divider)
    if ready == 'n':
        print('Fine, I\'ll wait...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        ready = ''
        while ready != 'n' and ready != 'y':
            print(divider)
            ready = input('Ready now? (y/n) ')
            print(divider)
            if ready == 'y':
                break
            elif  ready == 'n':
                print('All right, come back later.')
                print(divider)
                exit()
    elif ready == 'y':
        break
        
rounds_total = int(input('How many rounds do you want to play to a maximum of 20? '))

if rounds_total > 20:
    rounds_total = 20

print(divider)

print(f'Okay, let\'s go, you are playing {rounds_total} rounds!')

print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('GO!')
print(divider)

rounds_counter = rounds_total
points = 0
errors = 0

start = timer()

while rounds_counter > 0:
    letter_expected = random.choice(letters)
    print('Please press this button:\n')
    letter_in = input(letter_expected + ' - ')
    print(divider)
    if letter_in == letter_expected:
        points += 1
    else:
        errors += 1
    rounds_counter -= 1

end = timer()

elapsed_time = timedelta(seconds=end-start).total_seconds()

print(divider)

print('Game over!')

print(divider)

print(f'You played {rounds_total} rounds. You finished in {elapsed_time} seconds and scored {points} point(s) with {errors} error(s).')

print(divider)

