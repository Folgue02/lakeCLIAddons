import os
from colorama import init
from termcolor import colored
init() # Colorama


class match:
    def __init__(self, whole_line:str, line_num:int, pattern:str, file:str):
        self.whole_line = whole_line
        self.line_num = line_num
        self.pattern = pattern
        self.file = file

    def embed_result(self, color="green"):
        return self.whole_line.replace(self.pattern, colored(self.pattern, color))



class str_search:
    def __init__(self, pattern, target_file, case_sensitive=False):
        self.pattern = pattern
        self.target_file = target_file
        self.case_sensitive = case_sensitive

        if not os.path.exists(self.target_file):
            raise FileNotFoundError(f"File '{self.target_file}' doesn't exist.")
    
        # Read file
        self.target_content = open(self.target_file, "r").read()
        self.matches = []

        self.get_matches()


    def get_matches(self) -> dict: 
        # Finds the matches of a pattern compared to the lines to an specified file.
        # Returns a dictionary with the matches
        for index, line in enumerate(self.target_content.split("\n")):
            if (self.pattern if self.case_sensitive else self.pattern.upper()) in (line if self.case_sensitive else line.upper()):
                self.matches.append(match(line, index+1, self.pattern, self.target_file))

            else:
                continue

