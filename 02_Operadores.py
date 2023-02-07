# Operadores #

# Operaciones con enteros #
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(10 ** 3)
print(2 ** 3 + 3 - 7 / 1 // 4)

# Operaciones con cadenas de texto
texto1, texto2, texto3 = "Hola ", "Python ", "¿Qué tal?"
 
print(texto1 + texto2 + texto3)
print("Hola " + str(10//3))
print("Operacion larga: " + str(2 ** 3 + 3 - 7 / 1 // 4))

# Operaciones mixtas
print("Hola " * (2 **2))
my_float = 2.5 * 2
print("Hola " * int(my_float))

# Operadores Comparativos #

# Operaciones con enteros #
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

# Operaciones con str #
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa") #Orden alfabetico
print(len("aaaa") >= len("abaa")) #longitud
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

# Operadores logicos #
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))