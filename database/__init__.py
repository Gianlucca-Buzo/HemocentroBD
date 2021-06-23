import mysql.connector

db = mysql.connector.connect(
            host="localhost",
            user="lucca",
            passwd="lucca2021",
            database='HEMOCENTRO',
            auth_plugin='mysql_native_password'
        )
cursor = db.cursor(buffered=True)




