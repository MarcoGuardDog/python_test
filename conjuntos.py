#creando un conjunto con set(

conjunto = set(["dato 1","dato 2"])

#metiedno un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato 1", "dato2"])
conjunto2 = {conjunto1,"dato3"}

print(conjunto2)


#teoria de conjuntos
#un conjunto es el que tiene mas dato 
#el subconjo es el que tiene menos datos
conjunto1 = {1,3,5,7} #"conjunto"
conjunto2 = {1,3,7}  #"subconjunto"

print(conjunto2)

resultado = conjunto2.issubset(conjunto1) 

print(resultado)

