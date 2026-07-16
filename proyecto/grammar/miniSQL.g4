grammar miniSQL;

query : SELECT columns FROM table_name (WHERE condition)? EOF ;
columns : POR| column (COMA column)* ;
column : ID ;
table_name : ID ;

condition : expr (logic_op expr)* ;

expr : ID op value ;

op : IGUAL | DIFERENTE | MENOR_QUE | MAYOR_QUE | MENOR_IGUAL | MAYOR_IGUAL ;

value : INT | STRING ;

logic_op : AND | OR ;

// REGLAS DEL LEXER 
SELECT : [Ss][Ee][Ll][Ee][Cc][Tt] ;
FROM   : [Ff][Rr][Oo][Mm] ;
WHERE  : [Ww][Hh][Ee][Rr][Ee] ;
AND    : [Aa][Nn][Dd] ;
OR     : [Oo][Rr] ;

POR   : '*' ;
COMA : ',' ;

IGUAL       : '=' ;
DIFERENTE   : '!=' ;
MENOR_QUE   : '<' ;
MAYOR_QUE   : '>' ;
MENOR_IGUAL : '<=' ;
MAYOR_IGUAL : '>=' ;

INT    : [0-9]+ ;
STRING : '\'' (~['])* '\'' ;
ID     : [a-zA-Z_][a-zA-Z_0-9]* ;

WS : [ \t\r\n]+ -> skip ;