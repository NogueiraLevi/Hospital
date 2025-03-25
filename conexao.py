import psycopg2

def conectar():
    return psycopg2.connect(
        dbname="hospital",
        user="postgres",
        password="postgresql",  # Substitua pela senha correta
        host="localhost",
        port="5432"
    )
