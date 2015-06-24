from random import randint

size_q = int(raw_input("Enter size square: "))
ai = raw_input("Two player or one? Take number player: ")
if int(ai) == 1:
	ai_men = True
else:
	ai_men = False	

area = []
for x in range(0,size_q):
	area.append(["*"]*size_q)
	

#area[2][2] = "X"
for x in range(0,size_q):
	print " ".join(area[x])
	
print

#function horizontal
def hor(area_func, player):
	win = False
	for y in range(0,size_q):
		for x in range(0,size_q):
			if area_func[y][x] == player:				
				point = 0
				zetta = x
				while zetta < size_q:
					if area_func[y][zetta] == player:
						point += 1					
					zetta += 1
				if point == 5:
					win = True
					break
			elif win == True:
				break
		if win == True:
			break
	if win == True:
		print "You Win!"						
	
#function vertical
def vert(area_func, player):
	win = False
	for y in range(0,size_q):
		for x in range(0,size_q):
			if area_func[y][x] == player:				
				point = 0
				zetta = y
				while zetta < size_q:
					if area_func[zetta][x] == player:
						point += 1					
					zetta += 1
				if point == 5:
					win = True
					break
			elif win == True:
				break
		if win == True:
			break
	if win == True:
		print "You Win!"
	
#function diagonal up/down

def diag_down(area_func, player):
	win = False
	for y in range(0,size_q):
		for x in range(0,size_q):
			if area_func[y][x] == player:				
				point = 0
				zetta = y
				betta = x
				while zetta < size_q and betta < size_q:
					if area_func[zetta][betta] == player:
						point += 1					
					zetta += 1
					betta += 1
				if point == 5:
					win = True
					break
			elif win == True:
				break
		if win == True:
			break
	if win == True:
		print "You Win!"
				
#function diagonal down/up
def diag_up(area_func, player):
	win = False
	for y in range(0,size_q):
		for x in range(0,size_q):
			if area_func[y][x] == "X":				
				point = 0
				zetta = y
				betta = x
				while zetta >= 0 and betta < size_q:
					if area_func[zetta][betta] == player:
						point += 1					
					zetta -= 1
					betta += 1
				if point == 5:
					win = True
					break
			elif win == True:
				break
		if win == True:
			break
	if win == True:
		print "You Win!"

def ai_walk(area_func):
	num_hor = randint(0, size_q)
	num_vert = randint(0, size_q)
	area_func[num_hor][num_vert] = "O"	


pravda = True
x = "X"
o = "O"
while pravda == True:
	num1 = int(raw_input("Enter player1 the number from 1 to 5: "))-1
	num2 = int(raw_input("Enter player1 the number from 1 to 5: "))-1
	area[num1][num2] = x
	
	for z in range(0,size_q):
		print " ".join(area[z])
	print	
	#player_one
		
	hor(area, x)				
	vert(area, x)
	diag_down(area, x)
	diag_up(area, x)
	
	#player_two
	hor(area, o)				
	vert(area, o)
	diag_down(area, o)
	diag_up(area, o)
	############
	
	if ai_men == True:
		ai_walk(area)
	else:
		num1 = int(raw_input("Enter player2 the number from 1 to 5: "))-1
		num2 = int(raw_input("Enter player2 the number from 1 to 5: "))-1
		area[num1][num2] = o	
	
	for z in range(0,size_q):
		print " ".join(area[z])	
					
	answer = str(raw_input("Do you wan enter number? "))
	answer = answer.lower()
	if answer == "n" or answer == "no":
		pravda = False
		
	
	
	
