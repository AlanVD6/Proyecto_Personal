import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "generated"))

from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from miniSQLLexer import miniSQLLexer
from miniSQLParser import miniSQLParser
from miniSQLVisitor import miniSQLVisitor

class ColectorDeErrores(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errores.append(f"Línea {line}, columna {column}: {msg}")


class ASTBuilder(miniSQLVisitor):
    def visitQuery(self, ctx):
        columnas = self.visit(ctx.columns())
        tabla = ctx.table_name().getText()
        condicion = self.visit(ctx.condition()) if ctx.condition() else None
        return {"columns": columnas, "from": tabla, "where": condicion}

    def visitColumns(self, ctx):
        if ctx.STAR():
            return ["*"]
        return [c.getText() for c in ctx.column()]

    def visitCondition(self, ctx):
        expresiones = [self.visit(e) for e in ctx.expr()]
        conectores = [op.getText().upper() for op in ctx.logic_op()]
        return {"expresiones": expresiones, "conectores": conectores}

    def visitExpr(self, ctx):
        columna = ctx.ID().getText()
        operador = ctx.op().getText()
        valor_texto = ctx.value().getText()

        if ctx.value().INT():
            valor = int(valor_texto)
        else:
            valor = valor_texto.strip("'")

        return {"columna": columna, "operador": operador, "valor": valor}

def parsear(consulta: str):

    input_stream = InputStream(consulta)
    lexer = miniSQLLexer(input_stream)
    lexer.removeErrorListeners()
    colector_lexer = ColectorDeErrores()
    lexer.addErrorListener(colector_lexer)

    stream = CommonTokenStream(lexer)
    parser = miniSQLParser(stream)
    parser.removeErrorListeners()
    colector_parser = ColectorDeErrores()
    parser.addErrorListener(colector_parser)

    arbol = parser.query()

    errores = colector_lexer.errores + colector_parser.errores
    if errores:
        return None, errores

    ast = ASTBuilder().visit(arbol)
    return ast, []