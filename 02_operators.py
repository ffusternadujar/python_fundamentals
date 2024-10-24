### Operadores ###

print("1. Aritmeticos")

print(3 - 2)
print(3 * 2)
print(3 / 2)
print(10 % 4)
print(10 // 4) # Floor division
print(2 ** 3) # to the power of
print(2 ** 3 + 3 - 7 / 1 // 4)



print("2. Concatenación")

print("Hola" + "Python")
print("Hola" + str(5))
print("Hola" * 5)
print("Hola" * int(2 ** 3 + 3 - 7 / 1 // 4))


print('3. Comparación')

print(3 > 2)
print(3 < 2)
print(3 >= 2)
print(3 <= 2)
print(3 == 2)
print(3 != 2)
print(3 > 2 <= 5)

print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

print('aaab' >= 'aaaa') # Compara en una ordenación alfábetica cual es mayor en función de ASCII
print('aaab' >= 'aaac') # Compara en una ordenación alfábetica cual es mayor en función de ASCII


print('4. Lógicos')

print(3 > 4 and "Hola" > "Phython")
print(3 > 4 or "Hola" > "Phython")
print(3 < 4 and "Hola" < "Phython")
print(3 < 4 or "Hola" < "Phython")
print(3 < 4 and "Hola" > "Phython")
print(3 < 4 or "Hola" > "Phython")
print(1 > 1 and not "Hola" > "Phython")