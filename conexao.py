import psycopg2

def conectar():
    return psycopg2.connect(
        dbname="hospital",
        user="postgres",
        password="sua_senha",  # Substitua pela senha correta
        host="localhost",
        port="5432"
    )
