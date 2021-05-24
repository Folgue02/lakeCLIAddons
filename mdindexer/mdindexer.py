#!/usr/bin/env python3
import os
from sys import argv
import argparse

def main(): 
    parser = argparse.ArgumentParser()

    parser.add_argument("file", type=str, help="File to read")
    parser.add_argument("-i", "--indentation", type=int,help="Number of spaces for indentantion (default is 2)")
    arguments = parser.parse_args()

    # Define target
    target = arguments.file

    # Define indentation
    indentation = 2 # Default value

    if arguments.indentation:
        indentation = arguments.indentation


    try:
        content = open(target, "r").read()
    except Exception as e:
        print("Cannot read the file due to the following reason: " + str(e))
        return

    result = {}

    for line in content.split("\n"):
        if line.startswith("#"):
            level = 0
            for char in line:
                if char == "#":
                    level += 1

                else:
                    break

            result[line] = level

        else:
            continue
        

    if result == {}:
        print("There isn't anything to index here.")

    else:
        print(f"----- INDEX OF FILE: '{target}'")
        for x in result:
            print(" "*indentation*result[x] + x)

        print(f"----- END")



if __name__ == "__main__":
    main()
