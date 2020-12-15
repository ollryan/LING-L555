import sys

fd = open('hung.conllu')
freq = {}  #frequency list for parts of speech
form_tag = {} #matrix to store correspondences form as a token and part of speech
forms = {}
y = 0 #counter for total number of tokens
for line in fd.readlines():
	if '\t' not in line:
		continue
	#print(line)
	x = line.split()
	y = y + 1
	pos = x [3]
	if pos not in freq:
		freq[pos] = 0  #add pos to the feq list with value 0
	freq[pos] = freq[pos] + 1
	token = x [1]
	if token not in forms:
		forms[token] = 0  #add pos to the feq list with value 0
	forms[token] = forms[token] + 1
	if token not in form_tag:
		form_tag[token] = {}
	if pos not in form_tag[token]:
		form_tag[token][pos] = 0
	form_tag[token][pos] = form_tag[token][pos] + 1
	#print(x)
for pos in freq:
	print('%.4f\t%d\t%s\t%s' % (freq[pos]/y, freq[pos] , pos, '_'))#P, count, tag, form
for token in form_tag:
	for tag in form_tag[token]:
		print('%.4f\t%d\t%s\t%s' % (form_tag[token][tag]/forms[token], form_tag[token][tag] , tag, token))#P, count, tag, form
		
#print(freq)
#print(forms)
#print(y)



