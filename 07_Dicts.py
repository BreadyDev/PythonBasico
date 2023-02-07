### Diccionarios ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Antonio", "Apellido":"Ramos", "Edad":20}
my_dict = {
    "Nombre":"Antonio",
    "Apellido":"Ramos",
    "Edad":20,
    1: 1.72,
    "Lenguajes": {"Python", "Java", "C++"}
}

print(my_dict)
print(my_other_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Juan"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Domicilio"] = "Priv Lopez Mateos #110"
print(my_dict)

del(my_dict["Domicilio"])
print(my_dict)

print("Ramos" in my_dict)
print("Apellido" in my_dict)
print(my_dict["Apellido"])

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, "Antonio")
print(my_new_dict)

my_values = my_new_dict.values()
print(my_values)
print(type(my_values))

print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))