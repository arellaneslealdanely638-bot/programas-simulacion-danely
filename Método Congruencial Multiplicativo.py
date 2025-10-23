# Método Congruencial Multiplicativo


# Fórmula: Xn+1 = (a * Xn) mod m

def multiplicativo(a, semilla, m, n):
    print("\n--- MÉTODO CONGRUENCIAL MULTIPLICATIVO ---\n")
    x = semilla
    for i in range(n):
        x = (a * x) % m   # Se aplica la fórmula
        print(f"Número {i+1}: {x}")  # Se muestra cada número generado

# Pedir datos al usuario
a = int(input("Ingresa el valor del multiplicador (a): ")) # multiplicador
semilla = int(input("Ingresa la semilla (X0): ")) # (x0)valor inicial 
m = int(input("Ingresa el valor del módulo (m): ")) # modulos
n = int(input("Cuántos números deseas generar: ")) # cuantos numero voy a generar

# Llamar la función
multiplicativo(a, semilla, m, n)
