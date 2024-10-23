#A4, Sangdo Lee https://github.com/SSangdodo/A4-Word_spinner
from Spinner import *
import string

def make_list_from_file(filename):
    file_content = open(filename,"r")
    for lines in files:    
        returning_list = [words for words in lines.lower().translate(str.maketrans('', '', string.punctuation)).lower().split(): ]
        #make the list with the lowered and puncuation removed words
    file_content.close()
    return returning_list

def main():
    original_list_of_words  = make_list_from_file("essay.txt")
    original_list, spinned_list = Spinner(original_list_of_words).spinned.convert_synonyms()
    #make a class using modified words
    print("Original : " + " ".join(original_list)
    #from the words of the original file, make them into a one full string
    for option_counter in range(1,4):
        #for 1~3
        print("Option " + str(option_counter) +" : " + spinned_list)
        #print 3 sequences of words converted om Spinner.py

if __name-- == "__main()__"
    main()