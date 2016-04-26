#Practica: Aritmetica modular - Criptografia 2016
#Autor: Ahisahar Pretel Rodriguez
#Correo: approdriguez@correo.ugr.es



from time import time
import timeit
import math
import random
from math import ceil

#Numero de ejecuciones para calcular el tiempo de media
n_ejec = 100

#Ejercicio 1

def mcd(a, b):
	"""mcd: Gives the mcd of two given numbers as a linear combination

	Args:
		a (int): just a number
		b (int): a number

	Returns:

		The mcd of the two numbers and que u, v values

	Examples:

		#a = 24
		#b = 14

		#d,u,v = mcd(a,b)
	"""
	x = 0
	y = 1
	u = 1
	v = 0
	while a != 0:
		q = b//a
		r = b%a
		m = x-u*q
		n = y-v*q
		b,a = a,r
		x,y = u,v
		u,v = m,n
	mcd = b
	return mcd, x, y

a=4864
b=3458

print("Ejercicio 1. Algoritmo extendido de Euclides\n")
print("Parametros: a, b =",a ,b)
print("Solucion: ",mcd(a,b))
t = timeit.Timer(lambda: mcd(a,b))
print("Tiempo de ejecucion medio(",n_ejec,"ejecuciones): ",t.timeit(n_ejec)/n_ejec)
print("---------------------------------------------------------")




#Ejercicio 2
#calculo de inverso mod p

def modinv(a, m):
		"""modinv: returns a^-1 mod p

		Args:
			a (int): just a number
			m (int): the number Zp a.k.a. mod p

		Returns:

			Int: a^-1 mod p

		Examples:

			#a = 24
			#b = 14

			#a = modinv(a,b)
		"""
		g, x, y = mcd(a, m)
		if g != 1:
			return -1
		else:
			return x % m
a = 117
b = 244

print("Ejercicio 2. Inverso Modular\n")
print("Parametros: a, b =",a ,b)
print("Solucion: ",modinv(a,b))
t = timeit.Timer(lambda: modinv(a,b))
print("Tiempo de ejecucion medio(",n_ejec,"ejecuciones): ",t.timeit(n_ejec)/n_ejec)
print("---------------------------------------------------------")


#Euclides algorithm for mcd only

def mcdd(a,b):


		"""mcd: Gives the mcd of two given numbers

		Args:
			a (int): just a number
			b (int): a number

		Returns:

			The mcd of the two given numbers

		Examples:

			#a = 24
			#b = 14

			#d = mcdd(a,b)
		"""
		x = 0
		y = 1
		u = 1
		v = 0
		while a != 0:
			q = b//a
			r = b%a
			m = x-u*q
			n = y-v*q
			b,a = a,r
			x,y = u,v
			u,v = m,n
		mcd = b
		return mcd



def powerIntMod(y, x, n):

		"""powerIntMod: Gives y^x mod n "pretty fast"

		Args:
			y (int): just a number
			x (int): a number
			n (int): mod number
		Returns:
			int: y**x mod n
		Examples:

			y = 24
			x = 14
			n = 114

			e = powerIntMod(y,x,n)
		"""
		a = x
		b = 1
		c = y
		while a != 0:
			if a % 2 == 0:
				a = a/2
				c = (c**2) % n
			else:
				a = a -1
				b = (b * c) % n
		return b
a = 5
b = 596
n = 1234

print("Ejercicio 3. Exponenciacion modular\n")
print("Parametros: a, b ,n=",a ,b)
print("Solucion: ",powerIntMod(a,b,n))
t = timeit.Timer(lambda: powerIntMod(a,b,n))
print("Tiempo de ejecucion medio(",n_ejec,"ejecuciones): ",t.timeit(n_ejec)/n_ejec)
print("---------------------------------------------------------")


