import sqlite3
import tkinter as tk
from tkinter import messagebox



def create_db():
    conn =  sqlite3.connect('meu_banco.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL)''')
    conn.commit()
    conn.close()


def salvar():
    nome = entry_nome.get()

    if nome:
        conn =  sqlite3.connect('meu_banco.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pessoas  (nome) VALUES (?)", (nome,))
        conn.commit()
        conn.close()
        messagebox.showinfo('CONFIRMADO', 'EFETUADO COM SUCESSO')
        listar_nomes()
        limpar_campos()
    else:
        messagebox.showerror('Erro', 'Algo não funciona')

def listar_nomes():
    conn =  sqlite3.connect('meu_banco.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pessoas")
    registros =  cursor.fetchall()
    conn.close()

    listbox.delete(0, tk.END)
    for registro in registros:
        listbox.insert(tk.END, f" ID: {registro[0]},Nome: {registro[1]}")


def limpar_campos():
    entry_nome.delete(0, tk.END)   



root = tk.Tk()
root.title('Cadastro de pessoas ')

tk.Label(root, text='Nome: ').grid(row= 0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(root)
entry_nome.grid(row = 0, column=1, padx= 10, pady= 10)

btn_salvar = tk.Button(root, text='Salvar', command=salvar)
btn_salvar.grid(row = 1,  columnspan=2, pady=10 )

listbox = tk.Listbox(root, width=40, height=10)
listbox.grid(row=2, columnspan=2, padx=10, pady=10)

create_db()
listar_nomes()

root.mainloop()