from database import SCHEMA

def verificar_semantica(ast: dict):
    
    errores = []
    tabla = ast["from"]

    if tabla not in SCHEMA:
        errores.append(f"La tabla '{tabla}' no existe en el esquema.")
        return errores 

    columnas_validas = SCHEMA[tabla]

    if ast["columns"] != ["*"]:
        for columna in ast["columns"]:
            if columna not in columnas_validas:
                errores.append(
                    f"La columna '{columna}' no existe en la tabla '{tabla}'."
                )

    if ast["where"]:
        for expr in ast["where"]["expresiones"]:
            if expr["columna"] not in columnas_validas:
                errores.append(
                    f"La columna '{expr['columna']}' usada en WHERE no existe en la tabla '{tabla}'."
                )

    return errores