print("Run Dynamic Coin Row")

def coin(lista):
	
	#Pad the input list, you could also copy it to a new list
	#or just use an n+1 range or something like that
	lista.insert(0, 0)

	#Create your table for DP
	dtable = list()

	for x in range(len(lista)):
		if(x == 0):
			dtable.append(lista[0])
		elif(x == 1):
			dtable.append(lista[1])
		else:		
			number = max(lista[x] + dtable[x-2], dtable[x-1])
			dtable.append(number)

	return dtable[len(lista) - 1]

		
milista = [5, 1, 2, 10, 6, 2]
print(coin(milista))

print("Ok, but now how to answer question of which coins gave the best amount")
print("I think I can leave this floating for the meantime")

