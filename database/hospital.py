def insert_hospital (hospital_values,address_values,number_values):
    cursor.execute("INSERT INTO Hospital (Nome, Email) VALUES %s" % (hospital_values,))
    db.commit()
    insert_address(address_values)
    insert_number(number_values)
    return True

def insert_address (address_values):
    cursor.execute("INSERT INTO Endereco_Hospital VALUES %s" % (address_values,))
    db.commit()
    return True

def insert_number (number_values):
    cursor.execute("INSERT INTO Telefones_Hospital VALUES %s" % (number_values,))
    db.commit()
    return True