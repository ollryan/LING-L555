import sys

sentence = 0


line = sys.stdin.readline()
while line:
	line = line.strip()
	if line == "":
		line = sys.stdin.readline()
		continue
	print("# sent_id =",sentence) 
	print("# text =",line)
	tokenn = 0

	sentence = sentence + 1
	line = line.replace('.', ' .')
	line = line.replace(',', ' ,')
	line = line.replace('\'', '\' ')
	line = line.replace('(', '( ')
	line = line.replace(')', ' )')
	line = line.replace(';', ' ;')
	line = line.replace(':', ' :')
	line = line.replace('"', ' " ') 
	tokens = line.split(' ')
	#print(tokens)
	for token in tokens:
		if token.strip()=='':
			continue
		tokenn = tokenn + 1
		print('%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_' % (tokenn, token))
	print()
	line = sys.stdin.readline()

