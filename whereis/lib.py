

def error(*args):
    for x in args:
        print(colored("error: ", "red") + x)



class table:
    def __init__(self, rowTitles:list, separator:str=" "):
        self.rowTitles = rowTitles
        self.content = []
        self.separator = separator



    def printTable(self):
        # Print the titles of the rows

        # Turn all rows into string lists
        for row in range(len(self.content)):
            for col in range(len(self.content[row])):
                self.content[row][col] = str(self.content[row][col])

        # Contains the width of each column
        widths = []
        for col in range(len(self.rowTitles)):

            # Default value for the width of the column
            colWidth = len(self.rowTitles[col])

            # Iterate through the entire column
            for row in range(len(self.content)):
                if len(self.content[row][col]) > colWidth:
                    colWidth = len(self.content[row][col])

            widths.append(colWidth)

        # Print the table

        # Function to save time repeating code
        # Creates a string with the content of a column and the filling spaces
        createElement = lambda element, w: element + " "*(w - len(element))

        # Start with the column titles
        for index in range(len(self.rowTitles)):
            print(createElement(self.rowTitles[index], widths[index]), self.separator, end="")
        print()

        # Print the underline
        for index in range(len(self.rowTitles)):
            print("="*widths[index], self.separator, end="")
        print()

        # Print the content
        for row_index in range(len(self.content)):
            for col_index in range(len(self.content[row_index])):
                print(createElement(self.content[row_index][col_index], widths[col_index]), self.separator, end="")

            print() # Jumpline after each row printed

    def addContent(self, newContent:list):
        # Adds a row of content
        # The length of the list must be as long as the rowTitles length

        if len(newContent) != len(self.rowTitles):
            raise ValueError(f"The new row must contain '{len(self.rowTitles)}', instead, the new content had a length of '{len(self.rowTitles)}'")

        else:
            self.content.append(newContent)


if __name__ == "__main__":
    print("This is not meant to be executed, just imported.")
