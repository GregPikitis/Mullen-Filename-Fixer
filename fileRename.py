# !/usr/bin/python
'''
Programmers: Hunter Harris, Matthew Griffin

Description: A program that formats a file name

IDEAS:
- Add more file formats
- Add function to see/alert user if old dir is empty
- Add file that holds things like new/old dir, last name
- Name formatting(in case of bad user input)

'''
# Importing stuff
try:
        import os
        import shutil
        import sys

except ImportError:
        print("Python " + str(sys.version()) + "is not installed correctly. Try re-installing.")

DEBUG = False

class Rename:
        def __init__(self):
                # Making some basic variables, olddir, newdir, and lastName
                olddir = "old"
                newdir = "new"
                lastName = input("What is your last name [i.e. 'Harris']?: ") # Getting last name

                # If lastName has any other characters than letters
                if(lastName.isalpha() == False):
                        print("Bad User input")
                        sys.exit(0)

                # Formatting lastName
                lastName = lastName.upper()
                lastName = lastName + "_"

                for filename in os.listdir(olddir):
                        print ("FOUND FILE: " + filename) # Printing the name[s] of the file[s] in the 'old' dir
                        print("---Renaming file " + filename + "...")    
                                
                        # If the filename ends in a recognizable format
                        if(filename.endswith(".docx")):
                                shutil.copyfile(olddir + "/" + filename, newdir + "/" + filename) # Copying the old file to the new dir
                                os.rename(newdir + "/" + filename, newdir + "/" + lastName + filename) # Renaming the file

                                 # If 'DEBUG' is true
                                if(DEBUG):
                                        print("Last Name: " + str(lastName))
                                        print("File Name: " + str(filename))

                        print("File renaming done!") # When the program is done

if(__name__ == "__main__"):
        rename = Rename()
