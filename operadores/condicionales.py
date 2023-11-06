
#AND

resultado = True & True #Devolver True
resultado2 = False & True #Devolver Falso
resultado3 = True & False #Devolver falso 
resultado4 = False & True #Devolver falso

#OR

resultado5 = True & True #Devolver True
resultado6 = False & True #Devolver True
resultado7 = True & False #Devolver True
resultado8 = False & False #Devolver Falso

#NOT

resultado9 = not 23 == 23 #Devolver Falso
resultado10 = not False #Devolver True

print(resultado9)

codigo_de_ropa = "american cool"
codigo_de_polera = "levis"


if codigo_de_ropa   ==  codigo_de_polera:
    print("te compra un pley")

else:
    print("te mando a estudiar")

print("mejor anda a dormir")