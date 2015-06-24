r_input = open("input.txt", "r")
w_output = open("output.txt", "w")
r_output = open("output.txt", "r")
"""
one = int(f.readline())
two = int(f.readline())
"""
x = 0
y = 0
pravda = True
while pravda == True:
	zetta = 0
	zetta = r_input.readline()
	if zetta != "":
		print zetta
		zetta = int(zetta)
		y = y + zetta
	else:
		break
		print "end"
		pravda = False	
	zetta = 0

w_output.write(str(y))
print "Sum file = " + str(y)

r_input.close
w_output.close
r_output.close	

"""
print one
print two

three = one + two
print three

p.write(str(three))

f.close
p.close

if f.closed and p.closed:
	print "all files closed"
"""

