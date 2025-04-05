'''introduccion a listas'''
array = ["futbol", "Pc", 18.6,18,[6,7,10.4],True, False]
print(array)
print(array[1])
print(array[4])
print(array[-1])
print(array[0:3])
print(array[:2])
print(array[2:])
#cantidad de datos que encuentra el array
print(len(array))
#agregar un valor dentro de la lista
array.append(66)
print(array)
#insertar datos en una posicion
array.insert(1,88)
print(array)
#insertar mas de un dato al final
array.append([1,88,True,100])
print(array)