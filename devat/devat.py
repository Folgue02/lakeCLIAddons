#!/usr/bin/env python3
import argparse
from sys import platform, argv as a
from json import loads, dumps, JSONDecodeError
import os
from lib import *
import subprocess

TEMPLATE = {'referenceCommand': '', 'entryFile': '', 'help': {'description': '', 'usage': {}}, 'files': {}, 'directories': [], 'version': 1.0}

def main():
    # Parse the arguments
    parser = argparse.ArgumentParser()

    # Define the arguments
    parser.add_argument("-n", "--new", type=str, metavar="", help="Create a new project")
    parser.add_argument("-a", "--add", type=str, metavar="", help="Add a file to the project")
    parser.add_argument("-A", "--add-dir", type=str, metavar="", help="Add a directory to the project")
    parser.add_argument("-r", "--remove", type=str, metavar="", help="Remove a file from the project")
    parser.add_argument("-R", "--remove-dir", type=str, metavar="", help="Remove a directory from the project")
    parser.add_argument("-x", "--run", action="store_true", default=False, help="Tries to run the project")
    parser.add_argument("-c", "--check", action="store_true", default=False, help="Checks project integrity")
    parser.add_argument("-s", "--show", action="store_true", default=False, help="Shows the current configuration of the project.")
    arguments = parser.parse_args()

    if arguments.new:
        new(arguments.new)

    elif arguments.add:
        add(arguments.add, "file")

    elif arguments.add_dir:
        add(arguments.add_dir, "dir")

    elif arguments.remove:
        remove(arguments.remove, "file")

    elif arguments.remove_dir:
        remove(arguments.remove_dir, "dir")

    elif arguments.run:
        run()

    elif arguments.check:
        check()

    elif arguments.show:
        show()

    else:
        parser.print_help()


def new(proj_name):
    print(f"Creating project '{proj_name}'...")

    # Check if the folder already exists.
    if os.path.exists(proj_name):
        error(f"The file/folder already exists: '{proj_name}'")

    # Create the environment
    try:
        os.mkdir(proj_name)
    except Exception as e:
        error(f"Cannot create project folder due to the following reason: '{e}'")
        return

    # Create file environment
    copy_template = TEMPLATE
    copy_template["referenceCommand"] = proj_name

    try:
        open(os.path.join(proj_name, "installer.lci"), "w").write(dumps(TEMPLATE, indent=2))
    except Exception as e:
        error(f"Couldn't create installer due to the following error: '{e}'", "Couldn't create the project.")
        return

    success(f"Project '{proj_name}' has been created.")

def add(target_file, target_type):
    content = check_installer()

    # Directory
    if target_type == "dir":

        # Check if the folder already exists in the installer file
        if target_file in content["directories"]:
            error(f"Folder '{target_file}' is already added to the installer file.")
        else:
            content["directories"].append(target_file)

    # File
    elif target_type == "file":
        # Check if the file its already in the installer file
        if target_file in content["files"]:
            error(f"File '{target_file}' already exists in the installer file.")

        else:
            content["files"][target_file] = target_file

    # Save content
    write_installer(content)

def remove(target_file, target_type):
    content = check_installer()

    # File
    if target_type == "file":

        # Check if the file exists in the installer file
        if not target_file in content["files"]:
            error(f"File '{target_file}' doesn't exist in the installer file.")

        else:
            del content["files"][target_file]

    elif target_type == "dir":
        if not target_file in content["directories"]:
            error(f"Directory '{target_file}' doesn't exist in the installer file.")

        else:
            for index, d in enumerate(content["directories"]):
                if d  == target_file:
                    del content["directories"][index]
                else:
                    continue


    write_installer(content)

def run():
    content = check_installer()

    file_to_run = content["entryFile"]

    if not os.path.isfile(file_to_run):
        error(f"The entry file doesn't exist. ('{file_to_run}')")

    else:
        # Run
        success(f"Executing project '{content['referenceCommand']}'...")
        result = os.system(f"./{file_to_run}")

        # Project failed
        if result != 0:
            error(f"Project execution failed, error code: '{result}' ")

        else:
            success("The project execution as succesful!")

def check():
    content = check_installer()

    for prop in TEMPLATE:
        if prop not in content:
            warning(f"Installer file lacks a property. ('{prop}')")
        else:
            continue

    # Check elements of the project

    # Check the files
    for f in content["files"]:
        if not os.path.isfile(f):
            warning(f"File in the installer file doesn't exist in the filesystem. ('{f}')")

        else:
            pass

    # Check the folders
    for d in content["directories"]:
        if not os.path.isdir(d):
            warning(f"Directory in the installer file doesn't exist in the filesystem. ('{d}')")

        else:
            continue

    success(f"Project '{content['referenceCommand']}' was checked, see the results above.")

def show():
    content = check_installer()

    try:
        print(f"""Project name:
    {content['referenceCommand']}

Project version:
    {content['version']}

Project entry file:
    {content['entryFile']}

Project help object:
    Project description:
        {content['help']['description']}

    Project usage examples:
        {content['help']['usage']}\n""")
        # Project elements
        print("Project files:")

        if content["files"] == {}:
            print(colored("    Empty", "red"))

        else:
            for f in content["files"]:
                print(" "*4 + f + " -> " + content["files"][f])

        print("\nProject directories")

        if content["directories"] == []:
            print(colored("    Empty", "red"))

        else:
            for d in content["directories"]:
                print(" "*4 + d)

    except KeyError:
        error("Seems like installer file lacks some property, run a 'devat --check' to check which properties its lacking and fix it.")



if __name__ == "__main__":
    main()

