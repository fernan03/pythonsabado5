diccionario={
    'nombre':"juan",
    'edad':33,
    'hinchaVerde':True,
    'comidasFavoritas':['yogur','arandanos','alpiste']
}

print(diccionario)
print(diccionario['comidasFavoritas'][1])


#Diccionario vacion y llenarlo por teclado

diccionario2={}
diccionario2['nombre']=input("Digite su nombre: ")

#Recorrer diciconario
for llave,valor in diccionario2.items():
    print(llave)
    print(valor)