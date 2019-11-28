'''
The code takes a text as an input. It takes the file name of
a text file, reads it and creates a dictionary of unique words.
It keeps count of the frequency of each unique word.
Then, it creates a score based on how similar the
frequency of words appear in each dictionary compared with the
user input text. Then it prints an appropriate message determining
which author it thinks the inputted text is from.

References
https://stackoverflow.com/questions/1024847/add-new-keys-to-a-dictionary

By: Ben
'''
import math

#Functions
#Given function that normalizes letters (takes out punctuation and upper cases).
def normalize(word):
    return "".join(letter for letter in word if letter.isalpha()).lower()

'''
Part 1 and 2 Function
This function creates a dictionary with the word as
the key and the frequency as the value
'''
def get_counts(filename):
    result_dict = {}
    
    #Getting the individual words
    file = open(filename, "r")
    total = 0
    
    for lines in file:
        lines = lines.split()

        for word in lines:

            word = normalize(word)

            if word != "":

                #Adds 1 to the value if the word is already in the dictionary
                if word in result_dict:
                    result_dict[word] = result_dict[word] + 1
                    total = total + 1

                #Adds a new word to the dictionary           
                else:
                    result_dict[word] = 1
                    total = total + 1
                
    result_dict["_total"] = total
    
    file.close()
    return result_dict

#Given function that calculates the score of a single word when given a dictionary.
def get_score(word, counts):
    denominator = float(1 + counts["_total"])
    if word in counts:
        return math.log((1 + counts[word]) / denominator)
    else:
        return math.log(1 / denominator)

'''
This function takes a text and two dictionaries and returns a boolean
'''
def predict(text, williamSDict, janeADict):
    janeScore = 0
    williamScore = 0

    #This splits the text into words
    text = text.split()
    for word in text:

        word = normalize(word)

        if word != "":

            #Calculates the scores of the entire text
            williamScore = williamScore + get_score(word, williamSDict)
            janeScore = janeScore + get_score(word, janeADict)

    #This tells if its by Shakespeare or Jane Austen
    if janeScore > williamScore:
        return True

#Part 3 or 4 Main Program
hamletDict = get_counts("hamlet.txt")
prideDict = get_counts("pride-and-prejudice.txt")
textInput = input("Enter a text: ")

#If the predict returns True, it is Jane Austen while if it's false then its Shakespeare
if predict(textInput, hamletDict, prideDict):
    print("I think that was written by Jane Austen.")
else:
    print("I think that was written by William Shakespeare.")



