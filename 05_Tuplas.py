### Tuplas ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (20, 1.72, "Antonio", "Ramos", "Python")
my_other_tuple = (20, 35, 60)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])


print(my_tuple.count("Ramos"))
print(my_tuple.index("Antonio"))

"""
my_tuple[1] = 1.75
print(my_tuple)
"""

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Itocotlan"
my_tuple.insert(2, "Azul")
print(my_tuple)

my_tuple = tuple(my_tuple)
print(type(my_tuple))
print(my_tuple)

#del my_tuple[0] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined