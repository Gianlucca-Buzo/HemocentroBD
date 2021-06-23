from database import cursor, db

def select():
    cursor.execute(f"SELECT * FROM Estoque")
    for client in cursor:
        num_campos = len(client)
        for i in range (0,num_campos):
            print(client[i])

def update(tipoSanguineo,quantidade):
    nova_quantidade = select_quantidade(tipoSanguineo) + (quantidade)
    cursor.execute(f"UPDATE Estoque SET Quantidade = {nova_quantidade} WHERE TipoSanguineo = '{tipoSanguineo}'")
    db.commit()
    return True

def select_quantidade(tipoSanguineo):
    cursor.execute(f"SELECT Quantidade FROM Estoque WHERE TipoSanguineo = '{tipoSanguineo}'")
    for client in cursor:
        num_campos = len(client)
        for i in range (0,num_campos):
            return(client[i])