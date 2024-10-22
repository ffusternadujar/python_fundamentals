# Variables

my_string_variable = 'My String Variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)
print(type(my_int_variable))

my_int_to_str_variable = str(my_int_variable)
print(my_int_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, str(my_int_variable), my_bool_variable)
print('Concatenando:', my_string_variable)

# Algunas funciones del sistema
print(len(my_string_variable))
print('Este es el valor de:', my_bool_variable)

# Variables en una sola linea. ¡Ojo con el uso!
name, surname, alias, age = 'Francisco', 'Fuster', 'ffuster', 42
print('Me llamo:', name, surname, '.Mi edad es:', age, '.Y mi alias es:', alias)

# Inputs
'''
name = input('¿Cuál es tu nombre?: ')
print(name)
'''

# Cambios de tipo
name = 42
print(name)
age = 'Francisco'
print(age)

# ¿Forzamos el tipo?
address: str = 'Mi dirección'
address = 5
print(type(address))