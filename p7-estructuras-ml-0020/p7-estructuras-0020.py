# Jonathan Baray 0020
# ==============================================================================
# PRÁCTICA 7: ESTRUCTURAS DE DECISIÓN Y REPETICIÓN
# Archivo: p7-extructuras-0020.py
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. CONDICIONES (Python IF)
# ------------------------------------------------------------------------------
print("=== 1. CONDICIONES (IF) ===")

# Ejemplo 1
a = 33
b = 200
if b > a:
    print("Ejemplo 1: b es mayor que a")

# Ejemplo 2
edad = 18
if edad >= 18:
    print("Ejemplo 2: Es mayor de edad")

print()

# ------------------------------------------------------------------------------
# 2. IF...ELIF
# ------------------------------------------------------------------------------
print("=== 2. IF...ELIF ===")

# Ejemplo 1
a = 33
b = 33
if b > a:
    print("Ejemplo 1: b es mayor que a")
elif a == b:
    print("Ejemplo 1: a y b son iguales")

# Ejemplo 2
calificacion = 85
if calificacion >= 90:
    print("Ejemplo 2: Excelente")
elif calificacion >= 80:
    print("Ejemplo 2: Buen trabajo")

print()

# ------------------------------------------------------------------------------
# 3. IF...ELSE
# ------------------------------------------------------------------------------
print("=== 3. IF...ELSE ===")

# Ejemplo 1
a = 200
b = 33
if b > a:
    print("Ejemplo 1: b es mayor que a")
elif a == b:
    print("Ejemplo 1: a y b son iguales")
else:
    print("Ejemplo 1: a es mayor que b")

# Ejemplo 2
temperatura = 15
if temperatura > 20:
    print("Ejemplo 2: Hace calor")
else:
    print("Ejemplo 2: Hace frío")

print()

# ------------------------------------------------------------------------------
# 4. CICLO FOR (Python For Loops)
# ------------------------------------------------------------------------------
print("=== 4. CICLO FOR ===")

# Ejemplo 1: Recorrer una lista
frutas = ["manzana", "banana", "cereza"]
print("Ejemplo 1 (Lista):")
for x in frutas:
    print(x)

# Ejemplo 2: Usando la función range()
print("Ejemplo 2 (Range):")
for i in range(5):
    print(f"Número: {i}")

print()

# ------------------------------------------------------------------------------
# 5. CICLO WHILE (Python While Loops)
# ------------------------------------------------------------------------------
print("=== 5. CICLO WHILE ===")

# Ejemplo 1: Contador simple
print("Ejemplo 1:")
i = 1
while i < 6:
    print(i)
    i += 1

# Ejemplo 2: Uso de la instrucción break
print("Ejemplo 2 (con break):")
j = 1
while j < 10:
    print(j)
    if j == 3:
        break
    j += 1

    print("Jonathan Baray  NC 0020")