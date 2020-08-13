#insert seg0001 seg002 between lines in text
import sys
import re

#open file using open file mode
fp1 = open(sys.argv[1], "r", encoding='utf-8') # Open file on read mode -- input file
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

#open file using open file mode
outfile = re.sub(r'.txt','_template.txt', sys.argv[1])
fp2 = open(outfile, "w", encoding='utf-8') # Open file on write mode -- extra file


i = 1
out = []
extra = []
for line in lines:


	line = re.sub(r'^ ','', line)
	line = re.sub(r' $', '', line)
	line = re.sub(r' +', ' ', line)\

	if(line == ""):
		continue

	line = re.sub(r'([\u0900-\u097F ])([?!])\s*(?=[\u0900-\u097FA-Za-z])', r"\1\2\n", line)
	line = re.sub(r'([\u0964])([\)\'\"])', r"\1PLACEHOLDER1\2", line)
	line = re.sub(r'[\u0964]\s*', "\u0964\n", line)

	line = re.sub(r'\nPLACEHOLDER1', '', line)

	seg_template = "\"SEG" + "{0:03}".format(i) +"\""
	i = i + 1

	line = re.sub(r'\n\n','\n', line)

	out.append(seg_template)
	out.append(line)
	#print(seg_template)
	#print(line)

o = '\n'.join([str(elem) for elem in out]) 
o = re.sub(r'\n\n','\n', o)
print(o)

out = o.split("\n")
for l in out:
	if(re.search(r'SEG', l, flags=re.IGNORECASE)):
		fp2.write(l + "\n")
	elif(re.search(r'^[^\u0900-\u097F]+$', l )):
		fp2.write(l + "\n")
	else:
		fp2.write('\n')