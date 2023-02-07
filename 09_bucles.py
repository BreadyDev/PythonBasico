### Bucles ###

my_cond = 0

while my_cond <= 10:
    print(my_cond)
    my_cond += 1
else:  
    print("Mi condicion es mayor a 10")
    
print("La ejecucion continua")

while my_cond <= 20:
    my_cond += 1
    
    print(my_cond)
    
    if my_cond == 15:
        print("Se detiene la ejecución")
        break


my_list = [20, 24, 30, 35, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (20, 1.72, "Antonio", "Ramos", "Toño")

for element in my_tuple:
    print(element)

my_set = {"Antonio", "Ramos", 20}

for element in my_set:
    print(element)

my_dict = {"Nombre": "Antonio", "Apellido": "Ramos", "Edad": 20, 1: "Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        print("Se rompe el for")
        break
else:
    print("Bucle del diccionario terminado")
    
for element in my_dict:
    print(element)
    if element == "Edad":
        continue
else:
    print("Bucle del diccionario terminado")