
with open("input.txt") as data:
	sum = 0
	while(True):
		line = data.readline()
		if(line == ''):
			print(sum)
			break
		sum = sum + int(line)
