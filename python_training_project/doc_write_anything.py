f = open("output.txt", "w")
f.write(str(raw_input("Enter any text: ")))


answer = raw_input("Do you wanna rewrite text?: ")
answer = (str(answer)).lower()

while answer == "yes" or answer == "y" or answer =="yep":
	f.write(str(raw_input("Enter any text: ")))
	answer = raw_input("Do you wanna rewrite text?: ")
	answer = (str(answer)).lower()
	if answer == "no" or answer == "n":
		print "Good bye!"
		f.close
		break	

if f.close() != True:
	f.close
	print "file closed and writed"
else:
	print "file closed and writed"	
