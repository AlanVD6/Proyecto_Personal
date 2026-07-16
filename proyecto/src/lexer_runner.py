import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "generated"))

from antlr4 import InputStream, CommonTokenStream
from miniSQLLexer import miniSQLLexer

def obtener_tokens(consulta: str):
    input_stream = InputStream(consulta)
    lexer = miniSQLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    stream.fill()

    tokens = []
    for token in stream.tokens:
        if token.type == -1:  # EOF
            continue
        nombre_tipo = lexer.symbolicNames[token.type]
        tokens.append({
            "tipo": nombre_tipo,
            "lexema": token.text,
        })
    return tokens