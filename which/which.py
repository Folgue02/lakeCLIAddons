#!/usr/bin/env python3
import os
from sys import platform, argv as a
import argparse



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("executable", help="File to look for.")
    arguments = parser.parse_args()

    parsedPath = os.environ ["PATH"].split(":") if platform != "win32" else os.environ["PATH"].split(";")
    
    result = False
    for path in parsedPath:
        if arguments.executable in os.listdir(path):
            print(f"File found in '{path}'")
            result = True


        else:
            pass

    if not result:
        print(f"File '{arguments.executable}' not found anywhere in the path.")



if __name__ == "__main__":
    main()
