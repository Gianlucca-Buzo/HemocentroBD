from database import cursor, db

def exists_employee (cpf):
    cursor.execute("SELECT Nome FROM Funcionario WHERE CPF = '%s' " % (cpf,))
    return verify_cursor(cursor)

#Insere funcionario comum
def insert_employee (employee_values,address_values,number_values):
    if not exists_employee(employee_values[0]):
        cursor.execute("INSERT INTO Funcionario VALUES %s" % (employee_values,))
        db.commit()
        insert_address(address_values)
        insert_number(number_values)
        insert_cellphone(number_values)
        return True
    else:
        return False

#Insere enfermeiro
def insert_nurse (employee_values,nurse_values,address_values,number_values):
    if not exists_employee(nurse_values[0]):
        cursor.execute("INSERT INTO Funcionario (CPF,Nome,Email,Sexo,DataNascimento,Salario) VALUES %s" % (employee_values,))
        cursor.execute("INSERT INTO Enfermeiro VALUES %s" % (nurse_values,))
        db.commit()
        insert_address(address_values)
        insert_number(number_values)
        insert_cellphone(number_values)
        return True
    else:
        return False

#Insere administrador
def insert_manager (employee_values,manager_values,address_values,number_values):
    if not exists_employee(manager_values[0]):
        cursor.execute("INSERT INTO Funcionario (CPF,Nome,Email,Sexo,DataNascimento,Salario) VALUES %s" % (employee_values,))
        cursor.execute("INSERT INTO Administrador VALUES %s" % (manager_values,))
        db.commit()
        insert_address(address_values)
        insert_number(number_values)
        insert_cellphone(number_values)
        return True
    else:
        return False

def insert_address (address_values):
    cursor.execute("INSERT INTO Endereco_Funcionario VALUES %s" % (address_values,))
    db.commit()
    return True

def insert_cellphone (number_values):
    if(number_values[0][1]!= ''):
        cursor.execute("INSERT INTO Telefones_Funcionario VALUES %s" % (number_values[0],))
        db.commit()
    return True

def insert_number (number_values):
    if(number_values[1][1]!= ''):
        cursor.execute("INSERT INTO Telefones_Funcionario VALUES %s" % (number_values[1],))
        db.commit()
    return True


def verify_cursor(cursor):
    for x in cursor:
        return True
    return False

############################################ PESQUISAS ################################################
def create_dictionary (employee_values):
    dictionary = {'CPF': employee_values[0],
                  'Nome': employee_values[1],
                  'Email': employee_values[2],
                  'Sexo': employee_values[3],
                  'DataNascimento': employee_values[4],
                  'Salario': employee_values[5],
                  'Cargo': employee_values[6]
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
    if (dictionary['Salario'] != ''):
        if (string != ''):
            string += f" AND Salario = '{dictionary['Salario']}'"
        else:
            string += f"Salario = '{dictionary['Salario']}'"
    if (dictionary['Cargo'] != ''):
        if (string != ''):
            string += f" AND Cargo = '{dictionary['Cargo']}'"
        else:
            string += f"Cargo = '{dictionary['Cargo']}'"
    return string

def create_dictionary_fields (employee_values):
    dictionary = {'CPF': employee_values[0],
                  'Nome': employee_values[1],
                  'Email': employee_values[2],
                  'Sexo': employee_values[3],
                  'DataNascimento': employee_values[4],
                  'Salario': employee_values[5],
                  'Cargo': employee_values[6],
                  'COREN': employee_values[7],
                  'COFEN': employee_values[8],
                  'NumerosTelefone': employee_values[9],
                  'Rua': employee_values[10],
                  'Numero': employee_values[11],
                  'Complemento': employee_values[12]
                }
    return create_string_fields(dictionary)

def create_string_fields (dictionary):
    string = ''
    if (dictionary['CPF'] == True):
        string += f"f.CPF"
    if (dictionary['Nome'] == True):
        if (string != ''):
            string += f",f.Nome"
        else:
            string += f"f.Nome"
    if (dictionary['Email'] == True):
        if (string != ''):
            string += f",f.Email"
        else:
            string += f"f.Email"
    if (dictionary['Sexo'] == True):
        if (string != ''):
            string += f",f.Sexo"
        else:
            string += f"f.Sexo"
    if (dictionary['DataNascimento'] == True):
        if (string != ''):
            string += f",f.DataNascimento"
        else:
            string += f"f.DataNascimento"
    if (dictionary['Salario'] == True):
        if (string != ''):
            string += f",f.Salario"
        else:
            string += f"f.Salario"
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
    if (dictionary['Cargo'] == True):
        if (string != ''):
            string += f",f.Cargo"
        else:
            string += f"f.Cargo"
    if (dictionary['COREN'] == True):
        if (string != ''):
            string += f",enf.Registro_COREN"
        else:
            string += f"enf.Registro_COREN"
    if (dictionary['COFEN'] == True):
        if (string != ''):
            string += f",enf.Registro_COFEN"
        else:
            string += f"enf.Registro_COFEN"
    return string

def select_employee (fields,values):
    cursor.execute(f"SELECT {fields} FROM Funcionario as f LEFT OUTER JOIN Telefones_Funcionario AS t ON t.CPF_Funcionario = f.CPF LEFT OUTER JOIN Endereco_Funcionario AS e ON e.CPF_Funcionario = f.CPF LEFT OUTER JOIN Enfermeiro AS enf ON enf.CPF_Funcionario = f.CPF WHERE {values} GROUP BY f.CPF")
    field_names = [i[0] for i in cursor.description]
    results = []
    for client in cursor:
        results.append(client)
    return (results,field_names)

def select():
    cursor.execute(f"SELECT * FROM Funcionario")
    results = []
    field_names = [i[0] for i in cursor.description]
    for row in cursor:
        results.append(row)
    return (results,field_names)