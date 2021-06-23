import mysql.connector

db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="gzvnpy",
            database='HEMOCENTRO',
            auth_plugin='mysql_native_password'
        )
cursor = db.cursor()




