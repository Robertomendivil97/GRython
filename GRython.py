import ply.lex as lex
import ply.yacc as yacc

from GRython_Lexer import tokens

import sys

count = 0

print("    RYTHON       ")
print("PLY Sintax and Lexer Analyzer")
print(" \n\n")
# -----------------------------------~ YACC ~-----------------------------------

precedence = (
    ('right', 'ASSIGN'),
    ('left', 'NE'),
    ('left', 'LT', 'GT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'PARL'),
    ('left', 'PARR')
)


# -----------------------------------< GENERAL PROGRAM >-----------------------------------
def p_package(p):
    ''' program : PACKAGE COLON V MAINP P B END'''


def p_MAINP(p):
    ''' MAINP : empty'''
    #global program_counter
    #program_instructions.append("Goto ")
    #program_counter += 1

# -----------------------------------< VARIABLES >-----------------------------------
symbols = []


def p_V(p):
    ''' V : V VAR VM AS TIPO
    | empty'''

#V1 - Mas de una variable
#V2 - Variables seáradas por coma

def p_VM(p):
    ''' VM : ID VM2'''
    symbols.append(p[1])    
    global count

    count += 1

    #symbols[p[1]] = ["NULL", "TYPE"]

def p_VM2(p):
    ''' VM2 : COMMA ID VM2'''
    symbols.append(p[2])
    global count
    count += 1
    
    #symbols[p[2]] = ["NULL", "TYPE"]



def p_VM_array(p):
    ''' VM : ID SQBL NUMBER SQBR VM2'''
    #symbols[p[1]] = ["NULL", "TYPE", p[3]]

def p_VM2_array(p):
    ''' VM2 : COMMA ID SQBL NUMBER SQBR VM2'''
    #symbols[p[2]] = ["NULL", "TYPE", p[4]]


def p_VM_matrix(p):
    ''' VM : ID SQBL NUMBER SQBR SQBL NUMBER SQBR VM2'''
    #symbols[p[1]] = ["NULL", "TYPE", [p[3], p[5]]]

def p_VM2_matrix(p):
    ''' VM2 : COMMA ID SQBL NUMBER SQBR SQBL NUMBER SQBR VM2'''
    #symbols[p[2]] = ["NULL", "TYPE", [p[4], p[6]]]


def p_VM_cube(p):
    ''' VM : ID SQBL  NUMBER SQBR SQBL NUMBER SQBR SQBR SQBL NUMBER SQBR VM2'''
    #symbols[p[1]] = ["NULL", "TYPE", [p[3], p[5], p[7]]]


def p_VM2_cube(p):
    ''' VM2 : COMMA ID SQBL  NUMBER SQBR SQBL NUMBER SQBR SQBR SQBL NUMBER SQBR VM2'''
    #symbols[p[2]] = ["NULL", "TYPE", [p[4], p[6], p[8]]]


def p_VM2_empty(p):
    '''VM2 : empty'''


# +++++++++++++++ / VARIABLE TYPE \ +++++++++++++++
sym_type = []

def p_TIPO(p):
    ''' TIPO : FLOAT
    | INT
    | ARRAY_INT
    | ARRAY_FLOAT
    | MATRIX_INT
    | MATRIX_FLOAT
    | CUBE_INT
    | CUBE_FLOAT
    | BOOL'''
    
    #TABLA DE SIMBOLOS 
    
    global count
    for i in range(count):
        sym_type.append(p[1])
    
    count = 0



# -----------------------------------< END OF VARIABLES >-----------------------------------

# -----------------------------------< PROCEDURES >-----------------------------------



def p_P(p):
    ''' P : P  AUXPOSP MODULE ID COLON ST ENDM'''
    symbols.append(p[3+1])
    sym_type.append("MODULE")



def p_P_empty(p):
    ''' P : empty'''


def p_AUXPOSP(p):
    ''' AUXPOSP : empty'''
    


# -----------------------------------< END OF PROCEDURES >-----------------------------------

# ------------------------------< MAIN PROGRAM or INTERMADIATE CODE >------------------------------
def p_B(p):
    ''' B : MAIN PARL PARR ST '''


def p_ST(p):
    ''' ST : S ST
    | empty'''


# ---------------------------< END OF MAIN PROGRAM or INTERMADIATE CODE >---------------------------

# STATEMENTS
def p_S(p):
	''' S : ROUT PARL SID PARR
	| RIN PARL IID PARR
	| IF CONDITION COLON ST ENDIF
	| IF CONDITION COLON ST ELSE COLON ST ENDIF
	| FOR ID IN ID COLON ST ENDFOR
	| VMC ASSIGN UPDATE
	| WHILE CONDITION COLON ST ENDW
	| DO COLON ST DWHILE COLON CONDITION ENDDO
	| RGOSUB ID
	'''

# print management
def p_SID(p):
	'''SID : STRING SID2
	| VMC SID2'''
def p_SID2(p):
	'''SID2 : PLUS VMC SID2
	| PLUS STRING SID2
	| empty'''

# input management
def p_IID(p):
	'''IID : VMC IID2'''
def p_IID2(p):
	'''IID2 : COMMA VMC  IID2
	| empty'''


# if management
def p_CONDITION(p):
	'''CONDITION : CMP COMPARATOR CMP'''
def p_CMP(p):
	'''CMP : NUMBER
	| ID'''
def p_COMPARATOR(p):
	'''COMPARATOR : NE
	| GT
	| LT
	| EQ'''


# ASSIGN management
def p_VMC(p):
	'''VMC : ID
	| ID SQBL CMP SQBR SQBL CMP SQBR
	| ID SQBL CMP SQBR SQBL CMP SQBR SQBL CMP SQBR'''
# Definicion de cuadruplos
def p_UPDATE(p):
	'''UPDATE : VMC UPDATE
	| NUMBER OPERATOR UPDATE
	| VMC
	| NUMBER'''
def p_OPERATOR(p):
	'''OPERATOR : PLUS
	| MINUS
	| TIMES
	| DIVIDE'''

# EMPTY VALUES
def p_empty(p):
	''' empty :	'''
	pass

# THROWING ERROR
def p_error(p):
	print("\tSyntax error in line " + str(p.lineno))



parser = yacc.yacc()

f = open("codes/test_SumaMatriz.txt", "r")
parser.parse(f.read())

#Print symbol table

print("TABLA DE SIMBOLOS")
for i in range(len(symbols)):
	print(str(sym_type[i]) + "\t\t" + str(symbols[i]))