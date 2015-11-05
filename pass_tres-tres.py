#!/usr/bin/env python
# By Tedezed

cadena1='pass_old'
cadena2='pass_new'
coparar = ''
comparar2 = ''
fin_i = 3
fin_x = 3

coincidencias = ''

while fin_i <= len(cadena1):
	comparar = cadena1[fin_i-3:fin_i]
	print 'Cadena 1 con: ' + comparar

	while fin_x <= len(cadena2):
		comparar2 = cadena2[fin_x-3:fin_x]
		print comparar2
		if comparar == comparar2:
			#print 'ENCONTRADO!'+ comparar + ' con ' + comparar2
			coincidencias =  coincidencias + ' ' + comparar 
		fin_x = fin_x + 1

	fin_x = 3
	fin_i = fin_i + 1

print 'ENCONTRADO: ' + coincidencias
