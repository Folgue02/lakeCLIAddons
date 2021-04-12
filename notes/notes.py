#!/usr/bin/env python3
import os
from sys import argv as a


NOTE_FILE = os.path.join(os.getcwd(), "notes.txt")

def listNotes():
    for index, line in enumerate(open(NOTE_FILE, "r").read().split("\n")):
        print(f"[]")



def main():
    if not os.path.isfile(NOTE_FILE):
        print("The note file doesn't exist! Creating it now...")
        open(NOTE_FILE, "w").write("")
        print("File created!")

    # Arguments
    if a == []:
        


if __name__ == "__main__":
    main()


