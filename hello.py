#!/usr/bin/env python3
# creating my first program
# Purpose : Say hello
print('Hello, World!')

# Purpose : Say hello
import argparse
parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('Hello, Universe!' , help= 'Hello, Universe!')
args = parser.parse_args()
print('Hello, Universe ' + args.name + '!')


#I do not understand 'testing the program' at all, the one explained in the tiny python project. 
# I will appreciate if anyone can explain to me. I am totally lost at that aspect 