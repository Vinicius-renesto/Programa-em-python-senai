import sqlite3  # Banco de dados
import tkinter as tk  # Interface básica
from tkinter import messagebox  # Caixas de mensagens
from tkinter import ttk  # Interface gráfica

# Função para conectar ao banco de dados
def conectar():
    return sqlite3.connect('clinica_saude.db')

# Função para criar a tabela de pacientes no banco de dados
def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        peso REAL NOT NULL,
        altura REAL NOT NULL,
        imc REAL
        )
    ''')
    conn.commit()
    conn.close()

# Função para calcular o IMC
def calcular_imc(peso, altura):
    try:
        imc = peso / (altura ** 2)
        return round(imc, 2)
    except ZeroDivisionError:
        return 0.0

# Função para inserir um novo paciente
def inserir_paciente():
    nome = entry_nome.get()
    idade = entry_idade.get()
    peso = entry_peso.get()
    altura = entry_altura.get()

    if nome and idade and peso and altura:
        try:
            idade = int(idade)
            peso = float(peso)
            altura = float(altura)
            imc = calcular_imc(peso, altura)
            
            conn = conectar()
            c = conn.cursor()
            c.execute('INSERT INTO pacientes(nome, idade, peso, altura, imc) VALUES(?, ?, ?, ?, ?)', 
                      (nome, idade, peso, altura, imc))
            conn.commit()
            conn.close()
            messagebox.showinfo('AVISO', 'PACIENTE CADASTRADO COM SUCESSO!')
            mostrar_pacientes()
        except ValueError:
            messagebox.showerror('ERRO', 'POR FAVOR, INSIRA VALORES VÁLIDOS!')
    else:
        messagebox.showerror('ERRO', 'PREENCHA TODOS OS CAMPOS!')

# Função para mostrar todos os pacientes cadastrados
def mostrar_pacientes():
    for row in tree.get_children():
        tree.delete(row)
    
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM pacientes')
    pacientes = c.fetchall()
    for paciente in pacientes:
        tree.insert("", "end", values=(paciente[0], paciente[1], paciente[2], paciente[3], paciente[4], paciente[5]))
    conn.close()

# Função para excluir um paciente
def excluir_paciente():
    dado_del = tree.selection()
    if dado_del:
        paciente_id = tree.item(dado_del)['values'][0]
        conn = conectar()
        c = conn.cursor()
        c.execute('DELETE FROM pacientes WHERE id = ?', (paciente_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo('AVISO', 'PACIENTE EXCLUÍDO COM SUCESSO!')
        mostrar_pacientes()
    else:
        messagebox.showerror('ERRO', 'SELECIONE UM PACIENTE PARA EXCLUIR!')

# Função para editar as informações de um paciente
def editar_paciente():
    selecao = tree.selection()
    if selecao:
        paciente_id = tree.item(selecao)['values'][0]
        novo_nome = entry_nome.get()
        nova_idade = entry_idade.get()
        novo_peso = entry_peso.get()
        nova_altura = entry_altura.get()

        if novo_nome and nova_idade and novo_peso and nova_altura:
            try:
                nova_idade = int(nova_idade)
                novo_peso = float(novo_peso)
                nova_altura = float(nova_altura)
                imc = calcular_imc(novo_peso, nova_altura)
                
                conn = conectar()
                c = conn.cursor()
                c.execute('UPDATE pacientes SET nome = ?, idade = ?, peso = ?, altura = ?, imc = ? WHERE id = ?',
                          (novo_nome, nova_idade, novo_peso, nova_altura, imc, paciente_id))
                conn.commit()
                conn.close()
                messagebox.showinfo('AVISO', 'DADOS ATUALIZADOS COM SUCESSO!')
                mostrar_pacientes()
            except ValueError:
                messagebox.showerror('ERRO', 'POR FAVOR, INSIRA VALORES VÁLIDOS!')
        else:
            messagebox.showwarning('AVISO', 'PREENCHA TODOS OS CAMPOS!')
    else:
        messagebox.showerror('ERRO', 'SELECIONE UM PACIENTE PARA EDITAR!')

# Interface gráfica
janela = tk.Tk()
janela.title('Cadastro de Pacientes - Clínica Saúde & Bem-Estar')

# Labels e campos de entrada
label_nome = tk.Label(janela, text='Nome:')
label_nome.grid(row=0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_idade = tk.Label(janela, text='Idade:')
label_idade.grid(row=1, column=0, padx=10, pady=10)
entry_idade = tk.Entry(janela)
entry_idade.grid(row=1, column=1, padx=10, pady=10)

label_peso = tk.Label(janela, text='Peso (kg):')
label_peso.grid(row=2, column=0, padx=10, pady=10)
entry_peso = tk.Entry(janela)
entry_peso.grid(row=2, column=1, padx=10, pady=10)

label_altura = tk.Label(janela, text='Altura (m):')
label_altura.grid(row=3, column=0, padx=10, pady=10)
entry_altura = tk.Entry(janela)
entry_altura.grid(row=3, column=1, padx=10, pady=10)

# Botões para salvar, excluir e editar
btn_salvar = tk.Button(janela, text='Salvar', command=inserir_paciente)
btn_salvar.grid(row=4, column=0, padx=10, pady=10)

btn_excluir = tk.Button(janela, text='Excluir', command=excluir_paciente)
btn_excluir.grid(row=4, column=1, padx=10, pady=10)

btn_atualizar = tk.Button(janela, text='Atualizar', command=editar_paciente)
btn_atualizar.grid(row=4, column=2, padx=10, pady=10)

# Configuração da tabela para mostrar os pacientes
columns = ('ID', 'Nome', 'Idade', 'Peso', 'Altura', 'IMC')

tree = ttk.Treeview(janela, columns=columns, show='headings')
tree.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

for col in columns:
    tree.heading(col, text=col)

# Função para inicializar o sistema e mostrar os pacientes cadastrados
criar_tabela()
mostrar_pacientes()

# Iniciar a interface
janela.mainloop()
