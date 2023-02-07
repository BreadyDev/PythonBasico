### Funciones ###

def my_function():
    print("Esto es una función")
    
my_function()

def my_other_function(var):
    print(f"Variable: {var}")
    my_function()
    
my_other_function(15)

def sumar_valores(var_1, var_2):
    print(var_1 + var_2)
    
#sumar_valores(int(input("Primer numero: ")), int(input("Segundo numero: ")))
sumar_valores(5, 7)
sumar_valores(123124, 124313)
sumar_valores("5", "7")
sumar_valores(1.4, 5.2)

def sumar_valores_return(var_1, var_2):
    my_sum = var_1 + var_2
    return(my_sum)

my_result = sumar_valores(5, 7)
print(f"Suma: {my_result}")

my_result = sumar_valores_return(5, 7)
print(f"Suma: {my_result}")

def print_name(name, surname):
    print(f"Mi nombre es: {name} {surname}")
    
print_name(surname="Ramos", name="Antonio")

def print_name_default(name, surname, alias = "Sin alias"):
    print(f"Me llamo {name} {surname} o {alias}")
    
print_name_default("Antonio", "Ramos")
print_name_default("Antonio", "Ramos", "Toño")

def print_text(*texts):
    for text in texts:
        print(str(text).upper())
        
print_text("Lenguajes chidos:")
print_text("1: Java", "2: Python", "3: C")