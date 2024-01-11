import math # We need the logarithmic function to use a smaller scale of values.
infinity = math.inf
symbols = ['.', ';', '?', ',' , '!', ':']

# We read the 100,000 word dictionary and store all the words
# that start with an alphabetic character in a Python Dictionary,
# where the word is the key and the integer denoting its popularity
# is the value. For example: 
# diccioDict['the'] = 1
# diccioDict['of'] = 2
# diccioDict['radiator'] = 68952
# Note: dictionary.txt uses ISO-8859-1 encoding.
with open('dictionary.txt', 'r', encoding='ISO-8859-1') as diccio:

	diccioDict = dict()
	counter = 1
	for line in diccio:
		if(line[0].isalpha()):
			toCopy = line.strip('\n')
			if(toCopy not in diccioDict):
				diccioDict[toCopy] = counter
				counter = counter + 1

# Now we read the 20,000 word dictonary and lookup the popularity of each word
# in the Python Dictionary diccioDict that we just made. If a word exists
# in both diccionary.txt and dictionary2.txt, then we are able to determine
# its popularity and store it in a final Python Dictionary called diccio2Dict.
# Note: dictionary2.txt uses ASCII encoding.
with open('dictionary2.txt', 'r') as diccio2:

	diccio2Dict = dict()
	for line in diccio2:
		if(line[0].isalpha()):
			toCopy = line.strip('\n')
			if(toCopy not in diccio2Dict and diccioDict.get(toCopy) != None):
				diccio2Dict[toCopy] = diccioDict[toCopy]


# We can use a logarithmic scale to avoid dealing with large numbers
# like 82697 in the popularity ranking.
for key, value in diccio2Dict.items():
	diccio2Dict[key] = math.log((value + 1) * math.log(len(diccio2Dict)))
# So the final Python Dictionary looks like
"""
words | popularity  --->  words | popularity
__________________        __________________
the   | 1                 the   |  3.01561
of    | 2                 of    |  3.421083
and   | 3                 and   |  3.70876
to    | 4                 to    |  3.9319
in    | 6                 in    |  4.268380
[...] |                   [...] |
PCB   | 60982             PCB   |  13.340821234
"""

# We find the length of the largest word
# Note: largestWord = 18
largestWord = 0
for key in diccio2Dict:
	if(len(key) > largestWord):
		largestWord = len(key)

# Helper Function
# Gets the optimal option for the initial letters up to index. The optimal option
# has the smaller weight and we are assuming that this weight has been computed for the
# first (index - 1) letters. We return a tuple of the form (minimum weight, length).
# We use this function to build our Dynamic Programming array.
def optimalTuple(string, index, weights):
	begin = max(0, index - largestWord)
	tuples = enumerate(reversed(weights[begin:index]))

	tupleList = list()
	for length, weight in tuples:
		tupleList.append((weight + diccio2Dict.get(string[index - length - 1:index], infinity), length + 1))

	minTuple = (infinity, infinity)
	for pair in tupleList:
		minTuple = min(minTuple, pair)

	return(minTuple)
		
# Dynamic Programming Function
def restoreMissingBlankSpace(file):

    # Load the input file to a string
    fullString = file.read()

    # Before we start, we remove the special symbols from fullString and add
    # them to a list with their respective indices so we can restore them later
    temp = list()
    counter = 0
    for character in fullString:
    	if(character in symbols):
    		temp.append((counter, character))
    		fullString = fullString.replace(character, "")
    	counter = counter + 1

    # We build the Dynamic Programming array of optimal weights
    # The array of weights starts with one 0.
    DPweights = [0]

    # Fill the rest of the array
    for index in range(1, len(fullString) + 1):
        weight, length = optimalTuple(fullString, index, DPweights)
        DPweights.append(weight)

    # Once we have our Dynamic Programming array complete we can
    # use backtracking to generate the string with the minimum weight/maximum popularity.
    result = list()
    index = len(fullString)

    while(index > 0):
        weight, length = optimalTuple(fullString, index, DPweights)
        result.append(fullString[index - length:index])
        index = index - length

    # Now, it's time to put the symbols back.
    # We have counter + 1 inside the if statement because the symbol goes
    # one position after the specific word it's attached to.
    # If the if statement is true we also have to increase the counter
    # because we need to continue right after we put the symbol
    # the final counter + 1 is the normal one we always have
    result = list(reversed(result))
    resultWithSymbols = list()
    counter = 0

    for word in result:
    	for character in word:
    		for index, symbol in temp:
    			if(counter + 1 == index):
    				word = word + symbol
    				counter = counter + 1
    		counter = counter + 1
    	resultWithSymbols.append(word)    


    finalString = ' '.join(resultWithSymbols)

    # Write the finalString to the file result.txt
    with open('result.txt', 'w') as outputFile:
    	outputFile.write(finalString)

    return(outputFile)


# Test the program
with open('test.txt', 'r') as inputFile:
	restoreMissingBlankSpace(inputFile)

