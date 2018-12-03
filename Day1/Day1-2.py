
def getFrequency():
	sum = 0
	frequencySet = set([0])
	while(True):
		with open("input1.txt") as data:
			while(True):
				line = data.readline()
				if(line == ''):
					break
				sum = sum + int(line)
				if(sum in frequencySet):
					print(sum)
					return
				else:
					frequencySet.add(sum)
getFrequency()
