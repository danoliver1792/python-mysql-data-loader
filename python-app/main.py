import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)

cursor = conn.cursor()

# criando um novo banco de dados
cursor.execute("CREATE DATABASE IF NOT EXISTS pessoa")
cursor.execute("USE pessoa")

# criando a tabela
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS nome (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255)
    )
    """
)

# inserindo dados
data = [
    ("Alberto", "Junior"),
    ("Joao", "Machado"),
    ("Joice", "Silva"),
    ("Amanda", "Moreira"),
    ("Eduardo", "Brandao"),
    ("Carla", "Pereira"),
    ("Amado", "Basilio"),
    ("Camila", "Fernanda"),
    ("Carlos", "Amaral"),
    ("Renata", "Candida")
]

insert_query = "INSERT INTO nome (first_name, last_name) VALUES (%s, %s)"

cursor.executemany(insert_query, data)

conn.commit()

cursor.close()
conn.close()
