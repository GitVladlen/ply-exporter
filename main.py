from my_parser import build_tree

if __name__=="__main__":
    data = '''
ID: A901 Name: Adveture name
Dialog: You see something in send
Option: Check it out
Option: Pass by
    '''
    
    result = build_tree(data)
    print (result)

