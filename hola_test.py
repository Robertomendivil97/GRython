import ply.lex as lex
import ply.yacc as yacc

import sys


tokens = ['HOLA','COMA','QUE','TAL']

t_ignore = r' '

t_HOLA = r'hola'
t_COMA = r'\,'
t_QUE = r'que'
t_TAL = r'tal'


def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)

lexer = lex.lex()


def p_S(p):
    '''
    S : X QUE TAL
    '''
    print("\tCORRECTO")
    
def p_X(p):
    '''
    X : HOLA Y
    '''
def p_Y(p):
    '''
    Y : COMA HOLA Y  
    | 
    '''
def p_error(p):
    print("\tINCORRECTO")
    

parser = yacc.yacc()


while True:
        try:
            s = input('')
        except EOFError:
            break
        parser.parse(s)