def formato_nombre(name , lasname):
    """
    Devuelve el nombre de usuario en el formato apellido , nombre.

    Argumentos:
        name (str): Primer nombre de usuario
        lasname (str): Apellido paterno del usuario

    Retorno:
        (str): EL nombre completo en formato Apellido, Nombre.
    """
    return f"{lasname},{name}"

#funcion main para ejecución del código. 
def main():
    _name=input("introduce tu nombre")
    _lasname=input("introduce tu apellido paterno")
    print(formato_nombre(_name,_lasname))
    
if __name__ == "__main__":
    main()