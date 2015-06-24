def programm(num):
	num_sto = num % 100
	num_des = num_sto % 10
	print num_sto
	if num_sto > 4 and num_sto < 20:
		return str(num) + " programmistov"
	else:
		if num_des == 1:
			return str(num) + " programmist"
		elif num_des > 1 and num_des < 5:
			return str(num) + " programmista"
		else:
			return str(num) + " programmistov"
			
print programm(int(raw_input("Enter number: ")))						
print programm(int(raw_input("Enter number: ")))
print programm(int(raw_input("Enter number: ")))
