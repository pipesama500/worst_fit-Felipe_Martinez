def worst_fit(memoria_trabajo, req, index):

    # Si la lista está vacía
    if not memoria_trabajo:
        return None

    n = len(memoria_trabajo)
    indice_asignado = -1
    max_limite = -1

    # Buscar el segmento con el límite más grande que pueda contener la solicitud
    for i in range(index, n):
        base, limite = memoria_trabajo[i]
        if limite >= req and limite > max_limite:
            max_limite = limite
            indice_asignado = i

    # Si no se encuentra buscar desde el inicio
    if indice_asignado == -1:
        for i in range(index):
            base, limite = memoria_trabajo[i]
            if limite >= req and limite > max_limite:
                max_limite = limite
                indice_asignado = i
    # Si se encuentra un segmento válido, devolver la base y el índice
    if indice_asignado != -1:
        base_asignada = memoria_trabajo[indice_asignado][0]
        return base_asignada, indice_asignado
    else:
        return None # No hay suficiente memoria para la asignación