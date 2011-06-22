#!/usr/bin/python

import random

def choose(do_change):
    # goat is hidden at one of the three doors
    goat_hide = random.randint(1,3)
    # print "goat at door ", goat_hide

    # player chooses
    player_chose_1 = random.randint(1,3)
    # print "player chose  ", player_chose_1

    # quiz master chooses one of the to doors with nothing behind
    nothing = []
    for i in range(1,4):
        if not i == goat_hide and not i == player_chose_1:
            nothing.append(i)
    quizmaster_chose = random.randint(0,len(nothing)-1)
    quizmaster = nothing[quizmaster_chose]
    quizmaster_left_over = []
    for i in range(1,4):
        if not i == quizmaster:
            quizmaster_left_over.append(i)
    # quizmaster opens one door
    # print "quizmaster opens ", quizmaster
    doors_left = []
    for i in quizmaster_left_over:
        doors_left.append(i)

    # second choice of player
    player_chose_2 = None
    if do_change:
        for i in doors_left:
            if not i == player_chose_1:
                player_chose_2 = i
    else:
        player_chose_2 = player_chose_1

    # print "player_chose_2 ", player_chose_2

    # player won?
    if player_chose_2 == goat_hide:
        return True
    else:
        return False

def experiment(number_of_runs):
    # first: player always changes the first choice
    won_with_always_changing = 0.0
    for i in range(number_of_runs):
        if choose(True):
            won_with_always_changing += 1.0

    # second: player sticks with the first choice
    won_without_changing = 0.0
    for i in range(number_of_runs):
        if choose(False):
            won_without_changing += 1.0

    print "number of experiments: ", number_of_runs
    print "won with always changing: %i, %s%%" % (won_with_always_changing, str(won_with_always_changing/number_of_runs))
    print "won without chaning: %i, %s%%" % (won_without_changing, str(won_without_changing/number_of_runs))

experiment(100000)
