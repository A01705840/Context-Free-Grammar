import nltk
from nltk import CFG
nltk.download('punkt')

# Define a context-free grammar
grammar = CFG.fromstring("""
    S -> 'PROGRAM' ID 'BEGIN' DCL STL 'END'
    ID -> [a-z A-Z][a-z A-Z 0-9_]
    DCL -> DECL DCLP
    DCLP -> DECL DCLP
    DCLP ->
    DECL -> 'DCL' ID TYPE 'INIT' VAL
    TYPE -> 'REAL' | 'INT' | 'BOOL' | 'CHAR' | 'STRING'
    VAL -> LIT | ID
    STL -> ST STLP
    STLP -> ST STLP
    STLP ->
    ST -> 'CALL' ID '(' ARG ');' | 'IF' CONDITION 'THEN' ST 'ELSE' ST 'ENDIF' | 'PRINT (' EXP ');'
    ARG -> EXP ARGP
    ARGP -> EXP ARGP
    ARGP ->
    CONDITION -> EXP RELOP EXP
    EXP -> TERM ADDOP EXP | TERM
    TERM -> FACTOR MULTOP TERM | FACTOR
    FACTOR -> LIT | ID | '(' EXP ')'
    LIT -> INTLIT | REALLIT | STRLIT | BOOLLIT | CHARLIT
    INTLIT -> [0-9]+
    REALLIT -> INTLIT'.'INTLIT
    STRLIT -> '"'[a-zA-Z0-9?¿!¡_.,]'"'
    BOOLLIT -> 'TRUE' | 'FALSE'
    CHARLIT -> [A-Z]
    ADDOP -> + | -
    MULTOP -> * | /
    RELOP -> < | > | <= | >= | ==
""")

# Create a parser with the defined grammar
parser = nltk.ChartParser(grammar)

# Input sentence to be parsed
sentence = ""

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Parse the sentence
for tree in parser.parse(tokens):
    tree.pretty_print()
