#! python3

import sys

# My first beginner project
'''
    This is a program that converts sentence in to abbreviation.
    Version 0.0.1
    Type --version for version info
    It works with string and also works lists and tuples etc
'''

def version():
    if sys.argv:
        if sys.argv[-1] == '--version':
            return 'version 0.0.1'


def abbreviator(abb):
    # =====this logic prints the verion of the software=====
    if sys.argv[-1] == '--version':
        print(version())

    # =====this logic prints non_grouped sentence abbreviation=====
    if isinstance(abb, str):
        for spl in abb.split():
            if not spl.lower() in ('at','is','and'):
                print(spl[0].upper() + '.', end='') 

    #=====this logic prints the abbreviation of grouped letters=====
    elif isinstance(abb, (list, tuple)):
        for spl in abb:
            if not spl.lower() in ('at','is','and'):
                print(spl[0].upper() + '.', end='')



ls = ['chidera','chisom']



if __name__ == '__main__':
    abbreviator(ls)
