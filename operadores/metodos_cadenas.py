#creando una lista con list()
lista = list(["hola","mario",11,15,89,True])

#devuelve la cantidad de elementos de la lista
cantidad_de_elmentos = len(lista)
#agregando un elemento a la lista
lista.append("vamoj a jugar futbol")
#agregando un elemento ala lista de un indice especifico
lista.insert(2,"deja de joder")
#agregando varios elementos ala lista 
lista.extend([True,1989,11])
#eliminando un elemento de la lista (por su indice)
lista.pop(3)
#removiendo un elemento de la lista por su valor 
lista.remove("deja de joder")

#verificando si un elemento se encuentra en la lista

elemento_encontrado = lista.index("hola")


print(elemento_encontrado)
      
    




