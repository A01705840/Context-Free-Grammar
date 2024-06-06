# Context-Free-Grammar

Evidencia 2 para TC2037 Implementation of Computational Methods

## Description
The language that I will be using for the context-free-grammar is HAL/S.

HAL/S is a programming is a programming language for real time aerospace programming. It was produce for NASA Space Shuttle Flight Software. 

HAL/S was created with the intention of having reliability, efficiency and machine independence, this means less programming training, and reuse of blocks of code for other perojects, without the access of the aerrospace hardware. (Ryer, 1978) 

### RULES THAT'LL BE USED ON THE GRAMMAR
1. A program consists of a PROGRAM declaration followed by an identifier, the keyword BEGIN, a list of declarations, a list of statements, and finally the keyword END.
2. An identifier must start with a letter and can be followed by any combination of letters, digits, and underscores.
3. Declarations can be a sequence of one or more individual declarations or can be empty.
4. A declaration consists of the keyword DCL followed by an identifier, a type specifier, the keyword INIT, a value, and a semicolon.
5. Types include REAL, INT, BOOL, CHAR or STRING.
6. Values in declarations can be literals or identifiers.
7. Statements in the program are a sequence of one or more individual statements or can be empty.
8. Statements can be CALL statements, IF-ELSE statements, or PRINT statements.
9. A CALL statement consists of the keyword CALL followed by an identifier representing a subroutine, followed by arguments enclosed in parentheses, and ends with a semicolon.
10. An IF-ELSE statement begins with the keyword IF followed by a condition, the keyword THEN, a statement, the keyword ELSE, another statement, and finally the keyword ENDIF.
11. Conditions in IF-ELSE statements consist of expressions separated by relational operators.
12. Expressions can be arithmetic expressions consisting of terms separated by additive operators.
13. Terms are composed of factors separated by multiplicative operators.
14. Factors can be literals, identifiers, or expressions enclosed in parentheses.
15. Literals can be integer literals, real literals, string literals, boolean literals, or character literals.
16. Integer literals consist of one or more digits.
17. Real literals consist of one or more digits followed by a decimal point and another sequence of digits.
18. String literals are enclosed in double quotes and can contain any sequence of characters.
19. Boolean literals are TRUE or FALSE.
20 Character literals are enclosed in single quotes and represent a single character.
21. Additive operators include addition (+) and subtraction (-).
22. Multiplicative operators include multiplication (*) and division (/).

## RULES OF HAL/S BUT NOT IN THE GRAMMAR
1. Labels are used to mark specific points in the code for referencing and branching. They typically end with a colon.
2. Branching instructions allow the program to jump to a different part of the code based on certain conditions or unconditionally.
3. Looping constructs like DO-WHILE or REPEAT-UNTIL are commonly used in HAL/S for repetitive tasks.
4. HAL/S typically includes instructions for direct memory access, such as loading from or storing to specific memory locations.
5. Subroutine calls allow for modular programming by invoking a separate block of code. This can improve code organization and reusability.
6. Asynchronous events are used to respond to events in priority. HAL/S may include mechanisms for handling interrupts, allowing the program to respond to external events asynchronously.
-------------------------------------------------------
## The Grammar
Now that the rules are defined for the construction of the grammar, it is needed to make a tree. In order to make the tree clearer, some objects of the grammar will be defined better:

In this code the Natural Language ToolKit is used in order to detect the programming language. 

### Step One
The Context Free Grammar is defined with the function CFG.fromstring(). 
```py
rammar = CFG.fromstring("""
    S -> 'PROGRAM' ID 'BEGIN' DCL STL 'END' ';'
    ID -> 'ExampleHAL' | 'ExampleHAL2' | 'ALTITUDE' | 'VELOCITY' | 'UpdateVelocity' | 'DisplayVelocity' | 'SUBROUTINE' | 'Altitude' | 'below' | 'above' | 'is' | CHAR ID
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
```

## Step Two
Create a parser that can analyze the defined grammar.
```py
custom_parser = nltk.ChartParser(grammar)
```

