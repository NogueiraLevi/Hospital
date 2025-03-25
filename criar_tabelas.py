try:
    from conexao import conectar

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            idade INT NOT NULL,
            genero VARCHAR(10),
            telefone VARCHAR(20)    
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS consultas (
            id SERIAL PRIMARY KEY,
            paciente_id INT NOT NULL,
            data_consulta DATE NOT NULL,
            descricao TEXT,
            FOREIGN KEY (paciente_id) REFERENCES pacientes(id) ON DELETE CASCADE
        );
    """)

    conexao.commit()
    print("Tabelas criadas com sucesso!!")

except Exception as e:
    print("Erro ao criar tabelas:", e)

finally:
    cursor.close()
    conexao.close()
