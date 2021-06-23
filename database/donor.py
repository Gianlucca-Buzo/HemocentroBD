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
        return True
    else:
        return False

def insert_address (address_values):
    cursor.execute("INSERT INTO Endereco_Doador VALUES %s" % (address_values,))
    db.commit()
    return True

def insert_number (number_values):
    cursor.execute("INSERT INTO Telefones_Doador VALUES %s" % (number_values,))
    db.commit()
    return True

def verify_cursor(cursor):
    for x in cursor:
        return True
    return False

