from database import cursor, db

def select():
    cursor.execute(f"SELECT * FROM Estoque")
    field_names = [i[0] for i in cursor.description]
    results = []
    for client in cursor:
        results.append(client)
    return (results,field_names)

def update(tipoSanguineo,quantidade):
    nova_quantidade = select_quantidade(tipoSanguineo) + (quantidade)
    cursor.execute(f"UPDATE Estoque SET Quantidade = {nova_quantidade} WHERE TipoSanguineo = '{tipoSanguineo}'")
    db.commit()
    return True

def select_quantidade(tipoSanguineo):
    cursor.execute(f"SELECT Quantidade FROM Estoque WHERE TipoSanguineo = '{tipoSanguineo}'")
    for row in cursor:
        return row[0]
