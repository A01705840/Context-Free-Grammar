import nltk
from nltk import CFG

# Download necessary NLTK data
nltk.download('punkt')

# Define a context-free grammar
grammar = CFG.fromstring("""
    S -> 'PROGRAM' ID 'BEGIN' DCL STL 'END' ';'
    ID -> 'ExampleHAL' | 'ALTITUDE' | 'VELOCITY' | 'UpdateVelocity' | 'DisplayVelocity' | 'SUBROUTINE' | 'Altitude' | 'below' | 'above' | 'is' | CHAR ID
    DCL -> DECL DCLP
    DCLP -> DECL DCLP | 
    DECL -> 'DCL' ID TYPE 'INIT' '(' VAL ')' ';'
    TYPE -> 'REAL' | 'INT' | 'BOOL' | 'CHAR' | 'STRING'
    VAL -> LIT | ID
    STL -> ST STLP
    STLP -> ST STLP | 
    ST -> 'CALL' ID ';' | 'IF' CONDITION 'THEN' STL 'ELSE' STL 'ENDIF' ';' | 'PRINT' '(' EXP ')' ';' | 'SUBROUTINE' ID 'BEGIN' STL 'END' ';'
    CONDITION -> EXP RELOP EXP
    EXP -> TERM ADDOP EXP | TERM | ID
    TERM -> FACTOR MULTOP TERM | FACTOR
    FACTOR -> LIT | ID | '(' EXP ')'
    LIT -> INTLIT | REALLIT | STRLIT | BOOLLIT | CHARLIT
    INTLIT -> DIGIT INTLIT | DIGIT
    REALLIT -> INTLIT '.' INTLIT
    STRLIT -> '"' CHAR '"'
    BOOLLIT -> 'TRUE' | 'FALSE'
    CHAR -> 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z' | ' ' | '.' | '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '1000'
    CHARLIT -> CHAR | CHAR CHARLIT
    ADDOP -> '+' | '-' | '='
    MULTOP -> '*' | '/'
    RELOP -> '<' | '>' | '<=' | '>=' | '=='
    DIGIT -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '.'
""")

# Create a parser with the defined grammar
custom_parser = nltk.ChartParser(grammar)

# Define a custom tokenizer
def custom_tokenize(sentence):
    # Tokenize the sentence using nltk's word_tokenize
    tokens = nltk.word_tokenize(sentence)
    # Join tokens and then split by space to properly handle complex tokens
    joined = " ".join(tokens)
    # Manually add spaces around special characters to ensure they are tokenized correctly
    for char in '();,."<>=':
        joined = joined.replace(char, f' {char} ')
    return joined.split()

# Input sentences to be parsed
sentences = [
    """
    PROGRAM ExampleHAL BEGIN
        DCL ALTITUDE REAL INIT ( 0.0 ) ; 
        DCL VELOCITY REAL INIT ( 0.0 ) ; 
        CALL UpdateVelocity ; 
        END ;
    """
]

# Tokenize and parse each sentence using the custom tokenizer
for sentence in sentences:
    tokens = custom_tokenize(sentence.strip())
    print(f"Tokens for '{sentence.strip()}': {tokens}")
    trees = list(custom_parser.parse(tokens))
    if trees:
        print(f"Parse tree for '{sentence.strip()}':")
        for tree in trees:
            tree.pretty_print()
    else:
        print(f"No parse tree found for '{sentence.strip()}'")
