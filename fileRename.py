# !/usr/bin/python
#
# Programmers: Hunter Harris, Matthew Griffin
#
# Description: A program that renames a file for our English teacher, Mrs.Mullen-Barnett
#
# Importing stuff
try:
	import os
	import shutil

except ImportError:
	print("Python is not installed correctly. Try re-installing.")

class Rename:
	def __init__(self):
		# Making some basic variables, olddir, newdir, and lastName
		olddir = "/home/matthew/Documents/Python/Mullen-Filename-Fixer/old"
		newdir = "/home/matthew/Documents/Python/Mullen-Filename-Fixer/new"

		# Getting the last name, and editing the name a bit	
		lastName = raw_input("What is your last name [i.e. 'Harris']?: ")
		lastName = lastName.upper()
		lastName = lastName + "_"

		for filename in os.listdir(olddir):	
			print ("FOUND FILE: " + filename) # Printing the name[s] of the file[s] in the 'old' dir
			print("--Renaming file " + filename + "...")	
	
			# If the filename ends in '.docx' (MS Word)
			if filename.endswith(".docx"):
        			shutil.copyfile(olddir + "/" + filename, newdir + "/" + filename) # Copying the old file to the new dir
        			os.rename(newdir + "/" + filename, newdir + "/" + lastName + filename) # Renaming the file
			print("FILE RENAMING DONE!")

if(__name__ == "__main__"):
	rename = Rename()
