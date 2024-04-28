# Context-Free-Grammar
Evidencia 2 para TC2037 Implementation of Computational Methods

## Description
The language that I will be using for the context-free-grammar is HAL/S.

HAL/S is a programming is a programming language for real time aerospace programming. It was produce for NASA Space Shuttle Flight Software. 

HAL/S was created with the intention of having reliability, efficiency and machine independence, this means less programming training, and reuse of blocks of code for other perojects, without the access of the aerrospace hardware. (Ryer, 1978) 

### RULES THAT'LL BE USED ON THE GRAMMAR
1. Every program begins with the label PROGRAM + [NAME OF PROGRAM]
2. Comments are initiated by '--' at the beginning
3. All statements end with a semi-colon
4. Keyword are created by beginning a label DECLARE. Keywords are always declared before they are used. They are never 2 characters or less.
5. Variables or Identifiers can be written within 1 and 30 characters in length and can use A-Z, 9-0, and underscores (_).
6. After the label DECLARE, they come the executable statements.
7. These executable statements are WRITE, READ. After the statment, it is followed by a parenthesis with a conexion number (N)
8. At the end, there are delimiting statements, like CLOSE
   
10. It also contains, Operators which are logical statements '-, +, /, **, ,'
11. Two operators can never be together. If they are, they need to be parethesized ().
12. And literals, which are numbers. This numbers can be represented as integer ans scalar types and does not distignuish them.
13. These literals, are not limited to '0-9' the syntaxis can have logical characters like '-, +, /, **, , .' 
14. CLOSE must be the last line on every program.

## RULES OF HAL/S BUT NOT IN THE GRAMMAR
1. _Declare Statements_ : When a variable is a compound varibles, intergrated by other variables, they can be declared as a variable with the following syntax: DECLARE + [VARIABLE_NAME] + : +  PROGRAM + atributes of the declare statement. These statements count as programs themselves, and have this same sintax.
2. _Function Statements_ : When a function variable is declared, it can be used with the standard functions syntaxis. They can be declared as a function with the following syntax: [FUNCTION_NAME] + : +  FUNCTION ([variable1, variable2,...]; + declare of variables and conditions.
-------------------------------------------------------
## The Grammar
Now that the rules are defined for the construction of the grammar, it is needed to make a tree. In order to make the tree clearer, some objects of the grammar will be defined better:

## PROGRAM

## COMMENTS

## STATEMENT
   ## VARIABLES
   ## LOGICAL STATEMENTS
   ## EXECUTABLE STATEMENTS
## LITERALS

```
print('Hello World')
```
## References:
Ryer, M. (September, 1978). PROGRAMMING IN HAL/S. Bitsavers. Retrieved 08 April. 2024, from https://bitsavers.org/pdf/intermetrics/programming_in_hal-s.pdf.

Carrero, D. (n.d.). Ejemplo Básico de Programa en HAL/S. Programaci. Programacion. Retrieved 08 April. 2024, from https://programacion.net/articulo/ejemplo-basico-de-programa-en-hal-s_3294.

Gatevidyalay. (n.d.). Left Recursion | Left Recursion Elimination. Elearn. Retrieved 28 April. 2024, from https://elearn.daffodilvarsity.edu.bd/pluginfile.php/1868451/mod_folder/content/0/Lecture - 6 Left Recursion.pdf.

Geeks for Geeks. (2021, June 11). Removal of ambiguity (Converting an Ambiguous grammar into Unambiguous grammar) - GeeksforGeeks. Geeksforgeeks. Retrieved 28 April. 2024, from https://geeksforgeeks.org/removal-of-ambiguity-converting-an-ambiguos-grammar-into-unambiguos-grammar/.
