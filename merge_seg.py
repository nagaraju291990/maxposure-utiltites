#insert seg0001 seg002 between lines in text
import sys
import re

#open file using open file mode
fp1 = open(sys.argv[1], "r", encoding='utf-8') # Open file on read mode -- input file
lines = fp1.read()#.split("\n") # Create a list containing all lines
fp1.close() # Close file

lines = re.sub(r'\"SEG\d+\"', "SEG",lines)
lines2 = lines.split("SEG")
#print(lines)
out = []
for line in lines2:
	line = re.sub(r'\n'," ", line)
	out.append(line)

for o in out:
	o = re.sub(r'^ ', "", o)
	if(o != ""):
		print(o)