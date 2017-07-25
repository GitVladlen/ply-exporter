import ply.lex as lex
from ply.lex import TOKEN
import re

tokens = (
    "TAG",
    "ID",
    "NAME",
    "TEXT",
)

reserved = {
    'id' : 'ID',
    'name' : 'NAME'
}

def t_TAG(t):
    r'\w+:'
    t.type = reserved.get(t.value, 'ID')
    return t

t_TEXT = r'\w+'

t_ignore = " \n"

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