#A4, Sangdo Lee https://github.com/SSangdodo/A4-Word_spinner
from Spinner import *
import string
def make_list_from_file(filename):
    file_content = open(filename,"r")
        returning_list = [words for words in lines.lower().translate(str.maketrans('', '', string.punctuation)).lower().split(): ]
        #make the list with the lowered and puncuation removed words
    file_content.close()
    return returning_list
