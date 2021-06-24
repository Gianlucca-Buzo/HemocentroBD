from database import cursor, db, stock, donor

def insert_donation (donation_values):
    cursor.execute("INSERT INTO Doacao (ID_Doador,ID_Enfermeiro,DataDoacao,Quantidade) VALUES %s" % (donation_values,))
    db.commit()
    update_stock(donation_values)
    return True

def update_stock (donation_values):
    tipoSanguineo = donor.select_tipoSanguineo (donation_values[0])
    stock.update(tipoSanguineo,float(donation_values[3]))
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

def select_donation (fields,values):
    cursor.execute(f"SELECT {fields} FROM Doacao WHERE {values}")
    field_names = [i[0] for i in cursor.description]
    results = []
    for client in cursor:
        results.append(client)
    return (results,field_names)

def select():
    cursor.execute(f"SELECT * FROM Doacao")
    results = []
    field_names = [i[0] for i in cursor.description]
    for row in cursor:
        results.append(row)
    return (results,field_names)