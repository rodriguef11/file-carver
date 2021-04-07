#!/usr/bin/env python3
#Programmer:	Fernando Rodriguez
#Program Name:	Lab 3 - Disk Imaging
#File Name:	rodriguef11_lab3.py
#Description:	Program will take a raw image and carve out jpgs and pdfs.
#Class:		CSC 447

#1- Command line arguments
#2- Read in image as raw bytes
#3- Carve by using the provided Header/Footer hex values

import sys				#system exit
from rodriguef11_carve import carve	#carve function

#Print help file
def help():
	print("\n<flag>\t<option>\tdescription")
	print("-h\t\t\t:help file")
	print("-t\t<type>\t\t:file type: jpg or pdf")
	print("-f\t<filename>\t:file name\n") 

#Check for correct command line usage
if len(sys.argv) < 2:
	print("\nUsage: python3 rodriguef11-lab3.py <flag> <option>")
	help()
	sys.exit(0)

#Placeholders for file name and type
file_name = ""
file_type = ""

#Loop through command line arguments and store valid information
#Flags: -h, -t, -f
i = 1
while i < len(sys.argv):
	if sys.argv[i] == "-h":
		help()
		i += 1
	elif sys.argv[i] == "-t":
		try:
			file_type = sys.argv[i+1]
		except IndexError:
			print("File type expected after -t flag")
			sys.exit(0)
		i += 2
	elif sys.argv[i] == "-f":
		try:
			file_name = sys.argv[i+1]
		except IndexError:
			print("File name expected after -f flag")
			sys.exit(0)
		i +=2
	else:
		print("Flag not recognized.")
		sys.exit(0)

#Create timer for runtime
#start timer
#Run carve
carve(file_name, file_type)
#end timer
