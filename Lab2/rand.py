import random
def n():
	while True:
		a= raw_input("write something")
		if a == "n":
			a = random.randint(0,1)
			if a == 1:
				print  "H"
			else:
				print "T"
		elif a == 'b':
			ab = int(raw_input("how many times?"))
			lis = []
			for x in xrange(ab):
				a = random.randint(0,1)
				lis.append(a)
			print lis
n()
