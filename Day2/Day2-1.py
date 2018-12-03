with open("input.txt") as file:
	count2 = 0
	count3 = 0
	while(True):
		line = file.readline()
		if(line == ''):
			break
		twoFlag = 0
		threeFlag = 0
		for char in line:
			count = line.count(char)
			if(count == 2):
				twoFlag = 1
			if(count == 3):
				threeFlag = 1
		count2 = count2 + twoFlag
		count3 = count3 + threeFlag
	print(count2 * count3)
