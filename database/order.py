from database import cursor, db, hospital
from datetime import datetime
from typing import Tuple

def create_tuple (nome_hospital,order_list):
    id_hospital = hospital.select_ID(nome_hospital)
    data_pedido = datetime.today
    str_data = data_pedido.strftime("%Y-%m-%d")
    order_list.append(str_data)
    order_list.append(id_hospital)
    return tuple(order_list)

def insert_order (order_values):
    cursor.execute("INSERT INTO Pedido (Quantidade,TipoSanguineo,DataPedido,ID_Hospital) VALUES %s" % (order_values,))
    db.commit()
    return True

############################################ PESQUISAS ################################################
def create_dictionary (order_values):
    if(order_values[0] != ''):
        id_hospital = hospital.select_ID(order_values[0])
    else:
        id_hospital = ''
    dictionary = {'ID_Hospital': id_hospital,
                  'Quantidade': order_values[1],
                  'TipoSanguineo': order_values[2],
                  'DataPedido': order_values[3]
                }
    return create_string(dictionary)

def create_string (dictionary):
    string = ''
    if (dictionary['ID_Hospital'] != ''):
        string += f"ID_Hospital = '{dictionary['ID_Hospital']}'"
    if (dictionary['Quantidade'] != ''):
        if (string != ''):
            string += f" AND Quantidade = '{dictionary['Quantidade']}'"
        else:
            string += f"Quantidade = '{dictionary['Quantidade']}'"
    if (dictionary['TipoSanguineo'] != ''):
        if (string != ''):
            string += f" AND TipoSanguineo = '{dictionary['TipoSanguineo']}'"
        else:
            string += f"TipoSanguineo = '{dictionary['TipoSanguineo']}'"
    if (dictionary['DataPedido'] != ''):
        if (string != ''):
            string += f" AND DataPedido = '{dictionary['DataPedido']}'"
        else:
            string += f"DataPedido = '{dictionary['DataPedido']}'"
    return string

def create_dictionary_fields (order_values):
    dictionary = {'NomeHospital': order_values[0],
                  'Quantidade': order_values[1],
                  'TipoSanguineo': order_values[2],
                  'DataPedido': order_values[3]
                }
    return create_string_fields(dictionary)

def create_string_fields (dictionary):
    string = ''
    if (dictionary['NomeHospital'] == True):
        string += f"h.Nome"
    if (dictionary['Quantidade'] == True):
        if (string != ''):
            string += f",p.Quantidade"
        else:
            string += f"p.Quantidade"
    if (dictionary['TipoSanguineo'] == True):
        if (string != ''):
            string += f",p.TipoSanguineo"
        else:
            string += f"p.TipoSanguineo"
    if (dictionary['DataPedido'] == True):
        if (string != ''):
            string += f",p.DataPedido"
        else:
            string += f"p.DataPedido"
    return string

def select_order (fields,values):
    cursor.execute(f"SELECT {fields} FROM Pedido AS p INNER JOIN Hospital AS h ON h.ID_Hospital=p.ID_Hospital WHERE {values}")
    field_names = [i[0] for i in cursor.description]
    results = []
    for client in cursor:
        results.append(client)
    return (results,field_names)

def select():
    cursor.execute(f"SELECT * FROM Pedido")
    field_names = [i[0] for i in cursor.description]
    results = []
    for client in cursor:
        results.append(client)
    return (results,field_names)

def select_for_transaction (id_pedido):
    cursor.execute(f"SELECT TipoSanguineo,Quantidade FROM Pedido WHERE ID_Pedido = {id_pedido}")
    results = []
    for row in cursor:
        results.append(row)
    return (results)

