import ply.lex as lex
from ply.lex import TOKEN
import re

tokens = (
    "TAG",

    "TAG_ID",
    "TAG_NAME",
    "TAG_DIALOG",
    "TAG_OPTION",

    "TEXT",
)

reserved = {
    'id' : 'TAG_ID',
    'name' : 'TAG_NAME',
    'dialog' : 'TAG_DIALOG',
    'option' : 'TAG_OPTION',
}


def t_TAG(t):
    r'\w+:'
    t.type = reserved.get(t.value.lower(), 'TAG')
    return t

t_TEXT = r'[^:]+'

# def t_TAG(t):
#     r'\w+:(\s*\w+\s*)*\w+:'

#     i1 = t.value.index(':')
#     n = t.value[::-1].index(' ')
#     i2 = len(t.value) - n

#     print (" >>> value = '{}' i1 = {} i2 = {} n = {}".format(
#         t.value, i1, i2, n))

#     tag_name = t.value[:i1]
#     t.type = reserved.get(tag_name.lower(), 'TAG')

#     t.lexer.lexpos -= n

#     t.value = t.value[i1 + 1: i2]

#     return t

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
Option: Pass by '''

    lexer.input(data)

    for tok in iter(lexer.token, None):
        print (repr(tok.type), repr(tok.value))


# import sys
# sys.path.insert(0, "../..")


# tokens = (
#     'H_EDIT_DESCRIPTOR',
# )

# # Tokens
# t_ignore = " \t\n"


# def t_H_EDIT_DESCRIPTOR(t):
#     r"\d+H.*"                     # This grabs all of the remaining text
#     i = t.value.index('H')
#     n = eval(t.value[:i])

#     # Adjust the tokenizing position
#     t.lexer.lexpos -= len(t.value) - (i + 1 + n)

#     t.value = t.value[i + 1:i + 1 + n]
#     return t


# def t_error(t):
#     print("Illegal character '%s'" % t.value[0])
#     t.lexer.skip(1)

# # Build the lexer
# import ply.lex as lex
# lex.lex()
# lex.runmain()