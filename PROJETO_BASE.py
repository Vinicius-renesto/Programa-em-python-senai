import sqlite3 # banco de dados
import tkinter as tk # interface basica
from tkinter import messagebox # caixas de mensagens
from tkinter import ttk # interface grafica tb

def conectar():
    return sqlite3.connect('teste.db')
# criar o banco (connect)

def criar_tabela():
    conn = conectar()
    c= conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER NOT NULL,
        nome TEXT NOT NULL,
        email TEXT NOT NULL              
        )       
    ''')
    conn.commit()
    conn.close()
  


# CREATE
def inserir_usuario():
    nome = entry_nome.get()
    email = entry_email.get()
    cpf =  entry_cpf.get()

    if nome and email:
        conn = conectar()
        c = conn.cursor()
        c.execute('INSERT INTO usuarios(id,nome, email) VALUES(?,?,?)', (cpf,nome, email))
        conn.commit()
        conn.close()
        messagebox.showinfo('AVISO', 'DADOS INSERIDOS COM SUCESSO!') 
        mostrar_usuario()
    else:
        messagebox.showerror('ERRO', 'ALGO DEU ERRADO!') 

# READ
def mostrar_usuario():
    for row in tree.get_children():   
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()    
    c.execute('SELECT * FROM usuarios')
    usuarios = c.fetchall()
    for usuario in usuarios:
        tree.insert("", "end", values=(usuario[0], usuario[1],usuario[2]))
    conn.close()    


# DELETE
def delete_usuario():
    dado_del = tree.selection()
    if dado_del:
       user_id = tree.item(dado_del)['values'][0]
       conn = conectar()
       c = conn.cursor()    
       c.execute('DELETE FROM usuarios WHERE id = ? ',(user_id,))
       conn.commit()
       conn.close()
       messagebox.showinfo('', 'DADO DELETADO')
       mostrar_usuario()

    else:
       messagebox.showerror('', 'OCORREU UM ERRO')  

# UPDATE 
       
def editar():
     selecao = tree.selection()
     if selecao:
         user_id = tree.item(selecao)['values'][0]
         novo_nome = entry_nome.get()
         novo_email = entry_email.get()

         if novo_nome and novo_email:
            conn = conectar()
            c = conn.cursor()    
            c.execute('UPDATE usuarios SET nome = ? , email = ? WHERE id = ? ',(novo_nome,novo_email,user_id))
            conn.commit()
            conn.close()  
            messagebox.showinfo('', 'DADOS ATUALIZADOS')
            mostrar_usuario()

         else:
             messagebox.showwarning('', 'PREENCHA TODOS OS CAMPOS')

     else:
            messagebox.showerror('','ALGO DEU ERRADO!')


# VAMOS COMPLETAR A INTERFACE GRÁFICA...
# 1
janela = tk.Tk()
janela.title('CRUD')





label_nome = tk.Label(janela, text='Nome:')
label_nome.grid(row=0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_email = tk.Label(janela, text='E-mail:')
label_email.grid(row=1, column=0, padx=10, pady=10)
entry_email = tk.Entry(janela)
entry_email.grid(row=1, column=1, padx=10, pady=10)


label_cpf = tk.Label(janela, text='CPF:')
label_cpf.grid(row=2, column=0, padx=10, pady=10)

entry_cpf = tk.Entry(janela, text='CPF:')
entry_cpf.grid(row=2, column=1, padx=10, pady=10)



# botões

btn_salvar = tk.Button(janela, text='SALVAR',command=inserir_usuario)
btn_salvar.grid(row = 3, column=0, padx=10, pady=10  )

btn_deletar = tk.Button(janela, text='DELETAR',command=delete_usuario)
btn_deletar.grid(row = 3, column=1, padx=10, pady=10  )

btn_atualizar = tk.Button(janela, text='ATUALIZAR',command=editar)
btn_atualizar.grid(row = 3, column=2, padx=10, pady=10  )

# arvore
columns = ('ID','NOME', 'EMAIL')

tree = ttk.Treeview(janela, columns=columns, show='headings')
tree.grid(row=6, column=0,columnspan=2, padx=10, pady=10 )

for col in columns:
    tree.heading(col, text=col)

criar_tabela()
mostrar_usuario()


janela.mainloop()