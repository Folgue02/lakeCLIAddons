#!/usr/bin/env python3
import os
from sys import platform, argv as a
from getpass import getuser
del a[0]

__version__ = 1.0



NOTE_FILE = os.path.join(f"C:\\Users\\{getuser()}\\" if platform == "win32" else f"/home/{getuser()}/", "notes.txt")

def listNotes():
    noteContent = open(NOTE_FILE, "r").read().split("\n")


    if noteContent == [""]:
        print("The note file it's empty.")

    else:
        for index, line in enumerate(noteContent):
            print(f"[ {'0'*(len(str(len(noteContent)))-len(str(index+1)))}{index+1} ]: {line}")


def removeNote(index):
    content = open(NOTE_FILE, "r").read().split("\n")

    if index-1 > len(content)-1 or index < 0:
        print("The index its out of range!")

    else:
        del content[index-1]
        open(NOTE_FILE, "w").write("\n".join(content))


def addNote(note):
    oldContent = open(NOTE_FILE, "r").read() 
    open(NOTE_FILE, "w").write(oldContent + ("\n" if oldContent != "" else "") + note)

def main():
    if not os.path.isfile(NOTE_FILE):
        print("The note file doesn't exist! Creating it now...")
        open(NOTE_FILE, "w").write("")
        print("File created!")

    # Arguments
    if a == []:
        listNotes()        

    else:
        command = a[0]

        if command == "list":
            listNotes()

        elif command == "add": # Should i do something about inserting a note in a place of the list?
            if len(a) < 2:
                print("You must specify the note to add.")

            else:
                addNote(" ".join(a[1:]))
        
        elif command == "remove":
            if len(a) < 2:
                print("You must specify the index of the note.")

            else:
                try:
                    index = int(a[1])

                except:
                    print("You must specify an integer as index for note to remove.")
                    return

                removeNote(index)

if __name__ == "__main__":
    main()


