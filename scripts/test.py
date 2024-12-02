import mysql.connector
import json
import getpass


db_server = "andph.eu"
db_port = 3306
db_name = "nosta_world"

db_user = input("Zadejte uživatelské jméno: ")
db_pass = getpass.getpass(prompt='Zadejte heslo: ')
try:
	conn = mysql.connector.connect(
		host = db_server,
		port = db_port,
		database = db_name,
		user = db_user,
		password = db_pass
	)
except mysql.connector.Error as err:
	# Potlačení tracebacku, vypsání vlastní chybové zprávy
	print(f"Chyba při připojování k databázi: {err}")
	exit(1)

cur = conn.cursor()

cur.execute("SELECT * FROM item_template WHERE VerifiedBuild >= 30000")


results = cur.fetchall()
for row in results:
    print(row.name)


cur.close()
conn.close()
