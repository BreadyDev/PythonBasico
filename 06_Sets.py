### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Antonio", "Ramos", 20}
print(my_other_set)
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Toño")
print(my_other_set)

my_other_set.add("Toño") # No admite repetidos
print(my_other_set)

print("Ramos" in my_other_set)
print("Ramoz" in my_other_set)

my_other_set.remove("Ramos")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))
print(my_other_set)

del(my_other_set)
#print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Antonio", "Ramos", 20}
my_list = list(my_set)
print(type(my_set))
print(my_set)
print(type(my_list))
print(my_list)
print(my_list[0])

my_other_set = {"Java", "Python", "SQLServer", "HTML", "CSS"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union(my_new_set).union(my_set).union(my_other_set).union({"C#", "javaScript"}))

print(my_new_set.difference(my_set))
print(my_new_set.intersection(my_set))