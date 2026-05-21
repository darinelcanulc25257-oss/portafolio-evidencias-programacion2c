def calcularmedia(*args):
    """
    Devuelve el valor de la media o promedio de un conjunto de datos numericos.

    args:
        *args:(int): un nuevo numero variable de argumentos que representan los datos numericos.

    return:
        (float): el valor de la media o promedio de los datos numericos.
    """
    return sum(args) / len(*args)

assert(calcularmedia(3, 5, 4) == 4.0)
assert(calcularmedia(10, 20, 30) == 20.0)
assert(calcularmedia(1, 2, 3, 4, 5) == 3.0)