def sumar(a,b):
    return a+b
def restar(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
def resto(a,b):
    return a%b

a = 3
b = 5
resultado = 0

resultado  = sumar(a,b)
print(f"La suma es: {resultado}")
resultado  = restar(a,b)
print(f"La resta es: {resultado}")
resultado  = mult(a,b)
print(f"La multiplicacion es: {resultado}")
resultado  = div(a,b)
print(f"La division es: {resultado}")
resultado  = resto(a,b)
print(f"El resto es: {resultado}")