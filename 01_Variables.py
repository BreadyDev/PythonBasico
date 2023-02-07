# Variables

mi_variable = "Variable de String"
print(mi_variable)

mi_variable = 4
num_1: int = int(mi_variable)
num_2: float = 2.5
num_3: int = num_1 + num_2

mi_variable = str(num_1) + " + " + str(num_2) + " = " + str(num_3)
print(mi_variable)

print(len(mi_variable))
print(type(len(mi_variable)))

nom, ap, alias, edad = "Antonio", "Ramos", "Toño", 20
print("Me llamo: ", nom, ap, ". Mi edad es:", edad,". Y mi alias es:", alias)

nom = input("¿Cómo te llamas? ")
ap = input("¿Cúal es tu apellido? ")
alias = input("¿Cúal es tu alias? ")
edad = input("¿Cúal es tu edad? ")

print("Te llamas: ", nom, ap, ". Tu edad es:", edad,". Y tu alias es:", alias)