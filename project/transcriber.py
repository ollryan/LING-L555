import sys, re

#variable to hold transcription lookup
letter = {}

#load in transcription table from file
fd = open('oldhung.tsv')  #opens the file
for line in fd.readlines(): #read each line of the file
	#print(line)
	row = line.split() #splitting line into list: ortho character and ipa character
	#print(letter)
	#print(row)
	if len(row)== 0:
		continue
	if line [0]== '#':
		continue
	if row [1].count('<') == 0:
		letter[row[0].title()] = row[1].title()
	letter[row[0]] = row[1]
			
print(letter)

#read in the input line by line
line = sys.stdin.readline()
while line:
	form = line
	for char in letter:
		form = re.sub(char, letter[char],form) 
	print(form)
	line = sys.stdin.readline()
	
#look up each of the characters in the lookup table

#code for issues mentioned in oldhung?

#replace?

#printout the line with transcription
