from tkinter import *
from tkinter import messagebox
from random import *
import random
import qrcode
import psycopg2

class Banco():
    def __init__(self):
        self.conn = psycopg2.connect(
            host = "localhost",
            database = "qrcode",
            user = "postgres",
            password = "pabd"
        )
    
        self.cursor = self.conn.cursor()

    def inserOne(self, id, url, path):
        self.cursor.execute("INSERT INTO tbcodes (id_code, url, qr_code_path) VALUES ({}, '{}', '{}')".format(id, url, path))
        self.conn.commit()

def gerar_qr_code():
    url = texto_resposta.get()

    if (len(url)==0):
        messagebox.showinfo(
            title="Erro!",
            message='Inserir URL válida'

        )
    else:
        opcao = messagebox.askokcancel(
            title=url,
            message=f"O endereço é: \n"
            f"Endereço: {url} \n"
            f"Salvar?"
        )
    
    if opcao:
        qr = qrcode.QRCode(version=1,box_size=10,border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img=qr.make_image(fill_color='black',back_color='white')
        img_name = 'qrExport.png'
        img.save('qrExport.png')
        banco.inserOne(2, url, 'qrcode.png')



banco = Banco()

janela = Tk()
janela.title('Gerador de Código QRCode')





texto = Label(janela, text= 'ID:')
texto.grid(column=0,row=2,padx=10,pady=10)

texto = Label(janela, text= 'URL')
texto.grid(column=0,row=2,padx=10,pady=10)

texto = Label(janela, text= 'NOME')
texto.grid(column=0,row=2,padx=10,pady=10)

texto_resposta = Entry(width=45)
texto_resposta.grid(column=1,row=2,columnspan=2)

botao = Button(janela,text='Gerar QRCode',command=gerar_qr_code)
botao.grid(column=1,row=3,padx=10,pady=10)

janela.mainloop()