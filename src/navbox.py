# Created by Eli Foster
# 0.1.1
# If you are running Python 3, change all instances of raw_input to input.
# This program should be used with navitem. This will not do any of the list#= stuff, use navitem for that. This is just for formatting a box.

import sys
from navbox_small import small_navbox

'''The output file dir. Change this if you want it to be different. This file must already exist.'''
output = 'work/navbox_output.txt'

nav_complexity = raw_input("Would you like it small or big?\n")

def determine_complexity():
    if (nav_complexity == 'small'):
        small_navbox()
        sys.exit()
    elif (nav_complexity == 'big'):
        print("The big_navbox method is not yet implemented. Quitting program.")
        sys.exit()
        #big_navbox()
    elif (nav_complexity != 'big' and nav_complexity != 'small'):
        print ("Please put big or small as input, strings only. Quitting program.")
        sys.exit()

determine_complexity()
sys.exit()

'''
== Changelog ==
=== 0.1.1 ===
* FIX: Changed output dir to actually work.
=== 0.1.0 ===
* Initial. No big navboxes so far.

'''