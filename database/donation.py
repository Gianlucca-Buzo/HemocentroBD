from database import cursor, db

def insert_donation (donation_values):
    cursor.execute("INSERT INTO Doacao (ID_Doador,ID_Enfermeiro,DataDoacao,Quantidade) VALUES %s" % (donation_values,))
    db.commit()
    return True