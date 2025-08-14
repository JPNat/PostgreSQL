def readBD(cur, name):

    if name == None:
        return False
    
    try: 
        cur.execute(f'SELECT * FROM usuario WHERE nome = \'{nome}\'')
    except:
        return False
