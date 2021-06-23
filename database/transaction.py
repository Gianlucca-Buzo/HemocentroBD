from database import cursor, db   

def insert_transaction (transaction_values):
    cursor.execute("INSERT INTO Transacao (ID_Pedido,DataTransacao) VALUES %s" % (transaction_values,))
    db.commit()
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
    for client in cursor:
        num_campos = len(client)
        for i in range (0,num_campos):
            print(client[i])
        # return client[0]  