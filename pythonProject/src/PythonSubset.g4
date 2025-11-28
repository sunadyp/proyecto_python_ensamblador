grammar PythonSubset;


program
    : (functionDef | statement)* EOF
    ;

// Definición de función: def nombre(arg1, arg2) { codigo }
functionDef
    : 'def' ID '(' parameterList? ')' block
    ;

// Lista de parámetros: a, b, c
parameterList
    : ID (',' ID)*
    ;

statement
    : assignmentStmt
    | printStmt
    | ifStmt
    | whileStmt
    | returnStmt    // Nueva sentencia para funciones
    | functionCall  // Llamada a función como sentencia
    | block
    ;

assignmentStmt
    : ID '=' expression
    ;

printStmt
    : 'print' '(' expression ')'
    ;

ifStmt
    : 'if' expression ':' statement ('else' ':' statement)?
    ;

whileStmt
    : 'while' expression ':' statement
    ;

returnStmt
    : 'return' expression?
    ;

block
    : '{' statement* '}'
    ;

expression
    : expression ('*' | '/') expression      # MulDiv
    | expression ('+' | '-') expression      # AddSub
    | expression ('>' | '<' | '==') expression # Relational
    | ID '(' expressionList? ')'             # FunctionCallExpr
    | STRING                                 # StringLiteral
    | INT                                    # Number
    | ID                                     # Id
    | '(' expression ')'                     # Parens
    ;

// Lista de argumentos para llamar función: (1, x, 3)
expressionList
    : expression (',' expression)*
    ;

// Llamada a función aislada (para usarla en statement)
functionCall
    : ID '(' expressionList? ')'
    ;

// LEXER (Tokens)

DEF     : 'def';
RETURN  : 'return';
IF      : 'if';
ELSE    : 'else';
WHILE   : 'while';
PRINT   : 'print';
STRING  : '"' .*? '"' ;
ID      : [a-zA-Z_] [a-zA-Z0-9_]* ;
INT     : [0-9]+ ;
COMMENT : '#' ~[\r\n]* -> skip ;
WS      : [ \t\r\n]+ -> skip ;

// Operadores y símbolos
PLUS    : '+';
MINUS   : '-';
MUL     : '*';
DIV     : '/';
ASSIGN  : '=';
LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
COLON   : ':';
COMMA   : ',';
GT      : '>';
LT      : '<';
EQ      : '==';