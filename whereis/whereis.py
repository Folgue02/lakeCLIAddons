#!/usr/bin/env python3
import argparse
import os
from colorama import init
from termcolor import colored
from lib import *



def look_for_elements(name, origin, type):
    result = [] # It will store the paths of the files found.
    try:
        elements = os.listdir(origin)
    except PermissionError:
        return result

    for element in elements:
        if (os.path.isfile(os.path.join(origin, element)) and type == "file" or type == "both") and element == name:
            result.append(os.path.join(origin, element))

        elif os.path.isdir(os.path.join(origin, element)):

            # Add folders as well
            if  type == "dir" or type == "both" and element == name:
                result.append(os.path.join(origin, element))

            result2 = look_for_elements(name, os.path.join(origin, element), type)

            # Append the results from the other directories
            for r in result2:
                result.append(r)

    return result




def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("file", type=str,help="File to look for")
    parser.add_argument("-o", "--origin", type=str, required=False, default=os.getcwd(), help="Directory where the search will start")
    parser.add_argument("-t", "--type", type=str, required=False, default="both", help="The type of the element to look for. (file, directory or both)")
    arguments = parser.parse_args()

    # Turn the origin path into an absolute path
    arguments.origin = os.path.abspath(arguments.origin)

    if not arguments.type in ["file", "directory", "both"]:
        error("Invalid element type to look for.", "(it can only be 'file/directory/both')")

    elif not os.path.isdir(arguments.origin):
        error(f"The origin directory its not a directory or doesn't exist: '{arguments.origin}'")

    else:
        result = look_for_elements(arguments.file, arguments.origin, arguments.type)


        t = table(["Index", "Name", "Type"])
        for index, x in enumerate(result):
            type = "UNKNOWN"
            if os.path.isfile(x):
                type = "FILE"

            elif os.path.isdir(x):
                type = "DIRECTORY"

            else:
                type = "SYMBOLIC LINK"

            t.addContent([index+1, x, type])

        t.printTable()





if __name__ == "__main__":
    main()


