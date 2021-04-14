#!/usr/bin/env python3
import argparse
import os
from termcolor import colored
from colorama import init
init()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="File where to search the string from.", type=str)
    parser.add_argument("targetString", help="String to search.", type=str)

    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print(f"The file '{args.file}' doesn't exist.")

    else:
        # Search for the string in the content of the file

        try:
            content = open(args.file, "r").read().split("\n") # Split the file in lines
        
        except PermissionError:
            print(colored(f"You don't have permissions to read this file: '{args.file}'", "red"))

        locations = []

        for index, line in enumerate(content):
            if args.targetString in line:
                locations.append([index+1, line])

        for x in locations:
            print(f"[{'0'*(len(str(len(content))) - len(str(x[0])))}{x[0]}]  {x[1].replace(args.targetString, colored(args.targetString, on_color='on_green'))}")
        

        if locations == []:
            print(f"[{colored('X', 'red')}]" + f"'{args.targetString}' doesn't appear in the file.")


if __name__ == "__main__":
    main()
