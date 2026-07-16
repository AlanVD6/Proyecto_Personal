from database import DATA

OPERADORES = {
    "=": lambda a, b: a == b,
    "!=": lambda a, b: a != b,
    "<": lambda a, b: a < b,
    ">": lambda a, b: a > b,
    "<=": lambda a, b: a <= b,
    ">=": lambda a, b: a >= b,
}

def evaluar_condicion(registro: dict, condicion: dict) -> bool:
    resultados = []
    for expr in condicion["expresiones"]:
        valor_registro = registro[expr["columna"]]
        comparar = OPERADORES[expr["operador"]]
        resultados.append(comparar(valor_registro, expr["valor"]))

    resultado_final = resultados[0]
    for i, conector in enumerate(condicion["conectores"]):
        siguiente = resultados[i + 1]
        if conector == "AND":
            resultado_final = resultado_final and siguiente
        else:  # OR
            resultado_final = resultado_final or siguiente

    return resultado_final


def ejecutar_consulta(ast: dict):
    tabla = ast["from"]
    registros = DATA[tabla]

    if ast["where"]:
        registros = [r for r in registros if evaluar_condicion(r, ast["where"])]

    if ast["columns"] == ["*"]:
        return registros

    return [{col: r[col] for col in ast["columns"]} for r in registros]