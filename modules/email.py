from re import match

def gmail(email):
    # Expresión regular para verificar que el email es un Gmail
    patron = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    # Verifica si el email coincide con el patrón
    return match(patron, email) is not None

# print(email('efhesioufhs'))