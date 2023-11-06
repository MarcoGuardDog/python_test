diccionario = { 
    "nombre" : "mario",
    "apellido" : "mojica",
    "subs" : 100000

}
#elemento con get()  si no encuentra nada igual el programa continua
valor_de_karen= diccionario.get("karen")
print("hola mario el programa continua")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("subs")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)