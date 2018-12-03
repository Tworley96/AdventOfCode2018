import time
from functools import lru_cache

def read_lines():
	with open("input.txt") as file:
		return file.read().splitlines()
lines = read_lines()

@lru_cache(len(lines))
def hammingDistance(str1, str2):
	distance = 0
	for i in range(0,len(str1)):
		if str1[i] != str2[i]:
			distance = distance + 1
	return distance

def commonLetters(str1,str2):
	letters = ""

	for i in range(0,len(str1)):
		if str1[i] == str2[i]:
			letters = letters + str1[i]
	return letters


def splitOnHammingDistance(ids,length):
	if len(ids) == 0 or len(ids) == 1:
		return ""

	newIDSets = {}
	for i in range(0, length):
		newIDSets[i] = []

	baseID = ids[0]

	#split into new sets based on hamming distance
	for id in ids:
		dist = hammingDistance(baseID,id)
		if(dist == 1):
			return commonLetters(baseID, id)
		if dist == length:
			newIDSets[dist - 1].append(id)
		elif dist == 0:
			newIDSets[dist].append(id)
		else:
			newIDSets[dist - 1].append(id)
			newIDSets[dist].append(id)
	for key, idSet in newIDSets.items():
		matchingLetters = splitOnHammingDistance(idSet, length)
		if(matchingLetters != ""):
			return matchingLetters
	return ""

start = time.time()
length = len(lines[0])
letters = splitOnHammingDistance(lines, length)
print(letters)
print(time.time() - start)