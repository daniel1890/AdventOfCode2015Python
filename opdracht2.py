lijst = open("opdracht2.txt").read()
array = lijst.split("\n")

#deel 1

def calc(getallen):
	getallen_lijst = getallen.split("x")
	lengte = int(getallen_lijst[0])
	breedte = int(getallen_lijst[1])
	hoogte = int(getallen_lijst[2])
	int_array = [lengte, breedte, hoogte]

	totaal = (2 * lengte * breedte) + (2 * breedte * hoogte) + (2 * hoogte * lengte)
	int_array.sort()	
	restwaarde = int_array[0] * int_array[1]
	totaal += restwaarde

	return totaal

ans = 0

for getallen in array:
	ans += calc(getallen)

print("Antwoord deel 1: ", ans)

# deel 2

ans2 = 0

def bow(getallen):
	getallen_lijst = getallen.split("x")
	lengte = int(getallen_lijst[0])
	breedte = int(getallen_lijst[1])
	hoogte = int(getallen_lijst[2])
	int_array = [lengte, breedte, hoogte]

	int_array.sort()

	totaal = (int_array[0] * 2) + (int_array[1] * 2)
	totaal += int_array[0] * int_array[1] * int_array[2]
	return totaal


for getallen in array:
	ans2 += bow(getallen) 


print("Antwoord deel 2: ", ans2)