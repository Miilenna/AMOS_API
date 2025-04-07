# Función que devuelve una lista de diccionarios con una clave 'text' y el valor correspondiente a 'paraula'
def paraula_schema(paraula) -> list:
    return [{"text":paraula}]
# Función que devuelve una lista de diccionarios a partir de una lista
def word_schema(words) -> dict:
    return [{"text": word} for word in words]