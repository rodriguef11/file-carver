#Programmer:	Fernando Rodriguez
#Program Name:	Lab 3 - Carve
#File Name:	rodriguef11_carve.py
#Description:	#1- Read in image as raw bytes
		#2- Carve by using the provided Header/Footer hex values
#Class:		CSC-447-001-Cyber Security Concepts

import sys

#Carve image into unique files of specified <type>
def carve(file_name, file_type):
	#Header and Footer information based on file type
	if file_type == "jpg":
		header = b'\xff\xd8\xff'
		footer = b'\xff\xd9'
		extension = ".jpg"
	elif file_type == "pdf":	
		header = b'\x25\x50\x44\x46'
		footer = b'\x45\x4f\x46\x0a'
		extension = ".pdf"
	else:
		print("Invalid file type")
		sys.exit(0)

	#Open file
	try:
		in_file = open(file_name, "rb") #(Check out "with open")
	except IOError: #for file open error
		print("File not found.")
		sys.exit(0)

	header_list = []		#list of header starting indices
	footer_list = []		#list of footer ending indicies
	offset = 0			#offset of line traversal

	#Traverse file to find header and footer indicies
	for line in in_file:
		#Search for header index and add to list if found
		start_index = line.find(header)
		if(start_index is not -1):
			header_list.append(start_index + offset)
		#Seach for footer index and add to list if found
		#Storing index after entire footer byte combination
		end_index = line.find(footer)	
		if(end_index is not -1):
			end_index += len(footer)
			footer_list.append(end_index + offset)
		offset += len(line)

	#Check if header is paired with invalid footer
	x = 0
	while x < len(header_list):
		if header_list[x] > footer_list[x]:
			del footer_list[x]
		else:
			x += 1

	#Print header and footer indicies
	#print(len(header_list), header_list)
	#print(len(footer_list), footer_list)
	
	#Create files based on each header and footer
	for x in range(0, len(header_list)):
		in_file.seek(header_list[x])
		data = in_file.read(footer_list[x]-header_list[x])
		out_fileName = "file" + str(x) + extension
		out_file = open(out_fileName, "wb")
		out_file.write(data)
		out_file.close()

	#Cleanup
	in_file.close()	
