# Método del Cuadrado Medio


def cuadrado_medio(semilla, n):
    """
    Genera una secuencia de números pseudoaleatorios
    usando el método del cuadrado medio.
    """
    print("\n--- MÉTODO DEL CUADRADO MEDIO ---\n")
    x = semilla
    for i in range(n):
        # 1️⃣ Elevar al cuadrado
        cuadrado = x * x

        # 2️⃣ Convertir a cadena con ceros al inicio (para mantener longitud uniforme)
        cuadrado_str = str(cuadrado).zfill(8)

        # 3️⃣ Extraer los 4 dígitos centrales
        medio = cuadrado_str[2:6]

        # 4️⃣ Convertir el resultado a número
        x = int(medio)

        # 5️⃣ Mostrar resultado
        print(f"Iteración {i+1}: cuadrado = {cuadrado_str}, medio = {medio}")

# --- Programa principal ---
# Pedir datos al usuario
semilla = int(input("Ingrese la semilla inicial (4 dígitos): "))
n = int(input("Ingrese cuántos números desea generar: "))

# Llamar a la función
cuadrado_medio(semilla, n)