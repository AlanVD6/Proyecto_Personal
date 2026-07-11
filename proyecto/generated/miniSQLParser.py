# Generated from grammar/miniSQL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,63,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,0,1,0,1,0,3,0,25,8,0,1,0,1,0,1,1,
        1,1,1,1,1,1,5,1,33,8,1,10,1,12,1,36,9,1,3,1,38,8,1,1,2,1,2,1,3,1,
        3,1,4,1,4,1,4,1,4,5,4,48,8,4,10,4,12,4,51,9,4,1,5,1,5,1,5,1,5,1,
        6,1,6,1,7,1,7,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,3,1,0,8,
        13,1,0,14,15,1,0,4,5,57,0,18,1,0,0,0,2,37,1,0,0,0,4,39,1,0,0,0,6,
        41,1,0,0,0,8,43,1,0,0,0,10,52,1,0,0,0,12,56,1,0,0,0,14,58,1,0,0,
        0,16,60,1,0,0,0,18,19,5,1,0,0,19,20,3,2,1,0,20,21,5,2,0,0,21,24,
        3,6,3,0,22,23,5,3,0,0,23,25,3,8,4,0,24,22,1,0,0,0,24,25,1,0,0,0,
        25,26,1,0,0,0,26,27,5,0,0,1,27,1,1,0,0,0,28,38,5,6,0,0,29,34,3,4,
        2,0,30,31,5,7,0,0,31,33,3,4,2,0,32,30,1,0,0,0,33,36,1,0,0,0,34,32,
        1,0,0,0,34,35,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,37,28,1,0,0,0,
        37,29,1,0,0,0,38,3,1,0,0,0,39,40,5,16,0,0,40,5,1,0,0,0,41,42,5,16,
        0,0,42,7,1,0,0,0,43,49,3,10,5,0,44,45,3,16,8,0,45,46,3,10,5,0,46,
        48,1,0,0,0,47,44,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,
        0,50,9,1,0,0,0,51,49,1,0,0,0,52,53,5,16,0,0,53,54,3,12,6,0,54,55,
        3,14,7,0,55,11,1,0,0,0,56,57,7,0,0,0,57,13,1,0,0,0,58,59,7,1,0,0,
        59,15,1,0,0,0,60,61,7,2,0,0,61,17,1,0,0,0,4,24,34,37,49
    ]

