def divisors(n):
	for x in range (1,n+1):
		if n%x==0:
			print x
if __name__ == "__main__":
	n = int(raw_input("number?"))
	divisors(n)
