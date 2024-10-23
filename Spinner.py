#A4 Sangdo Lee https://github.com/SSangdodo/A4-Word_spinner
from random import *
def make_list_from_file(filename):
    file_content = open(filename,"r")
    returning_list = []
    for lines in file_content:
        returning_list.append(lines.strip("\n").strip(" "))
        #extract space and tabs from the liens
    return returning_list
