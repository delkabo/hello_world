from random import randint

#create area for battleship
array = []
for x in range(0,10):
	array.append(["."]*10)
	
x = randint(0, len(array) - 1)
y = randint(0 , len(array) - 1)


#chosen type ship
def type_ship():
	ship = randint(1, 4)
	return ship				
	
for x in range(0,10):
	print " ".join(array[x])
print	

def ship_var():
	x = randint(1, 2)
	return x

def check_to_free(y, x, type_sh, ship_v):
	walking = type_sh - 1
	"""
	print str(y) + " " + str(x)
	print "Palubi: " + str(type_sh) + " VertorHor: " + str(ship_v)
	"""
	
	if array[y][x] == ".":
		
		if ship_v == 1:
			for step in range(x, x + type_sh - 1):
				if array[y][x] == ".":
					x += 1
				else:
					return False
					break		
			return True			
		if ship_v == 2:
			for step in range(y, y + type_sh - 1):
				if array[y][x] == ".":
					y += 1
				else:
					return False
					break	
			return True	
	else:
		return False

def krestiki():
	for igrik in range(0, 9):
		for iks in range(0, 9):
			if array[igrik][iks] == "0":
				if array[igrik][iks+1] == ".":
					array[igrik][iks+1] = "x"					
				if array[igrik+1][iks] == ".":
					array[igrik+1][iks] = "x"
				if array[igrik+1][iks+1] == "." and igrik+1 < 10:
					array[igrik+1][iks+1] = "x"	
				if array[igrik-1][iks+1] == "." and igrik-1 > -1:
					array[igrik-1][iks+1] = "x"	
				
	for igrik in range(-9, 0):
		igrik = igrik * (-1)
		for iks in range(-9, 0):
			iks = iks * (-1)
			if array[igrik][iks] == "0":
				if array[igrik][iks-1] == ".":
					array[igrik][iks-1] = "x"					
				if array[igrik-1][iks] == ".":
					array[igrik-1][iks] = "x"
				if array[igrik-1][iks-1] == "." and igrik-1 > -1:
					array[igrik-1][iks-1] = "x"	
				if igrik+1 < 10 and array[igrik+1][iks-1] == ".":
					print array[igrik+1][iks-1]
					print igrik
					print iks
					array[igrik+1][iks-1] = "x"
					
					
					
					
	

def point_to_start():
	type_sh = type_ship()
	ship_v = ship_var()
	pic_or_not = False
	
	dre = 0
	
	while pic_or_not != True:
		if ship_v == 1:
			x = randint(0, len(array) - type_sh)
			y = randint(0, len(array) - 1)
			pic_or_not = check_to_free(y, x, type_sh, ship_v)	
		elif ship_v == 2:
			x = randint(0, len(array) - 1)
			y = randint(0, len(array) - type_sh)
			pic_or_not = check_to_free(y, x, type_sh, ship_v)
		
		dre += 1
		if dre > 20:
			break	
	
	if ship_v == 1:
		for step in range(0, type_sh):
			array[y][x] = "0"
			x += 1
	elif ship_v == 2:
		for step in range(0, type_sh):
			array[y][x] = "0"
			y += 1
	else:
		print "Error print array"
		
	for step in range(0,100):
		krestiki()
	
				
					
					
	
	for betta in range(0, 10):
		print " ".join(array[betta])
	print								 		

point_to_start()
point_to_start()
point_to_start()
point_to_start()
point_to_start()
point_to_start()
point_to_start()
point_to_start()

"""
po bokam ne vsegda stavit ktestiki
"""
