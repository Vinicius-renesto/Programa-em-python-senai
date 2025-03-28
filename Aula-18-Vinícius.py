import tkinter as tk



def display():
    print( 'ISSO É UM TESTE ')

def display2():
    texto = entry1.get()
    text_label2.config(text=f'{texto}')



janela =  tk.Tk()
janela.title('Teste tkinter')

janela.geometry('500x500')

text_label = tk.Label(janela,text = 'ISSO É UM TEXTO')
text_label.pack(pady=10)

entry1 = tk.Entry(janela)
entry1.pack(pady=10)

btn = tk.Button(janela, text='ESCREVE UM TEXTO NO TERMINAL',command=display)
btn.pack(pady=10)

btn2 = tk.Button(janela, text='ESCREVE UM TEXTO NA TELA',command=display2)
btn2.pack(pady=10)

text_label2 = tk.Label(janela,text = 'AQUI VAI APARECER UM TEXTO')
text_label2.pack(pady=10)


janela.mainloop()