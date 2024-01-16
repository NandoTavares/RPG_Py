import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class JoguinRPG:
    def __init__(self, master):
        self.master = master
        self.master.title("Mate os dragões")
        self.master.geometry("800x600")  # Corrected line
        #background_image = Image.open("Aqui vem o caminho da imagem que vou colocar depois")
        #background_photo = ImageTk.PhotoImage(background_image)

        self.exibir_tela_inicial()

    def exibir_tela_inicial(self):
        self.limpar_tela()

        label = tk.Label(self.master, text="Bem vindo a um  jogo expirado em um d&d de mesa bem simplificado !")
        label.pack(pady=10)

        btn_loja = tk.Button(self.master, text="Ir para a Loja", command=self.ir_para_loja)
        btn_loja.pack()

        btn_dungeon = tk.Button(self.master, text="Ir para a Dungeon", command=self.ir_para_dungeon)
        btn_dungeon.pack()

    def ir_para_loja(self):
        self.limpar_tela()

        label = tk.Label(self.master, text="Você está na Loja. O que você gostaria de fazer?")
        label.pack(pady=10)

        btn_comprar = tk.Button(self.master, text="Comprar itens", command=self.comprar_itens)
        btn_comprar.pack()

        btn_sair_loja = tk.Button(self.master, text="Sair da Loja", command=self.exibir_tela_inicial)
        btn_sair_loja.pack()

    def ir_para_dungeon(self):
        self.limpar_tela()

        label = tk.Label(self.master, text="Você está na Dungeon. O que você gostaria de fazer?")
        label.pack(pady=10)

        btn_lutar = tk.Button(self.master, text="Lutar contra o monstro", command=self.lutar_contra_monstro)
        btn_lutar.pack()

        btn_fugir = tk.Button(self.master, text="Fugir da Dungeon", command=self.exibir_tela_inicial)
        btn_fugir.pack()

    def comprar_itens(self):
        messagebox.showinfo("Ação", "Você comprou alguns itens!")

    def lutar_contra_monstro(self):
        messagebox.showinfo("Ação", "Você está lutando contra um monstro!")

    def limpar_tela(self):
        for widget in self.master.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JoguinRPG(root)
    root.mainloop()
