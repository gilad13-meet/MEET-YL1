class Integer(object):
	def __init__(self, number, negative):
		self.number = number
		self.negative = negative
	def display(self):
		if (self.negative):
			print "-" + str(self.number)
		else:
			print self.number
	def add(self, number):
		if (self.negative == True):
			return -(self.number + number.number)	
		else:
			return self.number - number.number
	def subtract(self,number):
		if (self.negative == True):
			return -self.number + number.number	
		else:
			return self.number + number.number
	def multiply(self, number):
		if (self.negative == True):
			return self.number * number.number	
		else:
			return -(self.number * number.number)
	def divide(self,number):
		if (self.negative == True):
			return float(self.number) / number.number	
		else:
			return -(float(self.number) / number.number)
		
class NegativeInteger(Integer):
	def __init__(self, number):
		super(NegativeInteger, self).__init__(number, True)
	def display(self):
		Integer.display(self)
		print "This is an object of the NegativeInteger class"
if __name__=="__main__":

	arr = []
	howmuch = raw_input("how much times?")
	for v in xrange(int(howmuch)):
		ispositive = raw_input("is positive")
		number = raw_input("number?")
		if ispositive == "true":
			num = Integer(number, False)
		elif ispositive == "false":
			num = NegativeInteger(number)
		arr.append(num)
	for x in arr:
		x.display()

	
