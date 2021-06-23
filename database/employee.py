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
def insert_nurse (nurse_values,employee_values,address_values,number_values):
    if not exists_employee(nurse_values[0]):
        cursor.execute("INSERT INTO Funcionario VALUES %s" % (employee_values,))
        cursor.execute("INSERT INTO Enfermeiro VALUES %s" % (nurse_values,))
        db.commit()
        insert_address(address_values)
        insert_number(number_values)
        insert_cellphone(number_values)
        return True
    else:
        return False

#Insere admini
def insert_manager (manager_values,employee_values,address_values,number_values):
    if not exists_employee(employee_values[0]):
        cursor.execute("INSERT INTO Funcionario VALUES %s" % (employee_values,))
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