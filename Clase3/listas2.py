array1=["futbol", "Pc", 18.6,18,[6,7,10.4],"Pc"]
array2=[200,250,"hola"]
array3=array1+array2
print(array3)
#buscar valores dentro de un array
print("Pc" in array1)
#saber el indice donde esta lo que busco
print(array1.index("Pc"))
#cantidad de veces que tengo el valor en mi array
print(array1.count("Pc"))
#borrar valores de un array
array1.remove("Pc")
print(array1)
#limpiar
array1.clear()
#cambiar de posicion 
array1.reverse()
print(array1)
#ordenar de mayor a menor
array4=[1,2,8,-11,5]
array4.sort()
print(array4)
array4.sort(reverse=True)
print(array4)