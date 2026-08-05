import tkinter as tk

class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        


c = Cliente("Ana Sousa", "85 99999-9999")

janela = tk.Tk()
janela.title("AgendaFacil")
janela.geometry("360x220")

tk.Label(janela, text="Cliente cadastrado",
         font=("Arial", 12)).pack(pady=(24, 4))

tk.Label(janela, text=c.telefone,
         font=("Arial", 14), fg="gray30").pack(pady=6)

janela.mainloop()