## Step Three
Since the nature of the program is to be written on lines per order, to be tokenized, it needs to come together on a single line.
```py
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
```
## Step Four
Define the sentences on testing. On both of this tests, the resulting tree should be displayed.
```
sentences = [
    """
    PROGRAM ExampleHAL BEGIN
        DCL ALTITUDE REAL INIT ( 0.0 ) ; 
        DCL VELOCITY REAL INIT ( 0.0 ) ; 
        CALL UpdateVelocity ; 
        END ;
    """,
    """
    PROGRAM ExampleHAL2 BEGIN
        DCL ALTITUDE REAL INIT ( 0.0 ) ;
        DCL VELOCITY REAL INIT ( 0.0 ) ;
        CALL DisplayVelocity ;

        SUBROUTINE DisplayVelocity BEGIN
            PRINT ( VELOCITY ) ;
        END ;
    END ;

    """
```

## Step Five
Tokenize the sentences to see the generated trees if any. For this procedure the function costum_tokenize is used. Following up with the display of trees.
```
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
```

# Tests
For the ExampleHAL program this is the resulting tree
```
                                                                                             S                                                                                                

    _________________________________________________________________________________________|____________________________________________________________________________________            

   |      |    |   |      |                                                                       DCL                                                                             |           

   |      |    |   |      |                         _______________________________________________|_______________________                                                       |           

   |      |    |   |      |                        |                                                                      DCLP                                                    |           

   |      |    |   |      |                        |                                                                 ______|________________________________________              |           

   |      |    |   |      |                       DECL                                                             DECL                                             |             |           

   |      |    |   |      |        ________________|_________________________                       ________________|_________________________                      |             |           

   |      |    |   |      |       |   |    |   |   |      |      |          VAL                    |   |    |   |   |      |      |          VAL                    |             |           

   |      |    |   |      |       |   |    |   |   |      |      |           |                     |   |    |   |   |      |      |           |                     |             |           

   |      |    |   |      |       |   |    |   |   |      |      |          LIT                    |   |    |   |   |      |      |          LIT                    |             |           

   |      |    |   |      |       |   |    |   |   |      |      |           |                     |   |    |   |   |      |      |           |                     |             |           

   |      |    |   |      |       |   |    |   |   |      |      |        CHARLIT                  |   |    |   |   |      |      |        CHARLIT                  |             |           

   |      |    |   |      |       |   |    |   |   |      |      |     ______|_______              |   |    |   |   |      |      |     ______|_______              |             |           

   |      |    |   |      |       |   |    |   |   |      |      |    |           CHARLIT          |   |    |   |   |      |      |    |           CHARLIT          |            STL          

   |      |    |   |      |       |   |    |   |   |      |      |    |       _______|_______      |   |    |   |   |      |      |    |       _______|_______      |          ___|__________________
   |      |    |   |      |       |   |    |   |   |      |      |    |      |            CHARLIT  |   |    |   |   |      |      |    |      |            CHARLIT  |         ST              
       |
   |      |    |   |      |       |   |    |   |   |      |      |    |      |               |     |   |    |   |   |      |      |    |      |               |     |     ____|____________          |
   |      |    |   |      ID      |   |    |   |   |      ID    TYPE CHAR   CHAR            CHAR   |   |    |   |   |      ID    TYPE CHAR   CHAR            CHAR  DCLP  |    |            ID       STLP
   |      |    |   |      |       |   |    |   |   |      |      |    |      |               |     |   |    |   |   |      |      |    |      |               |     |    |    |            |         |
PROGRAM BEGIN END  ;  ExampleHAL DCL INIT  (   )   ;   ALTITUDE REAL  0      .               0    DCL INIT  (   )   ;   VELOCITY REAL  0      .               0    ...  CALL  ;      UpdateVelocity ...
```
For ExampleHAL2 program
```
                                                                                                                           S                                      

    _______________________________________________________________________________________________________________________|_____________________________________________________________________________________________________
   |      |    |   |      |                                                                       DCL                                                             
                                                               |
   |      |    |   |      |                         _______________________________________________|_______________________                                       
                                                               |
   |      |    |   |      |                        |                                                                      DCLP                                    
                                                               |
   |      |    |   |      |                        |                                                                 ______|________________________________________                                                             |
   |      |    |   |      |                       DECL                                                             DECL                                           
  |                                                           STL
   |      |    |   |      |        ________________|_________________________                       ________________|_________________________                    
  |          __________________________________________________|_______________
   |      |    |   |      |       |   |    |   |   |      |      |          VAL                    |   |    |   |   |      |      |          VAL                  
  |         |                                                                 STLP
   |      |    |   |      |       |   |    |   |   |      |      |           |                     |   |    |   |   |      |      |           |                   
  |         |                                                              ____|__________________________
   |      |    |   |      |       |   |    |   |   |      |      |          LIT                    |   |    |   |   |      |      |          LIT                  
  |         |                                                             ST                              |
   |      |    |   |      |       |   |    |   |   |      |      |           |                     |   |    |   |   |      |      |           |                   
  |         |                       ______________________________________|_____________                  |
   |      |    |   |      |       |   |    |   |   |      |      |        CHARLIT                  |   |    |   |   |      |      |        CHARLIT                
  |         |                      |        |    |   |         |                       STL                |
   |      |    |   |      |       |   |    |   |   |      |      |     ______|_______              |   |    |   |   |      |      |     ______|_______            
  |         |                      |        |    |   |         |                     ___|____________     |
   |      |    |   |      |       |   |    |   |   |      |      |    |           CHARLIT          |   |    |   |   |      |      |    |           CHARLIT          |         |                      |        |    |   |         |                    ST               |    |
   |      |    |   |      |       |   |    |   |   |      |      |    |       _______|_______      |   |    |   |   |      |      |    |       _______|_______      |         |                      |        |    |   |         |           _________|_________       |    |
   |      |    |   |      |       |   |    |   |   |      |      |    |      |            CHARLIT  |   |    |   |   |      |      |    |      |            CHARLIT  |         ST                     |        |    |   |         |          |    |    |   |    EXP     |    |
   |      |    |   |      |       |   |    |   |   |      |      |    |      |               |     |   |    |   |   |      |      |    |      |               |     |     ____|_________             |        |    |   |         |          |    |    |   |     |      |    |
   |      |    |   |      ID      |   |    |   |   |      ID    TYPE CHAR   CHAR            CHAR   |   |    |   |   |      ID    TYPE CHAR   CHAR            CHAR  DCLP  |    |         ID           |        |    |   |         ID         |    |    |   |     ID    STLP STLP
   |      |    |   |      |       |   |    |   |   |      |      |    |      |               |     |   |    |   |   |      |      |    |      |               |     |    |    |         |            |        |    |   |         |          |    |    |   |     |      |    |
PROGRAM BEGIN END  ;  ExampleHAL DCL INIT  (   )   ;   ALTITUDE REAL  0      .               0    DCL INIT  (   )   ;   VELOCITY REAL  0      .               0    ...  CALL  ;  DisplayVelocity SUBROUTINE BEGIN END  ;  DisplayVelocity PRINT  (    )   ;  VELOCITY ...  ...
```
## References:
Ryer, M. (September, 1978). PROGRAMMING IN HAL/S. Bitsavers. Retrieved 08 April. 2024, from https://bitsavers.org/pdf/intermetrics/programming_in_hal-s.pdf.

Carrero, D. (n.d.). Ejemplo Básico de Programa en HAL/S. Programaci. Programacion. Retrieved 08 April. 2024, from https://programacion.net/articulo/ejemplo-basico-de-programa-en-hal-s_3294.

Gatevidyalay. (n.d.). Left Recursion | Left Recursion Elimination. Elearn. Retrieved 28 April. 2024, from https://elearn.daffodilvarsity.edu.bd/pluginfile.php/1868451/mod_folder/content/0/Lecture - 6 Left Recursion.pdf.

Geeks for Geeks. (2021, June 11). Removal of ambiguity (Converting an Ambiguous grammar into Unambiguous grammar) - GeeksforGeeks. Geeksforgeeks. Retrieved 28 April. 2024, from https://geeksforgeeks.org/removal-of-ambiguity-converting-an-ambiguos-grammar-into-unambiguos-grammar/.
