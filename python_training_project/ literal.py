

print '\033[0;31mHello Red!'

print '\033[0;32mHello Green!'

print '\033[0;30mHello Black!'



def edinici(x):
	if x == 1:
		return "odin"
	elif x == 2:
		return "Dva"
	elif x == 3:
		return "Tri"
	elif x == 4:
		return "Chetire"
	elif x == 5:
		return "Pyat'"
	elif x == 6:
		return "Shest'"				
	elif x == 7:
		return "Sem''"
	elif x == 8:
		return "Vosem"	
	elif x == 9:
		return "Devyat'"											
	else:
		return ""
		
def desyatki(x):
	if x == 10:
		return "Desyat'"
	elif x == 11:
		return "Odinadzat'"	
	elif x == 12:
		return "Dvenadzat'"
	elif x == 13:
		return "Trenadzat'"
	elif x == 14:
		return "Chetirnadzat'"
	elif x == 15:
		return "Pyatnadzat'"
	elif x == 16:
		return "Shestnadcat'"
	elif x == 17:
		return "Semnadzat'"
	elif x == 18:
		return "Vosemnadzat'"
	elif x == 19:
		return "Devyatnadzat'"
	elif okruglenie(x) == 20:
		return "Dvadzat' "
	elif okruglenie(x) == 30:
		return "Tridzat' "
	elif okruglenie(x) == 40:
		return "Sorok "
	elif okruglenie(x) == 50:
		return "Pyatdesyat "
	elif okruglenie(x) == 60:
		return "SHestdesyat "
	elif okruglenie(x) == 70:
		return "Semdesyat "
	elif okruglenie(x) == 80:
		return "Vosemdesyat "
	elif okruglenie(x) == 90:
		return "Devyanosto "
	else:
		return ""
		
def sotni(x):
	if okruglenie(x) == 100:
		return "sto "
	elif okruglenie(x) == 200:
		return "dvesti "
	elif okruglenie(x) == 300:
		return "trista "
	elif okruglenie(x) == 400:
		return "chetiresta "
	elif okruglenie(x) == 500:
		return "pyatsot "	
	elif okruglenie(x) == 600:
		return "shestsot "
	elif okruglenie(x) == 700:
		return "semsot "
	elif okruglenie(x) == 800:
		return "vosemsot "
	elif okruglenie(x) == 900:
		return "devyatsot "							
	else:
		return ""			

		

def cifer_liter(x):
	
	a = x % 1000
	b = x % 100
	c = x % 10
	edin_i = ""
	
	sotnya_i = sotni(a)
	desyat_i = desyatki(b)
	if b not in range(10, 20):
		edin_i = edinici(c)
		
	
	return sotnya_i + desyat_i + edin_i
	
		
	
x = 22
b = x % 100

def okruglenie(n):
	if 999 < n < 10000:
		n_ost = n % 1000
		n = n - n_ost
	elif 99 < n < 1000:
		n_ost = n % 100
		n = n - n_ost
	elif 19 < n < 100:
		n_ost =  n % 10
		n = n - n_ost 	
	return n


print cifer_liter(int(raw_input("Enter number from 1 to 999: ")))
