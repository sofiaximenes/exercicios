n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))

if n1 < n2:
	n1, n2 = n2, n1

r1, mdc = n1%n2, n2
while r1 != 0:
	r1, mdc = mdc%r1, r1
	
print ('O mdc de (%d,%d) é: %d'%(n1,n2,mdc))