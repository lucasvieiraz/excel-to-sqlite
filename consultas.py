import sqlite3

conn = sqlite3.connect("controle_2026.db")
cursor = conn.cursor()

cursor.execute("SELECT PLACA, SETOR, VALOR FROM controle WHERE DATA = '09/01/2026'")
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)

conn.close() 