def MillerRobin(n,k):

	"""MillerRobin test: Tells with a probability of 1/4 if a given numer is prime and tells with 100% true if number is not prime

	Args:
		n (int): The number to test if it is prime
		k (int): number of iterations

	Returns:

		True if the number is probably prime
		False if the number is not prime

	Examples:

		Examples should be written this way:

		primo = 21

		>>>print('Aviso: si es primo es con una probabilidad de 1/4\n')
		>>>print ('El '+str(primo)+' es primo?: '+ str(isprime))

		Aviso: si es primo es con una probabilidad de 1/4

		El 75937643 es primo?: True
	"""


	if(n==2):
		return True
	if(n==1):
		return True

	s=0
	p = n-1

	if(n>3):
		p = n-1
		while p%2:
			s = s+1
			p = p/2
			ant = 0

		for i in range (1,k):
			a = random.randint(2,n-2)
			x = powerIntMod(a,s,n)

			if(x!=1 and x+1 != n):
				for r in range(1,s):
					x = powerIntMod(x,2,n)
					if(x==1):
						return False
					elif(x==-1):
						return True

				else:
					return False
			return True
p=123456789101119
k=4
print("Ejercicio 4. MillerRabin\n")
print("Parametros: p = ",p)
print("Solucion: ",MillerRobin(p,k))
t = timeit.Timer(lambda: MillerRobin(p,k))
print("Tiempo de ejecucion medio(",n_ejec,"ejecuciones): ",t.timeit(n_ejec)/n_ejec)
print("---------------------------------------------------------")


