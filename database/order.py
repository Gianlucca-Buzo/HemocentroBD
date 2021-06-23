from database import cursor, db

def insert_order (order_values):
    cursor.execute("INSERT INTO Pedido (ID_Hospital,TipoSanguineo,DataPedido,Quantidade) VALUES %s" % (order_values,))
    db.commit()
    return True

