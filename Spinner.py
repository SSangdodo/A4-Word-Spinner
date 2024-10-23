#A4 Sangdo Lee https://github.com/SSangdodo/A4-Word_spinner
from random import *

def make_list_from_file(filename):
    file_content = open(filename,"r")
    
    returning_list = [lines for lines in file_content.strip("\n").strip(" ")]
    #make the list from the lines in file content, removing the lines with the tab and spaces
    
    return returning_list

def make_response_dictionary(response_list):
    keyword_and_response = {}

    for items in response_list:
        keyword,synonyms = items.split(":")
        #split the keyword section and synonym section
        keyword_and_response[keyword] = synonyms.split(",")
        #store the key and synonyms into a dictonary
    
        return keyword_and_response