#!/usr/bin/env python3
import os
from sys import argv as a
from termcolor import colored
import argparse

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
        # in the ignore case
        if PARSER.parse_args().ignore:
            # Create a copy
            foo = elements
            elements = []
            for element in foo:
                if element.startswith("."):
                    continue

                else:
                    elements.append(element)


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

    PARSER.add_argument("-p", "--path", default=os.getcwd(), required=False, help="Path to display, if nothing its specified, it will be assigned as the current working directory.")
    PARSER.add_argument("-i", "--ignore", default=False, action="store_true", help="Ignore files and folders that starts with '.'.")

    if not os.path.isdir(PARSER.parse_args().path):
        print("The specified path doesn't exist.")
    else:
        print(os.path.abspath(PARSER.parse_args().path))
        printBranch(1, PARSER.parse_args().path)
    



if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    main()






