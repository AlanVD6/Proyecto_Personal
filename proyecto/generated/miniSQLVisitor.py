# Generated from grammar/miniSQL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .miniSQLParser import miniSQLParser
else:
    from miniSQLParser import miniSQLParser

# This class defines a complete generic visitor for a parse tree produced by miniSQLParser.

class miniSQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by miniSQLParser#query.
    def visitQuery(self, ctx:miniSQLParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#columns.
    def visitColumns(self, ctx:miniSQLParser.ColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#column.
    def visitColumn(self, ctx:miniSQLParser.ColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#table_name.
    def visitTable_name(self, ctx:miniSQLParser.Table_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#condition.
    def visitCondition(self, ctx:miniSQLParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#expr.
    def visitExpr(self, ctx:miniSQLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#op.
    def visitOp(self, ctx:miniSQLParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#value.
    def visitValue(self, ctx:miniSQLParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#logic_op.
    def visitLogic_op(self, ctx:miniSQLParser.Logic_opContext):
        return self.visitChildren(ctx)



del miniSQLParser