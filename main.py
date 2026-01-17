import sqlite3
import pandas as pd

excel_file = "Controle 2026.xlsx"

db_file = "controle_2026.db"

table_name = "controle"

# Processo
df = pd.read_excel(excel_file)

conn = sqlite3.connect(db_file)

# Criar a tabela e inserir os dados automaticamente
df.to_sql(table_name, conn, if_exists="replace", index=False)

conn.close()

print("Banco de dados SQLite criado com sucesso!")
