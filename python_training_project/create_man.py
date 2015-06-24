class man(object):
	color_eyes = "Brown"
	def __init__(self, sex, name, height, weight):
		self.sex = sex
		self.name = name
		self.height = height
		self.weight = weight
		
samantha = man("woman", "Samanta", 170, 65)
samantha.color_eyes = "Blue"
print samantha.color_eyes

class man_two(object):
	
	def create_man(self, name, sex):
		self.sex = sex
		self.name = name
		
john = man_two()
print john.create_man("batMAN", "Man")
print john.sex
	
