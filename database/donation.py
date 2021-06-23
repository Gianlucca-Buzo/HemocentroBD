from database import cursor, db

def insert_donation (donation_values):
    cursor.execute("INSERT INTO Doacao (ID_Doador,ID_Enfermeiro,DataDoacao,Quantidade) VALUES %s" % (donation_values,))
    db.commit()
    return True

############################################ PESQUISAS ################################################
def create_dictionary (donation_values):
    dictionary = {'ID_Doador': donation_values[0],
                  'ID_Enfermeiro': donation_values[1],
                  'DataDoacao': donation_values[2],
                  'Quantidade': donation_values[3]
                }
    return create_string(dictionary)

def create_string (dictionary):
    string = ''
    if (dictionary['ID_Doador'] != ''):
        string += f"ID_Doador = '{dictionary['ID_Doador']}'"
    if (dictionary['ID_Enfermeiro'] != ''):
        if (string != ''):
            string += f" AND ID_Enfermeiro = '{dictionary['ID_Enfermeiro']}'"
        else:
            string += f"ID_Enfermeiro = '{dictionary['ID_Enfermeiro']}'"
    if (dictionary['DataDoacao'] != ''):
        if (string != ''):
            string += f" AND DataDoacao = '{dictionary['DataDoacao']}'"
        else:
            string += f"DataDoacao = '{dictionary['DataDoacao']}'"
    if (dictionary['Quantidade'] != ''):
        if (string != ''):
            string += f" AND Quantidade = '{dictionary['Quantidade']}'"
        else:
            string += f"Quantidade = '{dictionary['Quantidade']}'"
    return string

def create_dictionary_fields (donation_values):
    dictionary = {'ID_Doador': donation_values[0],
                  'ID_Enfermeiro': donation_values[1],
                  'DataDoacao': donation_values[2],
                  'Quantidade': donation_values[3]
                }
    return create_string_fields(dictionary)

def create_string_fields (dictionary):
    string = ''
    if (dictionary['ID_Doador'] == True):
        string += f"ID_Doador"
    if (dictionary['ID_Enfermeiro'] == True):
        if (string != ''):
            string += f",ID_Enfermeiro"
        else:
            string += f"ID_Enfermeiro"
    if (dictionary['DataDoacao'] == True):
        if (string != ''):
            string += f",DataDoacao"
        else:
            string += f"DataDoacao"
    if (dictionary['Quantidade'] == True):
        if (string != ''):
            string += f",Quantidade"
        else:
            string += f"Quantidade"
    return string

def select_donor (fields,values):
    cursor.execute(f"SELECT {fields} FROM Doacao WHERE {values}")
    for client in cursor:
        num_campos = len(client)
        for i in range (0,num_campos):
            print(client[i])
        # return client[0]