from database import cursor, db

def select():
    cursor.execute(f"SELECT * FROM Estoque")
    for client in cursor:
        num_campos = len(client)
        for i in range (0,num_campos):
            print(client[i])