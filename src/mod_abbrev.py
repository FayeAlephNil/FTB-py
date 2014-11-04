# Created by Eli Foster
# 0.1.0

import sys
from Tkinter import *

# EDIT THIS IF YOU HAVE CHANGED YOUR DIRECTORY NAMES
directory = 'work/abbrev_output.txt'


def fn_run():
    tk = Tk()
    namevar = StringVar()
    abrvvar = StringVar()
    namelabel = Label(tk, text="Mod Name",  textvariable=namevar)
    abrvlabel = Label(tk, text="Mod Abbreviation", textvariable=abrvvar)
    quit = Button(tk, text="Close", command=tk.quit)

    nameentry = Entry(tk)
    abrventry = Entry(tk)

    namelabel.pack()
    nameentry.pack()
    abrvlabel.pack()
    abrventry.pack()
    quit.pack()

    tk.mainloop()
    tk.quit()

    fileout = open(directory, "w")
    fileout.write("|" + abrvvar.get().capitalize + " = {{#if:{{{name|}}}{{{code|}}}||_(}}{{#if:{{{name|}}}{{{link|}}}|" + namevar.get() + "|" + abrvvar.get().capitalize + "}}{{#if:{{{name|}}}{{{code|}}}||)}}\n|" + namevar.get() + " = {{#if:{{{name|}}}{{{code|}}}||_(}}{{#if:{{{name|}}}{{{link|}}}|" + namevar.get() + "|" + abrvvar.get().capitalize + "}}{{#if:{{{name|}}}{{{code|}}}||)}}")
    fileout.close()

    sys.exit()

fn_run()

'''
== Changelog ==
=== 0.1.0 ===
* Initial
'''