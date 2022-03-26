#!/usr/bin/env python3

from random import randint
import sys

def random_str(n1,n2):
    x = randint(n1,n2)
    return (x)

def random_line(files,n1,n2):
    lines = []
    rand_line = []
    with open(files) as f:
        lines = f.readlines()
        return(lines[random_str(n1,n2)])

def count_line(f):
    try:
        with open(f, 'r') as fp:
            num_lines = sum(1 for line in fp)
        return (num_lines)
    except:
        print("The file doesn't exist put a valid one")
        quit()

if len(sys.argv) == 1:
    print("Please put a file as argument")
    quit()

file_path = sys.argv[1]
num_of_line = count_line(file_path)

try:
    check_empty_file = random_line(file_path,0,num_of_line - 1)
except:
    print("The file is empty please put at least one word inside")
    quit()

word_to_find = random_line(file_path,0,num_of_line - 1)

word_you_guess = ""
original_string = ""
idx = 33

for i in range(len(word_to_find) - 1):
    word_you_guess = word_you_guess + str(chr(idx))
    original_string = original_string + str(chr(idx))
    idx = idx + 1

def replace_word(psx,word_you_guess,char):
    if psx != -1:
        word_you_guess = word_you_guess.replace(word_you_guess[psx],char)
    return (word_you_guess)

def letter_pos(char,word_you_guess):
    l = []
    for i in range(len(word_you_guess)):
        if word_you_guess[i] == char:
            l.append(i)
    if len(l) != 0:
        return(l)
    else:
        l = [-1]
        return (l)

def check_win(word_you_guess,original_string):
    idx = 0
    for i in range(len(word_you_guess)):
        if word_you_guess[i] == original_string[i]:
            idx = idx + 1
    return (idx)

chance = 7
wrong_letter = ""
while True:
    print("\n------------------------------")
    print(word_you_guess)
    print("------------------------------")
    input_guess = input("Put a letter big bro: ")
    if len(input_guess) == 0:
        input_guess = "#"
    elif input_guess[0].isalpha() == False:
        print("Please put letter")
    w_list = letter_pos(input_guess[0],word_to_find)
    for i in range(len(w_list)):
        word_you_guess = replace_word(w_list[i],word_you_guess,input_guess[0])
    if w_list == [-1] and chance != 0 and input_guess[0].isalpha() == True:
        chance = chance - 1
        wrong_letter = wrong_letter + input_guess[0] + " "
        if chance != 0:
            print("You still have " + str(chance) + " guess")
    if chance == 0:
        print("You lost bro")
        print("The word was " + word_to_find)
        quit()
    if check_win(word_you_guess,original_string) == 0:
        print("You win bro")
        print("The word was " + word_to_find)
        quit()
    print("Letter that you already try: " + wrong_letter)