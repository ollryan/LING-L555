import sys

#variable to hold transcription lookup table
letter = {}

#load in transcription table from a file
fd = open('lookup.tsv') #opens the file
for line in fd.readlines(): #read each line of the file
	print(line)
	row = line.split() #splitting line into list: ortho character and ipa character
	print(letter)
	print(row)
	if len(row)== 0:
		continue
	#populate variable letter with values from the row
	letter[row[0]] = row[1]
print(letter)
#read in the input line by line
line = sys.stdin.readline()
while line:

	#if the line is a comment, print it out
	if '\t' not in line:
		print(line)
		line = sys.stdin.readline()
		continue
	#take the 1st column and look up each of the characters in the lookup table
	row = line.split()
	form = row[1]
	for char in form:
		if char not in letter:
			continue
		form = form.replace(char, letter[char]) 
	print('%s\t%s\t_\t_\t_\t_\t_\t_\t_\tIPA=%s' % (row[0],row[1],form))
	#2   realidat    _   _   _   _   _   _   _   IPA=realidat
	#printout the line with transcription
	line = sys.stdin.readline()
	
