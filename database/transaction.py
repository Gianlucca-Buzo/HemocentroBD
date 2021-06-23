from database import cursor, db, order, stock

def insert_transaction (transaction_values):
    cursor.execute("INSERT INTO Transacao (ID_Pedido,DataTransacao) VALUES %s" % (transaction_values,))
    db.commit()
    update_stock(transaction_values)
    return True

def update_stock(transaction_values):
    results = order.select_for_transaction(transaction_values[0])
    stock.update(results[0],-(results[1]))
    return True

############################################ PESQUISAS ################################################
def create_dictionary (transaction_values):
    dictionary = {'ID_Pedido': transaction_values[0],
                  'DataTransacao': transaction_values[1]
                }
    return create_string(dictionary)

def create_string (dictionary):
    string = ''
    if (dictionary['ID_Pedido'] != ''):
        string += f"ID_Pedido = '{dictionary['ID_Pedido']}'"
    if (dictionary['DataTransacao'] != ''):
        if (string != ''):
            string += f" AND DataTransacao = '{dictionary['DataTransacao']}'"
        else:
            string += f"DataTransacao = '{dictionary['DataTransacao']}'"
    return string

def create_dictionary_fields (transaction_values):
    dictionary = {'ID_Pedido': transaction_values[0],
                  'DataTransacao': transaction_values[1]
                }
    return create_string_fields(dictionary)

def create_string_fields (dictionary):
    string = ''
    if (dictionary['ID_Pedido'] == True):
        string += f"ID_Pedido"
    if (dictionary['DataTransacao'] == True):
        if (string != ''):
            string += f",DataTransacao"
        else:
            string += f"DataTransacao"
    return string

def select_order (fields,values):
    cursor.execute(f"SELECT {fields} FROM Transacao WHERE {values}")
    field_names = [i[0] for i in cursor.description]
    results = []
    for client in cursor:
        results.append(client)
    return (results,field_names)