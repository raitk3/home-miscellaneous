"""
Disclaimer:
Written by a friend who knows much more about coding than I do.
"""

import csv
import re

# Functions that are used by the main thread (?)

def read_file(filename):
    """
    Read in data from file.
    
    Input: File name
    Output: List of rows as lists
    """
    
    data_from_file = []
    with open(filename) as csv:
        reader = csv.readlines()
        for row in reader:
            data_from_file.append(row.strip().split(";"))
    return data_from_file


def write_new(data: list):
    """
    Write a new .csv file.

    Input: Data as a list
    Output: None
    """

    with open("new_data.csv", "w") as csv:
        for row in data:
            csv.write(";".join(row) + "\n")
    

def parse_data(data):
    """
    Parse the data.

    Add two new columns with the sentence type and the next word if applicable.
    
    Input: List of rows
    Output: List of rows
    """
    replace_dict = {
                    "s": "is/was",
                    "re": "are/were"
                    }
    for i, row in enumerate(data):
        if i == 0:
            row += ["Sentence type", "Next word"]
        else:
            #Determine sentence type and add it to the list
            if "?" in row[2]:
                row.append("Quest.")
            elif "!" in row[2]:
                row.append("Excl.")
            elif "." in row[2]:
                row.append("Decl.")
            else:
                row.append("Frag.")
            
            #Find next word
            next_word = re.search(r"(\w+)", row[2])
            if next_word != None:
                if next_word[1] in replace_dict:
                    next_word = replace_dict[next_word[1]]
                else:
                    next_word = next_word[1]
            else:
                next_word = "NA"
            #Add next word to the list
            row.append(next_word)

    return data


#Main thread (?). It starts running from here.
if __name__ == '__main__':
    data = read_file("data.csv")
    #print(*data, sep="\n")
    data = parse_data(data)
    write_new(data)
