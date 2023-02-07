# Strings #

string_1:str = "Mi string"
string_2:str = "Mi otro string"

print(len(string_1))
print(len(string_2))

print(string_1 + " " + string_2)

string_ln:str = "Esto es un string\ncon salto de linea"
print(string_ln)

string_tab:str = "\tEsto es un string con tabulacion"
print(string_tab)

string_esc:str = "\tEsto es un string\nescapado"
print(string_esc)

nom, ap, edad = "Antonio", "Ramos", 20
print("Mi nombre es {} {} y tengo {} años".format(nom, ap, edad))
print("Mi nombre es %s %s y tengo %d años" %(nom, ap, edad))
print("Mi nombre es " + nom + " " + ap + " y tengo " + str(edad) +" años")
print(f"Mi nombre es {nom} {ap} y tengo {edad} años")

# Desempaquetado de caracteres #

language = "Python"
a, b, c, d, e, f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Divicion #

language_slice = language[1:2]
print(language_slice)

language_slice = language[2:]
print(language_slice)

language_slice = language[2]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reversa #
reversed_language = language[::-1]
print(reversed_language)

# Funciones #

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1212".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("py"))

#  Palindroma #

palabra:str = input("\nPalabra: ")
print((palabra.lower().replace(" ", ""))[::-1]==palabra)