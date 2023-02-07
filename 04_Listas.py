### Listas ###

my_list = list()
my_other_list = [] 

print(len(my_list))
print(len(my_other_list))

my_list = [20, 24, 62, 52, 30, 30, 17]

print(len(my_list))
print(my_list)

my_other_list = [20, 1.72, "Antonio", "Ramos"]

print(type(my_other_list)) 
print(type(my_list)) 

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[2])
print(my_other_list[3])
print(my_other_list[-1])
print(my_other_list[-2])
print(my_other_list[-3])
print(my_other_list[-4])

print(len(my_other_list))

print(my_list.count(30))

edad, alt, nom, ap = my_other_list
print(nom)

edad, alt, nom, ap = my_other_list[0], my_other_list[1], my_other_list[2], my_other_list[3]
print(nom)

print(my_list + my_other_list)
print(my_list + my_other_list)

# crear, insertar, actualizar, borrar #

print(my_other_list.append("Itocotlan"))

my_other_list.insert(1,"Rojo")
print(my_other_list)

my_other_list[1] = "Morado"
print(my_other_list)

my_other_list.remove("Morado")
print(my_other_list)

print(my_list)
my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop = my_list.pop(2)
print("Elemento eliminado: " + str(my_pop))
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()
my_list.clear()

print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

# Cambio de tipo #

my_list = "Hola"
print(my_list)
print(type(my_list))