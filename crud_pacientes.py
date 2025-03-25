from conexao import conectar

# CRIANDO CRUD

def inserir_pacientes(nome, idade, genero, telefone):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO pacientes(nome, idade, genero, telefone)
        VALUES (%s, %s, %s, %s) RETURNING id;
    """, (nome, idade, genero, telefone))
    
    paciente_id = cursor.fetchone()[0]
    conexao.commit()
    
    print(f'Paciente de ID: {paciente_id} criado com sucesso!!')

    conexao.close()
    cursor.close()

def listar_pacientes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM pacientes;")
    pacientes = cursor.fetchall()

    for paciente in pacientes:
        print(paciente)  # Exibir dados no terminal

    conexao.close()
    cursor.close()

def atualizar_paciente(id, nome, idade, genero, telefone):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE pacientes SET nome=%s, idade=%s, genero=%s, telefone=%s
        WHERE id=%s;
    """, (nome, idade, genero, telefone, id))
    
    conexao.commit()
    print("Paciente atualizado com sucesso")

    cursor.close()
    conexao.close()

def excluir_paciente(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM pacientes WHERE id=%s", (id,))  # Corrigido aqui
    conexao.commit()

    print("Paciente excluído com sucesso")

    conexao.close()
    cursor.close()
