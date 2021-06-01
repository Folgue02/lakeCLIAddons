#!/usr/bin/env python3
import argparse
import os
from colorama import init
init()
from termcolor import colored
from result import str_search, match
from pathlib import Path
import mimetypes
from copy import deepcopy as dp

def error(*args):
    for a in args:
        print(f"{colored('error', 'red')}: {a}")


def display_match(match:match, lines:bool, file_name:bool):
    # Function in charge of displaying the matches found in the files.
    line_buffer = ""

    if lines:
        line_buffer += f"[{match.line_num}]"

    if file_name:
        line_buffer += colored(os.path.join(".", Path(match.file)), "magenta")

    print((line_buffer + " " if line_buffer!="" else "") + match.embed_result())


def iterate_dirs(arguments:argparse.ArgumentParser) -> None:
    # Iterates through directories and search for the string through them
    try:
        elements = os.listdir(arguments.target)
    except Exception:
        error("Cannot inspect folder: " + arguments.target)
        return

    for x in elements:
        
        # Read file
        if os.path.isfile(os.path.join(arguments.target, x)):
            try:
                result = str_search(arguments.pattern, os.path.join(arguments.target, x), case_sensitive=arguments.case_sensitive)
            except UnicodeDecodeError:
                if not arguments.ignore_error:
                    error(f"Cannot decode file '{os.path.join(arguments.target, x)}'")
                    continue

                else:
                    continue

            for r in result.matches:
                display_match(r, arguments.lines, os.path.join(arguments.target, x))

        # Recursion
        elif os.path.isdir(os.path.join(arguments.target, x)):
            # Create a copy of the arguments
            copy = dp(arguments)
            copy.target = os.path.join(arguments.target, x)

            # Do the same with another directory
            iterate_dirs(copy)

        else:
            print(os.path.exists(os.path.join(arguments.target, x)))

def main():
    parser = argparse.ArgumentParser()
    
    # Arguments
    parser.add_argument("pattern", type=str, help="Pattern to search for")
    parser.add_argument("target", type=str, help="Target to look for the pattern")
    parser.add_argument("-l", "--lines",  action="store_true", help="Display line numbers")
    parser.add_argument("-n", "--filename",  action="store_true", help="Display file name")
    parser.add_argument("-i", "--ignore-error", action="store_true", help="If enabled, avoids displaying errors")
    parser.add_argument("-c", "--case-sensitive", action="store_true", help="Enables case sensitive search")

    arguments = parser.parse_args()

    # Check target existence
    if not os.path.exists(arguments.target):
        error(f"Path '{os.path.abspath(arguments.target)}' doesn't exist.")

    else:
        # Check single file
        if os.path.isfile(arguments.target):
            try:
                result = str_search(arguments.pattern, arguments.target, case_sensitive=arguments.case_sensitive)
            except UnicodeDecodeError:
                error("Cannot decode file '{arguments.target}'.")

            for r in result.matches:
                display_match(r, arguments.lines, arguments.filename)

        
        elif os.path.isdir(arguments.target):
            iterate_dirs(arguments)

        else:
            error("Invalid file type.")


if __name__ == "__main__":
    main()


