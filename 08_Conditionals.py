### Condicionales ###

my_cond = False

if my_cond:
    print("Se ejecuto el if")
    
my_cond = int(input("Num: "))

if my_cond == 10:
    print("Se ejecuta el segundo if")
    
if my_cond >= 10 and my_cond <= 20:
    print("Esta entre 10 y 20")
elif my_cond == 25:
    print("Es 25")
else:
    print("Es menor que 10 o mayor que 25")
print("La ejecucion continua")

my_string = "Cadena de texto"

if not my_string:
    print("Cadena vacia")
    
if my_string == "Cadena de texto":
    print("Cadenas coinciden")