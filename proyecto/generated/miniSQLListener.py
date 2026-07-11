# Generated from grammar/miniSQL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .miniSQLParser import miniSQLParser
else:
    from miniSQLParser import miniSQLParser

# This class defines a complete listener for a parse tree produced by miniSQLParser.
class miniSQLListener(ParseTreeListener):

    # Enter a parse tree produced by miniSQLParser#query.
    def enterQuery(self, ctx:miniSQLParser.QueryContext):
        pass

    # Exit a parse tree produced by miniSQLParser#query.
    def exitQuery(self, ctx:miniSQLParser.QueryContext):
        pass


    # Enter a parse tree produced by miniSQLParser#columns.
    def enterColumns(self, ctx:miniSQLParser.ColumnsContext):
        pass

    # Exit a parse tree produced by miniSQLParser#columns.
    def exitColumns(self, ctx:miniSQLParser.ColumnsContext):
        pass


    # Enter a parse tree produced by miniSQLParser#column.
    def enterColumn(self, ctx:miniSQLParser.ColumnContext):
        pass

    # Exit a parse tree produced by miniSQLParser#column.
    def exitColumn(self, ctx:miniSQLParser.ColumnContext):
        pass


    # Enter a parse tree produced by miniSQLParser#table_name.
    def enterTable_name(self, ctx:miniSQLParser.Table_nameContext):
        pass

    # Exit a parse tree produced by miniSQLParser#table_name.
    def exitTable_name(self, ctx:miniSQLParser.Table_nameContext):
        pass


    # Enter a parse tree produced by miniSQLParser#condition.
    def enterCondition(self, ctx:miniSQLParser.ConditionContext):
        pass

    # Exit a parse tree produced by miniSQLParser#condition.
    def exitCondition(self, ctx:miniSQLParser.ConditionContext):
        pass


    # Enter a parse tree produced by miniSQLParser#expr.
    def enterExpr(self, ctx:miniSQLParser.ExprContext):
        pass

    # Exit a parse tree produced by miniSQLParser#expr.
    def exitExpr(self, ctx:miniSQLParser.ExprContext):
        pass


    # Enter a parse tree produced by miniSQLParser#op.
    def enterOp(self, ctx:miniSQLParser.OpContext):
        pass

    # Exit a parse tree produced by miniSQLParser#op.
    def exitOp(self, ctx:miniSQLParser.OpContext):
        pass


    # Enter a parse tree produced by miniSQLParser#value.
    def enterValue(self, ctx:miniSQLParser.ValueContext):
        pass

    # Exit a parse tree produced by miniSQLParser#value.
    def exitValue(self, ctx:miniSQLParser.ValueContext):
        pass


    # Enter a parse tree produced by miniSQLParser#logic_op.
    def enterLogic_op(self, ctx:miniSQLParser.Logic_opContext):
        pass

    # Exit a parse tree produced by miniSQLParser#logic_op.
    def exitLogic_op(self, ctx:miniSQLParser.Logic_opContext):
        pass



del miniSQLParser