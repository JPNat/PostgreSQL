def readBD(cur, name):
    if not name:
        return False
        
    try:
        cur.execute("SELECT * FROM usuario WHERE nome = %s", (name,))
        return cur.fetchall() 
    except Exception as e:
        print(f"Erro ao consultar banco: {e}")
        return False
