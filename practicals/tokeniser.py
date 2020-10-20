import sys

line = sys.stdin.readline()
while line:
	print("#  sent_id= 1") 
	print("#text=",line)

	line = line.replace('.', '. ')
	line = line.replace(',', ' ,')
	line = line.replace('\'', '\' ')
	line = line.replace('(', ' (')
	line = line.replace(')', ' )')
	line = line.replace(';', ' ;')

	tokens = line.split(' ')
	print(tokens)
	for token in tokens:
		print(token)
	line = sys.stdin.readline()