class miniSQLParser ( Parser ):

    grammarFileName = "miniSQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'*'", "','", "'='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='" ]

    symbolicNames = [ "<INVALID>", "SELECT", "FROM", "WHERE", "AND", "OR", 
                      "STAR", "COMMA", "EQ", "NEQ", "LT", "GT", "LEQ", "GEQ", 
                      "INT", "STRING", "ID", "WS" ]

    RULE_query = 0
    RULE_columns = 1
    RULE_column = 2
    RULE_table_name = 3
    RULE_condition = 4
    RULE_expr = 5
    RULE_op = 6
    RULE_value = 7
    RULE_logic_op = 8

    ruleNames =  [ "query", "columns", "column", "table_name", "condition", 
                   "expr", "op", "value", "logic_op" ]

    EOF = Token.EOF
    SELECT=1
    FROM=2
    WHERE=3
    AND=4
    OR=5
    STAR=6
    COMMA=7
    EQ=8
    NEQ=9
    LT=10
    GT=11
    LEQ=12
    GEQ=13
    INT=14
    STRING=15
    ID=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(miniSQLParser.SELECT, 0)

        def columns(self):
            return self.getTypedRuleContext(miniSQLParser.ColumnsContext,0)


        def FROM(self):
            return self.getToken(miniSQLParser.FROM, 0)

        def table_name(self):
            return self.getTypedRuleContext(miniSQLParser.Table_nameContext,0)


        def EOF(self):
            return self.getToken(miniSQLParser.EOF, 0)

        def WHERE(self):
            return self.getToken(miniSQLParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(miniSQLParser.ConditionContext,0)


        def getRuleIndex(self):
            return miniSQLParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = miniSQLParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(miniSQLParser.SELECT)
            self.state = 19
            self.columns()
            self.state = 20
            self.match(miniSQLParser.FROM)
            self.state = 21
            self.table_name()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 22
                self.match(miniSQLParser.WHERE)
                self.state = 23
                self.condition()


            self.state = 26
            self.match(miniSQLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(miniSQLParser.STAR, 0)

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniSQLParser.ColumnContext)
            else:
                return self.getTypedRuleContext(miniSQLParser.ColumnContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(miniSQLParser.COMMA)
            else:
                return self.getToken(miniSQLParser.COMMA, i)

        def getRuleIndex(self):
            return miniSQLParser.RULE_columns

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumns" ):
                listener.enterColumns(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumns" ):
                listener.exitColumns(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumns" ):
                return visitor.visitColumns(self)
            else:
                return visitor.visitChildren(self)




    def columns(self):

        localctx = miniSQLParser.ColumnsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_columns)
        self._la = 0 # Token type
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.match(miniSQLParser.STAR)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.column()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 30
                    self.match(miniSQLParser.COMMA)
                    self.state = 31
                    self.column()
                    self.state = 36
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(miniSQLParser.ID, 0)

        def getRuleIndex(self):
            return miniSQLParser.RULE_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn" ):
                listener.enterColumn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn" ):
                listener.exitColumn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn" ):
                return visitor.visitColumn(self)
            else:
                return visitor.visitChildren(self)




    def column(self):

        localctx = miniSQLParser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_column)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(miniSQLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(miniSQLParser.ID, 0)

        def getRuleIndex(self):
            return miniSQLParser.RULE_table_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_name" ):
                listener.enterTable_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_name" ):
                listener.exitTable_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable_name" ):
                return visitor.visitTable_name(self)
            else:
                return visitor.visitChildren(self)




    def table_name(self):

        localctx = miniSQLParser.Table_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_table_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(miniSQLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniSQLParser.ExprContext)
            else:
                return self.getTypedRuleContext(miniSQLParser.ExprContext,i)


        def logic_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniSQLParser.Logic_opContext)
            else:
                return self.getTypedRuleContext(miniSQLParser.Logic_opContext,i)


        def getRuleIndex(self):
            return miniSQLParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = miniSQLParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.expr()
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4 or _la==5:
                self.state = 44
                self.logic_op()
                self.state = 45
                self.expr()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(miniSQLParser.ID, 0)

        def op(self):
            return self.getTypedRuleContext(miniSQLParser.OpContext,0)


        def value(self):
            return self.getTypedRuleContext(miniSQLParser.ValueContext,0)


        def getRuleIndex(self):
            return miniSQLParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = miniSQLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(miniSQLParser.ID)
            self.state = 53
            self.op()
            self.state = 54
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(miniSQLParser.EQ, 0)

        def NEQ(self):
            return self.getToken(miniSQLParser.NEQ, 0)

        def LT(self):
            return self.getToken(miniSQLParser.LT, 0)

        def GT(self):
            return self.getToken(miniSQLParser.GT, 0)

        def LEQ(self):
            return self.getToken(miniSQLParser.LEQ, 0)

        def GEQ(self):
            return self.getToken(miniSQLParser.GEQ, 0)

        def getRuleIndex(self):
            return miniSQLParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)




    def op(self):

        localctx = miniSQLParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(miniSQLParser.INT, 0)

        def STRING(self):
            return self.getToken(miniSQLParser.STRING, 0)

        def getRuleIndex(self):
            return miniSQLParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = miniSQLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logic_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(miniSQLParser.AND, 0)

        def OR(self):
            return self.getToken(miniSQLParser.OR, 0)

        def getRuleIndex(self):
            return miniSQLParser.RULE_logic_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_op" ):
                listener.enterLogic_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_op" ):
                listener.exitLogic_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_op" ):
                return visitor.visitLogic_op(self)
            else:
                return visitor.visitChildren(self)




    def logic_op(self):

        localctx = miniSQLParser.Logic_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_logic_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





