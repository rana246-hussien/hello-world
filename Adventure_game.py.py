#!/usr/bin/python
# -*- coding: utf-8 -*-

# imports
import time
import random

items = []

weapon = ['scarl', 'kar98', 'sniper86', 'awm', 'akm']
monster = [
    'abaal',
    'maksoud',
    'essam',
    'waheed',
    'hamadaa',
    'khaled alqanas',
    ]


def print_pause(message_to_print):
    print (message_to_print)
    time.sleep(2)


# starting messages

def intro():
    print_pause('Welcome our hero!')
    name = input('What is your name ?\n')
    if not name:
        return intro()
    else:
        return intro2(name)


# introduction

def intro2(name):
    weapon_this_game = random.choice(weapon)
    monster_this_game = random.choice(monster)
    items.clear()
    print_pause('\nYou have been chosen, {}, to save obours from monsters.'.format(name))
    print_pause('Dark magic&bad guys are everywhere and you, {}, are our only hope!'.format(name))
    print_pause('Your mission is to find {} and Defeated {} in Obour STEM school!'.format(weapon_this_game,
                monster_this_game))
    print_pause('\nAfter drinking a magic potion, you find yourself in the dark prison cell you should go to monsters home.'
                )
    place_choice(name, weapon_this_game, monster_this_game)


# choose place 1 or 2

def place_choice(name, weapon_this_game, monster_this_game):
    print_pause('''
In front of you are two places choose one to go to monsters.
''')
    place = \
        input('''Enter first to enter the first place.
Enter second to enter the second place.
What place do you want to open ?
''')

    if place == 'first':
        first_place(name, weapon_this_game, monster_this_game)
    elif place == 'second':
        second_place(name, weapon_this_game, monster_this_game)
    else:
        print_pause('Please {}, enter first or second!\n'.format(name))
        place_choice(name, weapon_this_game, monster_this_game)


# choose first place

def first_place(name, weapon_this_game, monster_this_game):
    print_pause('\nYou enter the 9th district.')
    if weapon_this_game in items:
        print_pause('The dark magician appear again and start speaking with you.'
                    )
        print_pause('Sorry, {}, I already gave you the {} to defeat {}.'.format(name,
                    weapon_this_game, monster_this_game))
        print_pause('You thank him again and leave the place.')
        place_choice(name, weapon_this_game, monster_this_game)
    else:
        print_pause('A dark magician appear in front of you and start speaking with you.'
                    )
        print_pause('Hello, {}, I was waiting for you.'.format(name))
        print_pause('Someone told me you will need this to defeat {}.'.format(monster_this_game))
        print_pause('The dark magician make appear the {} and give it to you.'.format(weapon_this_game))
        print_pause('You thank him and leave the 9th district.')
        items.append(weapon_this_game)
        place_choice(name, weapon_this_game, monster_this_game)


# choose seconde place

def second_place(name, weapon_this_game, monster_this_game):
    print_pause('\nYou enter the obour STEM school.')
    print_pause("This is the {}'s hiding place!".format(monster_this_game))
    choice_fight(name, weapon_this_game, monster_this_game)
    if weapon_this_game in items:
        print_pause('\nThe {} attacks you as soon as you pass the place!'.format(monster_this_game))
        if weapon_this_game == 'kar98':
            print_pause('You do your best...')
            print_pause('but you realize your {} is just a carrot!'.format(weapon_this_game))
            print_pause('Too late!')
            print_pause('You have been defeated.')
            play_again(name)
        else:
            print_pause('After an heroic fight, you defeat {}, thanks to {}!'.format(monster_this_game,
                        weapon_this_game))
            print_pause('\nCongratulations! You save obour STEM school from dark forces!'
                        )
            play_again(name)
    else:
        print_pause('\nAre you sure you want to fight the {} without the {}?'.format(monster_this_game,
                    weapon_this_game))
        choice_fight(name, weapon_this_game, monster_this_game)
        print_pause('\nThe {} attacks you as soon as you pass the place!'.format(monster_this_game))
        print_pause('You do your best...')
        print_pause('but without the {}, the {} win easily!'.format(weapon_this_game,
                    monster_this_game))
        print_pause('You have been lose from him.')
        play_again(name)


# choose fight or not

def choice_fight(name, weapon_this_game, monster_this_game):
    fight_or_not = \
        input('''
Would you like to (fight) fight or (withdraw) go back to the place choice?
''')
    if fight_or_not == 'fight':
        return True
    elif fight_or_not == 'withdraw':
        place_choice(name, weapon_this_game, monster_this_game)
    else:
        print_pause('Please {}, enter fight or withdraw!\n'.format(name))
        choice_fight(name, weapon_this_game, monster_this_game)


# play the game again

def play_again(name):
    choice_again = \
        input("""
Would you like to play again ? Please say 'yes' or 'no'.
""").lower()
    if 'yesno' in choice_again:
        print_pause("Please {}, enter 'yes' or 'no'!".format(name))
        play_again(name)
    elif 'yes' in choice_again:

        print_pause('\nExcellent {}, restarting the game ...'.format(name))
        intro2(name)
    elif 'no' in choice_again:

        print_pause('\nOk, Goodbye {}.'.format(name))
    else:
        print_pause("Please {}, enter 'yes' or 'no'!".format(name))
        play_again(name)


# go to the first of the code again

intro()
