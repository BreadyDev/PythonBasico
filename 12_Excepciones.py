### Excepciones ###

num_1 = 5
num_2 = 1
#num_2 = "1"

try:
    print(num_1+ num_2)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
    
    
try:
    print(num_1 + num_2)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    print("La ejecución continúa correctamente")
finally:
    print("La ejecución continúa")
  
try:
    print(num_1 + num_2)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)