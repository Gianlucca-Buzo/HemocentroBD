from database import cursor, db

def insert_hospital (hospital_values,address_values,number_values):
    cursor.execute("INSERT INTO Hospital (Nome, Email) VALUES %s" % (hospital_values,))
    db.commit()
    insert_address(hospital_values[0],address_values)
    insert_number(hospital_values[0],number_values)
    insert_cellphone(hospital_values[0],number_values)
    return True

def insert_address (nome_hospital,address_values):
    id_hospital = select_ID(nome_hospital)
    address_values.append(id_hospital)
    address_tuple = tuple(address_values)
    cursor.execute("INSERT INTO Endereco_Hospital (Rua,Numero,Complemento,ID_Hospital) VALUES %s" % (address_tuple,))
    db.commit()
    return True

def insert_cellphone (nome_hospital,number_values):
    if(number_values[0][0]!= ''):
        id_hospital = select_ID(nome_hospital)
        number_values[0].append(id_hospital)
        number_tuple = tuple(number_values[0])
        cursor.execute("INSERT INTO Telefones_Hospital (Numero,ID_Hospital) VALUES %s" % (number_tuple,))
        db.commit()
    return True

def insert_number (nome_hospital,number_values):
    if(number_values[1][0]!= ''):
        id_hospital = select_ID(nome_hospital)
        number_values[1].append(id_hospital)
        number_tuple = tuple(number_values[1])
        cursor.execute("INSERT INTO Telefones_Hospital (Numero,ID_Hospital) VALUES %s" % (number_tuple,))
        db.commit()
    return True

############################################ PESQUISAS ################################################

def select_ID (nome):
    cursor.execute(f"SELECT ID_Hospital FROM Hospital WHERE Nome = '{nome}'")
    for client in cursor:
        return client[0]

def create_dictionary (hospital_values):
    dictionary = {'Nome': hospital_values[0],
                  'Email': hospital_values[1]
                }
    return create_string(dictionary)

def create_string (dictionary):
    string = ''
    if (dictionary['Nome'] != ''):
        string += f"Nome = '{dictionary['Nome']}'"
    if (dictionary['Email'] != ''):
        if (string != ''):
            string += f" AND Email = '{dictionary['Email']}'"
        else:
            string += f"Email = '{dictionary['Email']}'"
    return string

def create_dictionary_fields (hospital_values):
    dictionary = {'Nome': hospital_values[0],
                  'Email': hospital_values[1],
                  'NumerosTelefone': hospital_values[2],
                  'Rua': hospital_values[3],
                  'Numero': hospital_values[4],
                  'Complemento': hospital_values[5]
                }
    return create_string_fields(dictionary)

def create_string_fields (dictionary):
    string = ''
    if (dictionary['Nome'] == True):
        string += f"h.Nome"
    if (dictionary['Email'] == True):
        if (string != ''):
            string += f",h.Email"
        else:
            string += f"h.Email"
    if (dictionary['NumerosTelefone'] == True):
        if (string != ''):
            string += f",GROUP_CONCAT(t.Numero) as NumerosTelefone"
        else:
            string += f"GROUP_CONCAT(t.Numero) as NumeroTelefone"
    if (dictionary['Rua'] == True):
        if (string != ''):
            string += f",e.Rua"
        else:
            string += f"e.Rua"
    if (dictionary['Numero'] == True):
        if (string != ''):
            string += f",e.Numero"
        else:
            string += f"e.Numero"
    if (dictionary['Complemento'] == True):
        if (string != ''):
            string += f",e.Complemento"
        else:
            string += f"e.Complemento"
    return string

def select_hospital (fields,values):
    cursor.execute(f"SELECT {fields} FROM HOSPITAL as H LEFT OUTER JOIN Telefones_Hospital AS t ON t.ID_Hospital = h.ID_Hospital LEFT OUTER JOIN Endereco_Hospital AS e ON e.ID_Hospital = h.ID_Hospital WHERE {values} GROUP BY h.ID_Hospital")
    field_names = [i[0] for i in cursor.description]
    results = []
    for client in cursor:
        results.append(client)
    return (results,field_names)