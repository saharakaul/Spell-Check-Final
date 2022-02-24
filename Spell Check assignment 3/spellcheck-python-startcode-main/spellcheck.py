# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time
#Binary Search Function Code
def binary_search(an_array, item):
    lower_index = 0
    higher_index = len(an_array) - 1

    while lower_index <= higher_index:
        middle_index = (higher_index + lower_index) // 2
        # print(lower_index, middle_index, higher_index)
        if item == an_array[middle_index]:
            return middle_index

        elif item < an_array[middle_index]:
            higher_index = middle_index - 1
        elif item > an_array[middle_index]:
            lower_index = middle_index + 1
    return -1
#Linear Search Function
def linear_search(an_array, item):
   for i in range(len(an_array)):
       if an_array[i] == item:
           return i
   return -1


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])
    #Main Loop
    loop = True
    while loop:
        #Print Main Menu
        print("""\nMain Menu
        1:Spell Check a Word (Linear search
        2: Spell Check a Word (Binary Search)
        3: Spell Check Alice In Wonderland (Linear Search)
        4: Spell Check Alice In Wonderland (Binary Search)
        5: Exit
        """)
        #Get User Instruction
        Number = int(input("Please Enter the command: "))
        #Linear Dictionary Search
        if Number == 1:
            #Get User Word
            item = input("Please Enter the word you would like to search for: ")
            print("Linear Search Starting...")
            #Timer
            start = time.perf_counter()
            if item in dictionary:
                #Call function
                print(linear_search(dictionary, item))
            else:
                print("Sorry " + item + " was not found in the dictionary")
            #Check time
            print("It takes " + str(time.perf_counter() - start) + " to run this code")
        #Binary Search Function in Dictionary
        elif Number == 2:
            #Get User Input
            item = input("Please Enter the word you would like to search for: ")
            print("Binary Search starting...")
            #Start timer
            start = time.perf_counter()
            if item in dictionary:
                #Call function
                print(binary_search(dictionary, item))
            else:
                print("Sorry " + item + " was not found in dictionary")
            #Check Time Taken
            print("It takes " + str(time.perf_counter() - start) + " to run this code")
        #Alice in Wonderland linear Search
        elif Number == 3:
            #Define wordsNotFound variable
            wordsNotFound = 0
            print("Linear Search starting...")
            #Start timer
            start = time.perf_counter()
            for i in aliceWords:
                #Call function
                if linear_search(dictionary, i.lower()) == -1:
                    wordsNotFound += 1
            #Check time taken
            print("It takes " + str(time.perf_counter() - start) + " to run this code")
        #Binary Search Alice in Wonderland
        elif Number == 4:
            print("Binary Search Starting...")
            #Set wordsNotFound to zero
            wordsNotFound = 0
            start = time.perf_counter()
            for i in aliceWords:
                #Call function
                if binary_search(dictionary, i.lower()) == -1:
                    wordsNotFound += 1
            print(wordsNotFound)
            #Check time taken
            print("It takes " + str(time.perf_counter() - start) + " to run this code")
        #Exit Program
        else:
            loop = False
            print("Program Ended")
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# Call main() to begin program
main()



