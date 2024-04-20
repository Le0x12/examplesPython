# Problema: Escribí un programa para solicitar al usuario el ingreso de un número entero y que luego imprima un valor de verdad dependiendo de si el número es par o no. 
# Recordar que un número es par si el resto, al dividirlo por 2, es 0.
 
# Ejemplo de ejecución:

# Número entero: 7254
# True

# Algoritmo:

# V 0.0
# 1) Pedir un numero en una variable 
# 2) crear una variable para el resultado 
# 3) obtener el residuo del numero para usar entre dos 
# 4) si el residuo es 0 imprimir true si no pasar a paso 5
# 5) imprimir false

# V 0.1
# 1) Pedir un numero en una variable 
# 2) Verificar que la entrada sea un numero entero 
# 3) obtener el residuo del numero para usar entre dos 
# 4) si el residuo es 0 imprimir true si no pasar al siguiente paso
# 5) imprimir false

# V 1.0
# 1) Pedir un numero en una variable 
# 2) Verificar que la entrada sea un numero entero 
# 3) Si el valor es un numero pasa al siguiente paso
# 4) Si no retonar a la peticion del numero 
# 5) obtener el residuo del numero para usar entre dos 
# 6) si el residuo es 0 imprimir true si no pasar al siguiente paso
# 7) imprimir false

isANumber = True

while isANumber:
    numberToUse = input("Hola, Ingresa un numero entero por favor ☜(⌒▽⌒)☞ ---->  ")
    isANumber = numberToUse.isnumeric()
    if isANumber:
        residuo = int(numberToUse) % 2
        if residuo == 0:
            print("Tu numero es par (ღ˘⌣˘ღ)")
            isANumber = False
        else:
            print("Tu numero no es par (╯°□°)╯︵ ┻━┻ ︵ ╯(°□° ╯)")
            isANumber = False
    else:
        print("Por favor ingresa solo numeros ᕕ(╭ರ╭ ͟ʖ╮•́)⊃¤=(————-")
        print("                                                   ")
        isANumber = True

print("                               ")
print("-------------------------------")
print("Gracias por usar mi programa ─=≡Σ((( つ◕ل͜◕)つ ")



