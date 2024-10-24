#A4 Sangdo Lee https://github.com/SSangdodo/A4-Word-Spinner
from random import *
def make_list_from_file(filename):
    file_content = open(filename,"r")
    returning_list = []
    for lines in file_content:
        returning_list.append(lines.strip("\n").strip(" "))
        #extract space and tabs from the lines and add in a list
    file_content.close()
    return returning_list

def make_response_dictionary(response_list):
    keyword_and_response = {}

    for items in response_list:
        keyword,synonyms = items.split(":")
        #split the keyword section and synonym section
        keyword_and_response[keyword] = synonyms.split(",")
        #store the key and synonyms into a dictonary
    return keyword_and_response

class Spinner():
    def __init__(self,file_words):
            self.file_words_list = file_words
            self.synonyms_data = make_response_dictionary(make_list_from_file("synonyms-simplified.txt"))
    
    def return_original_str(self):
        return " ".join(self.file_words_list)
    
    def convert_synonyms(self):
        returning_list = []
        for words in self.file_words_list:
            if self.synonyms_data.get(str(words),1) != 1 and randint(1,2) == 2:
                # if the word exist within synonym dictionary and if it meets the 50% chance of changing the words
                returning_list.append(self.synonyms_data[words][randint(0,len(self.synonyms_data[words])-1)])
                #append to the returning list, from random synonyms of the specified key
            else:
                returning_list.append(words)
                #no match of synonym or 50% of unchanged words

        return " ".join(returning_list)
    