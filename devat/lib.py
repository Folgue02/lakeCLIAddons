from termcolor import colored
import os
from json import loads, dumps, JSONDecodeError
from colorama import init
init()


def error(*args):
    for e in args:
        print(colored("error:", "red"), e)

def warning(*args):
    for e in args:
        print(colored("warning:", "yellow"), e)

def success(*args):
    for e in args:
        print(colored("success:", "green"), e)

def check_installer() -> dict:
    if not os.path.exists("installer.lci"):
        error("There is no installer.lci file.")
        raise FileNotFoundError("There is no installer file in the directory.")

    else:
        return loads(open("installer.lci", "r").read())


def write_installer(content):

    # Avoid parsing dictionaries to the file
    if type(content) == dict:
        content = dumps(content, indent=2)

    if not os.path.exists("installer.lci"):
        error("There is no installer.lci file.")
        raise FileNotFoundError("There is no installer file in the directory.")

    else:
        open("installer.lci", "w").write(content)


