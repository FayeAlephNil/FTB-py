# Created by Eli Foster
# Version 0.1.0

from Tkinter import *
import tkMessageBox
from navitem import run
import ScrolledText
import tempfile
import shutil
import os

directory = 'work/navitem_output.txt'

def open_changelog():
    cl = Tk()
    changelog = Message(cl, text="== Changelog ==\n=== navitem ===\n==== 0.1.6 ====\n*FIX: Shoved everything in run() method\n\n==== 0.1.5 ====\n *FIX: Changed directories AGAIN\n\n==== 0.1.4 ====\n* FIX: Changed directories to work/navitem/input-output.txt, for when I add more programs\n\n==== 0.1.3 ====\n* FIX: Fixed tab spacing; it's no longer 4 spaces, and is actually indents\n\n==== 0.1.2 ====\n* FIX: No longer overwrites input.txt; instead it makes output.txt\n* FIX: It should work now,  though be weird, on non-UNIX systems (thanks Wolfman)\n* FIX: Program exits properly using sys.exit()\n\n==== 0.1.1 ====\n* FIX: Made the text that gets written actually correct\n* TWEAK: Changed modname raw_input text\n\n==== 0.1.0 ====\n* Initial\n\n\n=== navbox ===\n==== 0.1.1 ====\n* FIX: Changed output dir\n\n==== 0.1.0 ====\n* Initial\n\n\n=== mod abbrev ===\n==== 0.1.0 ====\n* Initial")
    changelog.pack()
    cl.mainloop()

def navitem_():
    nav = Tk()
    navlabel = Label(nav, text="Mod abbreviation")
    navlabel.pack()
    naventry = Entry(nav, bd =5)
    naventry.pack()

    textlabel = Label(nav, text="Input").pack()
    ScrolledText.ScrolledText(nav, bd=5).pack(side=BOTTOM)
    nav.mainloop()

    tmp = tempfile.NamedTemporaryFile(delte=False)
    with open(directory) as finput:
        with open(tmp.name, 'w') as ftmp:
            for line in finput:
                x = str(line)
                ftmp.write("\t-->{{NI|" + x.rstrip("\r\n") + "|mod=" + naventry.get() + "}}{{,}}<!--\n")
    try:
        shutil.copyfile(tmp.name, directory)
    except:
        print "There was an issue using shutil! Trying to use os instead."
        os.rename(directory, directory)
    #run()



def main():
    tk = Tk()
    changelog_button = Button(tk, text="Changelog", command=open_changelog)
    navitem_butt = Button(tk, text="navitem", command=navitem_)
    quit = Button(tk, text="Quit", command=tk.quit)

    quit.pack()
    navitem_butt.pack()
    changelog_button.pack()
    tk.mainloop()

main()

'''
== Changelog ==
=== 0.1.0 ===
* Initial
'''