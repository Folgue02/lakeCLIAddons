#!/usr/bin/env python3
import os
from sys import argv as a
from termcolor import colored
del a[0]

def printBranch(level, path, indentation=4):
    elements = []
    baseString = " " + " "*indentation*level 
    try:
        elements = os.listdir(path)
    except PermissionError:
        print(baseString + colored("Permission denied", on_color="on_red"))
        return

    if elements ==  []:
        print(baseString + colored("Empty", "red"))

    else:
        for index, element in enumerate(elements):
            string = baseString
            if os.path.isdir(os.path.join(path, element)):
                string += "╚" + colored(element, "green")
                print(string)
                printBranch(level+1, os.path.join(path, element), indentation=indentation)
            
            else:
                string += ("╠" if index != len(elements)-1 else "╚") + element
                print(string)


def main():
    targetPath = os.getcwd()
    if a != []:
        targetPath = a[0]

    if not os.path.isdir(targetPath):
        print("The specified path doesn't exist.")
    else:
        print(targetPath)
        printBranch(1, targetPath)
    



if __name__ == "__main__":
    main()






