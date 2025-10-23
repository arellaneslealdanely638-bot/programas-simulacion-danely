
# Programa de metodo congruencial lineal
#este programa genera una secuencia de números pseudoaleatorios

# pseudoaleatorios usando la fórmula:
# Fórmula: Xn+1 = (a * Xn + c) % m


# Se piden los datos al usuario

semilla = int(input("Ingresa la semilla: ")) # valor inicial
a = int(input("Ingresa el valor de a: ")) # multiplicativo
c = int(input("Ingresa el valor de c: ")) #incremento
m = int(input("Ingresa el valor de m: ")) # metodo( limita el rago de los numeros)
n = int(input("Cuántos números quieres generar: ")) # cantidad de numeros


# Se inicia con la semilla

x = semilla

print("\n--- MÉTODO CONGRUENCIAL LINEAL ---\n")

# Ciclo que genera los números
for i in range(n):
    
     # Aplicamos la fórmula del método
    x = (a * x + c) % m
    
    # Se muestra cada número generado
    print(f"Número {i+1}: {x}")
