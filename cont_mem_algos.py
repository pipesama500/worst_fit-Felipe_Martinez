def worst_fit(mem_avail, req_size, index):
    if not mem_avail or req_size <= 0:
        return None

    n = len(mem_avail)
    max_index = -1
    max_limit = -1

    # Búsqueda desde el índice dado hasta el final (circularidad)
    for i in range(index, n):
        base, limit = mem_avail[i]
        if limit >= req_size and limit > max_limit:
            max_limit = limit
            max_index = i

    # Si no se encontró en el segmento inicial, buscar desde el principio hasta index
    if max_index == -1:
        for i in range(0, index):
            base, limit = mem_avail[i]
            if limit >= req_size and limit > max_limit:
                max_limit = limit
                max_index = i

    if max_index == -1:
        return None

    # Asignar memoria
    base, limit = mem_avail[max_index]
    new_base = base
    new_limit = req_size
    remaining_limit = limit - req_size

    # Actualizar lista de bloques
    if remaining_limit > 0:
        mem_avail[max_index] = (base + req_size, remaining_limit)
    else:
        del mem_avail[max_index]
    return mem_avail, new_base, new_limit, max_index
