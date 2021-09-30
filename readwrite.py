#readwrite.py
#This file holds all the necessary functions for reading the points from a text file of a specific type
#and writing the results to another file.

#read_txt function you input a file and it parses it into an array
from datetime import datetime
# Import the os module 
import os

#read_txt function reads an input file and parses it into an array it will return
def read_txt(filename):
    print("Reading File...")

    #try to read file
    try:
        # get current working directory and add folder and filename to current working directory path 
        cwd = os.getcwd() + '/test_txt_files/' + filename
        print(cwd)
        inputfile = open(cwd, 'r')
        Lines = inputfile.readlines()
        data_array = []
        
        for line in Lines:
            data_array.append(line.strip())
        inputfile.close()
    except FileNotFoundError:
        #throw error if the file does not exist and quit the program
        print("File does not exist!")
        quit()
    return data_array
    

#write_txt function takes in an input string and saves it to a txt file with current date and time 
def write_txt(result):
    from datetime import datetime

    outputfilename = "output/" + datetime.now().strftime("%m-%d-%Y_%H:%M:%S") + "_results.txt"

    try:
        f= open(outputfilename, "w+")
        f.write(result)
        f.close()
        print("\nResults created in file: " + outputfilename)
    except:
        print("Failed to create file!!")