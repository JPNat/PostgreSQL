def writeBD(cur, conn, rollback, email, nome, telefone, credito, senha, cargo_administrador):
    try:
        insert_usuario = 'INSERT INTO usuario (email, nome, telefone, credito, senha, cargo_administrador) VALUES (%s, %s, %s, %f, %s, %s)'

        insert_value = (email, nome, telefone, credito, senha, cargo_administrador)
        
        for record in insert_value:
            cur.execute(insert_usuario, record)

        cur.execute('SELECT * FROM usuario')
        for record in cur.fetchall():
            print(record)

        conn.commit()

        print('\n Criado com sucesso!')

        return True
    except:
        print('error')
        
        return False