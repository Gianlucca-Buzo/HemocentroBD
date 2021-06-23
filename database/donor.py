from database import cursor, db

def exists_donor (cpf):
    cursor.execute("SELECT Nome FROM Doador WHERE CPF = '%s' " % (cpf,))
    return verify_cursor(cursor)

def insert_donor (donor_values,address_values,number_values):
    if not exists_donor(donor_values[0]):
        cursor.execute("INSERT INTO Doador VALUES %s" % (donor_values,))
        db.commit()
        insert_address(address_values)
        insert_number(number_values)
        insert_cellphone(number_values)
        return True
    else:
        return False

def insert_address (address_values):
    cursor.execute("INSERT INTO Endereco_Doador VALUES %s" % (address_values,))
    db.commit()
    return True

def insert_cellphone (number_values):
    if(number_values[0][1]!= ''):
        cursor.execute("INSERT INTO Telefones_Doador VALUES %s" % (number_values[0],))
        db.commit()
    return True

def insert_number (number_values):
    if(number_values[1][1]!= ''):
        cursor.execute("INSERT INTO Telefones_Doador VALUES %s" % (number_values[1],))
        db.commit()
    return True

def verify_cursor(cursor):
    for x in cursor:
        return True
    return False

############################################ PESQUISAS ################################################
def create_dictionary (donor_values):
    dictionary = {'CPF': donor_values[0],
                  'Nome': donor_values[1],
                  'Email': donor_values[2],
                  'Sexo': donor_values[3],
                  'DataNascimento': donor_values[4],
                  'TipoSanguineo': donor_values[5]
                }
    return create_string(dictionary)

def create_string (dictionary):
    string = ''
    if (dictionary['CPF'] != ''):
        string += f"CPF = '{dictionary['CPF']}'"
    if (dictionary['Nome'] != ''):
        if (string != ''):
            string += f" AND Nome = '{dictionary['Nome']}'"
        else:
            string += f"Nome = '{dictionary['Nome']}'"
    if (dictionary['Email'] != ''):
        if (string != ''):
            string += f" AND Email = '{dictionary['Email']}'"
        else:
            string += f"Email = '{dictionary['Email']}'"
    if (dictionary['Sexo'] != ''):
        if (string != ''):
            string += f" AND Sexo = '{dictionary['Sexo']}'"
        else:
            string += f"Sexo = '{dictionary['Sexo']}'"
    if (dictionary['DataNascimento'] != ''):
        if (string != ''):
            string += f" AND DataNascimento = '{dictionary['DataNascimento']}'"
        else:
            string += f"DataNascimento = '{dictionary['DataNascimento']}'"
    if (dictionary['TipoSanguineo'] != ''):
        if (string != ''):
            string += f" AND TipoSanguineo = '{dictionary['TipoSanguineo']}'"
        else:
            string += f"TipoSanguineo = '{dictionary['TipoSanguineo']}'"
    return string

def create_dictionary_fields (donor_values):
    dictionary = {'CPF': donor_values[0],
                  'Nome': donor_values[1],
                  'Email': donor_values[2],
                  'Sexo': donor_values[3],
                  'DataNascimento': donor_values[4],
                  'TipoSanguineo': donor_values[5],
                  'NumerosTelefone': donor_values[6],
                  'Rua': donor_values[7],
                  'Numero': donor_values[8],
                  'Complemento': donor_values[9]
                }
    return create_string_fields(dictionary)

def create_string_fields (dictionary):
    string = ''
    if (dictionary['CPF'] == True):
        string += f"d.CPF"
    if (dictionary['Nome'] == True):
        if (string != ''):
            string += f",d.Nome"
        else:
            string += f"d.Nome"
    if (dictionary['Email'] == True):
        if (string != ''):
            string += f",d.Email"
        else:
            string += f"d.Email"
    if (dictionary['Sexo'] == True):
        if (string != ''):
            string += f",d.Sexo"
        else:
            string += f"d.Sexo"
    if (dictionary['DataNascimento'] == True):
        if (string != ''):
            string += f",d.DataNascimento"
        else:
            string += f"d.DataNascimento"
    if (dictionary['TipoSanguineo'] == True):
        if (string != ''):
            string += f",d.TipoSanguineo"
        else:
            string += f"d.TipoSanguineo"
    if (dictionary['NumerosTelefone'] == True):
        if (string != ''):
            string += f",GROUP_CONCAT(t.Numero) as NumerosTelefone"
        else:
            string += f"GROUP_CONCAT(t.Numero) as NumerosTelefone"
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

def select_donor (fields,values):
    cursor.execute(f"SELECT {fields} FROM Doador as d LEFT OUTER JOIN Telefones_Doador AS t ON t.CPF_Doador = d.CPF LEFT OUTER JOIN Endereco_Doador AS e ON e.CPF_Doador = d.CPF WHERE {values} GROUP BY d.CPF")
    results = []
    field_names = [i[0] for i in cursor.description]
    for row in cursor:
        results.append(row)
    return (results,field_names)

def select_tipoSanguineo (CPF):
    cursor.execute(f"SELECT TipoSanguineo FROM Doador WHERE CPF = '{CPF}'")
    results = []
    for row in cursor:
        results.append(row)
    return (results)