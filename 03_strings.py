### Strings ###

my_string = 'My string'
my_other_string = "My other string"

print(len(my_string))
print(len(my_other_string))

print(my_other_string + ' ' + my_other_string)

my_new_line_string = 'This is an string\nwith a new line'
print(my_new_line_string)

my_tab_line_string = '\tThis is an string with tabulation'
print(my_tab_line_string)

my_scape_string = 'This is an String \\n whit new line scaped'
print(my_scape_string)

# Format Strings
name, surname, age = 'Francisco', 'Fuster', 42
print('My name is {} {} and I am {:d} years old'.format(name, surname, age))
print('My name is %s %s and I am %d years old' %(name, surname, age))
print(f'My name is {name} {surname} and I am {age} years old')

# Unpackaging characters
language = 'python'
a, b, c, d, e, f = language

print(a)
print(b)
print(e)

# Split

languaje_slice = language[1:3]
print(languaje_slice)

languaje_slice = language[1:]
print(languaje_slice)

languaje_slice = language[:4]
print(languaje_slice)

languaje_slice = language[-2:]
print(languaje_slice)

languaje_slice = language[-2]
print(languaje_slice)

languaje_slice = language[0:6:2]
print(languaje_slice)

# Reverse
reverse_language = language[::-1]
print(reverse_language)

# Functions
print(len(language))
print(language.capitalize())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print("TEST".lower())
print("test".upper().isupper())
print(language.replace("t", "f"))