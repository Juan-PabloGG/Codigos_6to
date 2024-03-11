def cuatro_reinas(fila):
    def conflicto(k):
        for i in range(1, k):
            if fila[i] == fila[k] or abs(fila[i] - fila[k]) == abs(i - k):
                return True
        return False

    k = 1  # Inicia en la columna 1
    # Inicia en el renglón 1
    fila[1] = 0 # Como fila(k) se incrementa antes de usarla, se hace fila(1) igual a 0
    while k > 0:
        fila[k] = fila[k] + 1  # Se busca un movimiento legal en la columna k

        while fila[k] <= 4 and conflicto(k):
            fila[k] = fila[k] + 1  # Se intenta en el siguiente renglón

        if fila[k] <= 4:
            if k == 4:
                return True  
            else:  # Siguiente columna
                k = k + 1
                if k <= 4:
                    fila[k] = 0  
        else:  # Regresar a columna anterior
            k = k - 1

    return False  # No hay solución

# Evidencia del arreglo final
fila = [0, 0, 0, 0, 0]  
solucion = cuatro_reinas(fila)

if solucion:
    print("Solución encontrada:", fila[1:5]) 
else:
    print("No hay solución")
"""
    [ ,X, , ] 2
    [ , , ,X] 4
    [X, , , ] 1
    [ , ,X, ] 3
"""
