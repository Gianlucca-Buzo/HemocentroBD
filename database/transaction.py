from database import cursor, db   

def insert_transaction (transaction_values):
    cursor.execute("INSERT INTO Transacao (ID_Pedido,DataTransacao) VALUES %s" % (transaction_values,))
    db.commit()
    return True