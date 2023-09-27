def puissance(a,b):
	if a==0 and b<0 :
		raise TypeError("The power of zero is undefined for a negative exponant") 
	if b==0 :
		return 1
	if type(a) and type (b) is int :
		c=1
		if b<0:
			for i in range (b*(-1)):
				c=c/a
			return c	
		if b>=0:
			for i in range (b):
				c=a*c
			return c
	else :
		raise TypeError("Only integers are allowed")

