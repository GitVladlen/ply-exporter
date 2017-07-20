from my_lexer import tokens
import ply.yacc as yacc

def p_str(p):
    '''str : NUMBER'''
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