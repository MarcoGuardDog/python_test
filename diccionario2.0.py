#creando diccionario con dict()
diccionario = dict(nombre="mario",apellido="mojica",ciuda = "santa cruz")


#las listas no pueden ser clave
diccionario = {("mario","el peor"):"jajajaja"}

#creando diccionario con fromkeys()
diccionario = dict.fromkeys(["nombre","apellido","seguidores"])


print(diccionario)
