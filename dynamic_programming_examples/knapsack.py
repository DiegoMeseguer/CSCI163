#helper functions
def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

def printh(table):
	for row in table:
		rowstring = ""
		for column in row:
			rowstring = rowstring + str(column) + " "
		print(rowstring)	

print("Run DP Knapsack")
print("I need a data structure to store my n items weights and values")
print("I think I will use a dictionary")
print("Also the capacity which is a constant")

tabla = {1: [3, 25], 2: [2, 20], 3: [1, 15], 4: [4, 40], 5: [5, 50]}
capacity = 6
size = len(tabla)

for key, value in tabla.items():
	print(key, value)

print("I also should create my dynamic programming table and pad it with zeros")
print("let's create a table")

tabladp = list()
for x in range(size + 1):
	tabladp.append(zerolistmaker(capacity + 1))

print("Table OK, hash/dictionary OK, variables OK")
print("time to code the main function")

def knapsack(dtable):
	#by definition F(0,j) = 0 and F(i, 0) = 0 so we can start at dtable[1][1]
	#we will go row by row filling the table, so let's start with item 1

	for x in range(size):
		for y in range(capacity):
			i = x + 1
			j = y + 1
			weight = tabla[i][0]
			value =  tabla[i][1]

			if(j - weight < 0):
				dtable[i][j] = dtable[i-1][j]
			else:
				dtable[i][j] = max(dtable[i-1][j], value + dtable[i-1][j-weight])

print("Time to code the backtracking function")
#this only finds one of the (possibly many) optimal subsets
def backtracksack(dtable):
	#we start in the last spot of our table
	#we should go item by item until we reach an stopping condition
	solset = list()
	currentit = size
	currentcap = capacity

	while(currentit != 0 and currentcap != 0):
		if(dtable[currentit][currentcap] > dtable[currentit - 1][currentcap]):
			#then we take current item
			solset.append((currentit, tabla[currentit]))
			currentcap = currentcap - tabla[currentit][0]
			currentit = currentit - 1
		else:
			#we didn't took current item
			currentit = currentit - 1

	return solset

knapsack(tabladp)
printh(tabladp)
print(backtracksack(tabladp))

