print("*****MENU*****")
print("1. Agregar 1 empanada")
print("2. Mostrar empanada")
print("3. Salir")
opciones=100
#DATOS EMPANADAS
#SABOR
#INGREDIENTES (X3)
#PRECIO FABRICACION
#PRECIO VENTA

empanada={}
ingredientes=[]
precioFabricacion=()
precioVenta=()


while(opciones !=3):
    opciones = int(input("Digite una opcion"))
    if(opciones==1):
        empanada['sabor']=input("Digite sabor: ")
        for contador in range(3):
            ingredientes.append=(input(f'Digita el ingrediente {contador+1}'))
        empanada['ingredientes']=ingredientes
        empanada['precioFabricacion']=input("Digite precio fabricacion: ")
        empanada['precioVenta']=input("Digite precio venta: ")
        print("Agregando empanada")
    elif(opciones==2):
        for llave,valor in empanada.items():
            print(llave)
            print(valor)
    else:
        print("Digite opcion valida")




#MISMO EJERCICIO MEJORADO


