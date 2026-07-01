# Generador Congruencial Lineal
# Parámetros
m = 4096
a = 5
c = 1
semilla = 1234  # Puedes cambiarla

# Archivo de salida
archivo = open("resultados_generador.txt", "w")
archivo.write(f"Semilla: {semilla}\n")
archivo.write(f"a (multiplicador): {a}\n")
archivo.write(f"c (incremento): {c}\n")
archivo.write(f"m (módulo): {m}\n")
archivo.write("Números generados:\n")

# Generar período completo (4096 números)
x = semilla
numeros = []
for i in range(m):  # m = 4096 iteraciones
    x = (a * x + c) % m
    numeros.append(x)
    archivo.write(f"{i+1}: {x}\n")

archivo.close()

# Verificar que todos los números son distintos (período completo)
if len(set(numeros)) == m:
    print(f" Período completo de {m} números generado exitosamente.")
else:
    print(" No se obtuvo período completo. Revisa parámetros.")