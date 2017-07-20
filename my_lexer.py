import ply.lex as lex
from ply.lex import TOKEN
import re

tokens = ("ID", "NAME")

t_ID = r'ID: [C|A|L|N]\d{3}'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex(reflags=re.UNICODE | re.DOTALL | re.IGNORECASE)

if __name__=="__main__":
    data = '''
ID: A901 Name: Adveture name
Dialog: You see something in send
Option: Check it out
Option: Pass by
    '''

    lexer.input(data)

    for tok in iter(lexer.token, None):
        print (repr(tok.type), repr(tok.value))