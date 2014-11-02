# Created by Eli Foster
# 0.1.0

import sys

# EDIT THIS IF YOU HAVE CHANGED YOUR DIRECTORY NAMES
directory = 'work/abbrev_output.txt'

name = raw_input("What is the mod's name?\n")
abbrev = raw_input("What would you like its abbreviation to be?\n")

fileout = open(directory, "w")
fileout.write("|" + abbrev + " = {{#if:{{{name|}}}{{{code|}}}||_(}}{{#if:{{{name|}}}{{{link|}}}|" + name + "|" + abbrev + "}}{{#if:{{{name|}}}{{{code|}}}||)}}\n|" + name + " = {{#if:{{{name|}}}{{{code|}}}||_(}}{{#if:{{{name|}}}{{{link|}}}|" + name + "|" + abbrev + "}}{{#if:{{{name|}}}{{{code|}}}||)}}")
fileout.close()

sys.exit()

'''
== Changelog ==
=== 0.1.0 ===
* Initial
'''