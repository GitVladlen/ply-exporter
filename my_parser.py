from my_lexer import tokens
import ply.yacc as yacc

def p_root(p):
    'root : TAG value'
    p[0] = p[1]

def p_value(p):
    '''value : TEXT'''
    if len(p) > 2:
        p[0] = p[1]+p[2]
    else:
        p[0] = p[1]


def p_error(p):
    print ('Unexpected token:', p)

parser = yacc.yacc()

def build_tree(code):
    return parser.parse(code)

if __name__=="__main__":
    data = '''
ID: A901 Name: Adveture name
Dialog: You see something in send
Option: Check it out
Option: Pass by
    '''

    result = build_tree(data)
    print (result)