def sqrt(n):

	"""sqrt: Returns the largest integer x for which x * x exceed n.

	Args:
		n (int): A number

	Returns:

		(int): the largest integer x for x*x = n

	Examples:

		n = 29
		r = sqrt(n)

	"""

	x = n
	y = (x + 1) // 2
	while y < x:
		x = y
		y = (x + n // x) // 2
	if(x*x == n):
		return x
	else:
		return x+1

def PasoEnanoPasoGigante(a,c,p):

	"""PasoEnanoPasoGigante: compute discrete logarithms in Zp

	Args:
		a (int):
		c (int):
		p (int):

	Returns:

		True if the number is probably prime
		False if the number is not prime

	Examples:
	"""
	A = []
	B = []
	x=1

	s = sqrt(n)

	aux = c


	A.append(aux)

	for i in range(1,s):
		aux=(aux*a)%p
		A.append(aux)
	for i in range(1,s+1):
		aux=powerIntMod(a,i*s,p)
		B.append(aux)


	for i in A:
		#print(str(i))
		for j in B:
			#print(str(j))
			if i == j:
				x=A.index(i)
    			y=B.index(j)
            	break
	#print(str(x))
	x=  (((c+1)*s-x)%p)
	return x

n=113
a=3
b=57
print("Ejercicio 5. Paso Enano-Paso Gigante\n")
print("Parametros: n, a, b = ",n, a, b)
print("Solucion: ",PasoEnanoPasoGigante(a,b,n))
t = timeit.Timer(lambda: PasoEnanoPasoGigante(a,b,n))
print("Tiempo de ejecucion medio(",n_ejec,"ejecuciones): ",t.timeit(n_ejec)/n_ejec)
print("---------------------------------------------------------")


#Ejercicio 6

def Jacobi(a,p):
	"""Jacobi: a tool for compute Legendre symbols

	Args:
		a (int): a number
		p (int): and odd number

	Returns:

		(int): the value of the Jacobi Symbol

	Examples:
	"""

	if(p%a==0):
		return 0
	if(a==0):
		return 0
	if(a==1):
		return 1
	aux=a
	u=0
	#s=0
	while(aux%2==0):
		aux=aux/2
		u=u+1
	if(u>0):
		s=1
	if(p%8==1 or p%8==7):
		s=1
	elif(p%8==3 or p%8==5):
		s=-1
	if(p%4==3 and aux%4==3):
		s = -s
	n_1 = p%aux
	if(aux==1):
		return s
	else:
		return s * Jacobi(n_1,aux)

#Ejercicio 6a

def RaizModular(a,p):

	"""RaizModular: gives a root of a mod p

	Args:
		a (int): a number
		p (int): a prime number

	Returns:

		(int): a root of a mod p

	Examples:
	"""
	n=1
	while(Jacobi(n,p)!=-1):
		n = n+1
	aux = p-1
	u=0
	while(aux%2==0):
		aux=aux/2
		u=u+1
	s = aux
	if(u==1):
		r = powerIntMod(a,(p+1)/4,p)
	if(u>=2):
		r = powerIntMod(a,(s+1)/2,p)
		b = powerIntMod(n,s,p)
		j=0
		while(j<u-2):
			if(powerIntMod(modinv(a,p)*powerIntMod(r,2,p),powerIntMod(2,u-2-j,p),p)==-1%p):
				r = (r*b)%p
			b=powerIntMod(b,2,p)
			j = j+1
	return r


a = 319
p = 353
print("Ejercicio 6. Raices Modulares\n")
print("Parametros: a, p=",a, p)
print("Solucion: ", RaizModular(a,p))
t = timeit.Timer(lambda: RaizModular(a,p))
print("Tiempo de ejecucion medio(",n_ejec,"ejecuciones): ",t.timeit(n_ejec)/n_ejec)
print("---------------------------------------------------------")


#Ejercicio 6b

def RaicesCuadradas(a,p,q,n):
	""" Find sqare roots mod n
	args:
		a : int
		p : int
		q : int
		n : int
	returns:
		4 ints: prime factors
	example:

	r1,r2,r3,r4 = RaicesCuadradas(a,p,q,n)


	"""
	r = RaizModular(a,p)
	s = RaizModular(a,q)
	aux,c,d = mcd(p,q)
	x = (r*d*q + s*c*p)%n
	y = (r*d*q - s*c*p)%n
	return (x%n, -x%n, y%n, -y%n)

a= 132
p= 17
q= 29
n= 493
print("Ejercicio 6. Raices Cuadradas teorema chino\n")
print("Parametros: a, p, q, n=",a, p, q, n)
print("Solucion: ", RaicesCuadradas(a,p,q,n))
t = timeit.Timer(lambda: RaicesCuadradas(a,p,q,n))
print("Tiempo de ejecucion medio(",n_ejec,"ejecuciones): ",t.timeit(n_ejec)/n_ejec)
print("---------------------------------------------------------")

#Ejercicio 7
#hallar subconjunto de elementos cuyo producto es un cuadrado
def Fermat(n):
		"""Fermat: gives a given number as: n = x+y * x-y

		Args:
			n (int): a number

		Returns:

			(int): a + b
			(int): a - b

		Examples:
			Fermat(6352351)
		"""
		a = int(ceil(n**0.5))
		bc = a*a -n
		b = int(bc**0.5)
		while b*b!=bc:
			a = a+1
			bc = a*a -n
			b = int(bc**0.5)
		return a+b,a-b

n=455459
print("Ejercicio 7. Fermat\n")
print("Parametros: n=",n)
print("Solucion: ",Fermat(n))
t = timeit.Timer(lambda: Fermat(n))
print("Tiempo de ejecucion medio(",n_ejec,"ejecuciones): ",t.timeit(n_ejec)/n_ejec)
print("---------------------------------------------------------")

def funcionPollard(n):
	return (n**2) + 1

def Pollard(n):
	"""Pollard: returns a root of a given number

	Args:
		n (int): a number


	Returns:

		(int): a root of the number

	Examples:
		Pollard(6352351)
	"""
	a = random.randint(1,n-1)
	x = funcionPollard(a)%n
	y = funcionPollard(x)%n
	i = 1
	Iter = 4
	while(i<Iter):
			d,u,v = mcd(y-x,n)
			if(d<0):
				d= d -2*d
			if(d==n):
				print (str(n)+' es probablemente primo')
				return n
			if(d==1):
				i = i+1
				x = (x**2)+1%n
				y = powerIntMod((y**2) + 1,2,n)+1%n
			if(d>1 and d<n):
				return d

n=455459

print("Ejercicio 7. Pollard\n")
print("Parametros: n=",n)
print("Solucion: ",Pollard(n))
t = timeit.Timer(lambda: Pollard(n))
print("Tiempo de ejecucion medio(",n_ejec,"ejecuciones): ",t.timeit(n_ejec)/n_ejec)
print("---------------------------------------------------------")
