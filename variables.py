Variable = """Variable
            Lo que contiene esta informacion
            en este caso el nombre es variable"""
Variable2 = """lo que contiene la variable
            es la definicion en este caso
            este string"""

print (Variable)
print (Variable2)

#se puede usar el += para la suma o -= para resta
#Ejmplo
numero = 8
print (numero)
numero += 12
print (numero)
numero -= 10
print (numero)
#ahora esto se va a ejecutar con esos resultados
# correr para verlo...

#Concatenacion, unir dos o mas cadenas de texto
nombre = "Vivian"
saludo = "Hola " + nombre + " como estas?"
print (saludo)

#Para concatenar booleanos, enteros, flotantes etc...
#Hay que ponerle un f delante para recrearlo en string
#Ejemplo ahora nombre va a ser boolean o int
nombre = True
print (saludo)
#si ahora pongo el f como dije sale distinto, observar.
saludo = f"Hola {nombre} como estas?"
print (saludo)
nombre = 7.43
saludo = f"Hola {nombre} como estas?"
print (saludo)
#variable de pertenencia o identidad
#te muestra si hay algo que pertenezca a la variable
#print ('Hola' in saludo) #va a mostrar True porque esta
print ('Hola' in saludo)
#Ahora si ponemos hola sin H mayuscula es False
#porque es case sensitive
print ('hola' in saludo)
#si buscamos cualquier pedazo que contenga esa variable
#nos va a mostrar True, ejmplo ola
print ('ola' in saludo)
#Lo mismo para not in
print ('vivian' not in saludo)