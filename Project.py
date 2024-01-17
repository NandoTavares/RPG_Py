import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class JoguinRPG:
    def __init__(self, master):
        self.master = master
        self.master.title("Mate os dragões")
        self.master.geometry("800x600")

        self.exibir_tela_inicial()

    def exibir_tela_inicial(self):
        self.limpar_tela()

        label = tk.Label(self.master, text="Bem vindo a um jogo inspirado em D&D de mesa!")
        label.pack(pady=10)

        btn_loja = tk.Button(self.master, text="Ir para a Loja", command=self.ir_para_loja)
        btn_loja.pack()

        btn_dungeon = tk.Button(self.master, text="Ir para a Dungeon", command=self.ir_para_dungeon)
        btn_dungeon.pack()

        btn_guilda = tk.Button(self.master, text="Ir para a Guilda", command=self.ir_para_guilda)
        btn_dungeon.pack()

    def ir_para_loja(self):
        self.limpar_tela()

        label = tk.Label(self.master, text="Você está na Loja. O que você gostaria de fazer?")
        label.pack(pady=10)

        btn_comprar = tk.Button(self.master, text="Comprar itens", command=self.comprar_itens)
        btn_comprar.pack()

        btn_sair_loja = tk.Button(self.master, text="Sair da Loja", command=self.exibir_tela_inicial)
        btn_sair_loja.pack()

    def comprar_itens(self):
        self.limpar_tela()

        btn_espada_comum = tk.Button(self.master, text="Espada Comum", command=self.espada_comum)
        btn_espada_comum.pack()

        btn_espada_magica = tk.Button(self.master, text="Espada Mágica", command=self.espada_magica)
        btn_espada_magica.pack()

        btn_pocao_comum = tk.Button(self.master, text="Poção Comum", command=self.pocao_comum)
        btn_pocao_comum.pack()

        btn_sair_loja = tk.Button(self.master, text="Sair da Loja", command=self.exibir_tela_inicial)
        btn_sair_loja.pack()

    def espada_comum(self):
        messagebox.showinfo("Ação", "Você comprou uma Espada Comum!")

    def pocao_comum(self):
        messagebox.showinfo("Ação", "Você comprou uma Poção Comum! você recuperou 15 pontos de vida, muito bem!")

    def espada_magica(self):
        messagebox.showinfo("Ação", "Você comprou uma Espada Mágica!")

    def ir_para_dungeon(self):
        self.limpar_tela()

        label = tk.Label(self.master, text="Você está na Dungeon. O que você gostaria de fazer?")
        label.pack(pady=10)

        btn_lutar = tk.Button(self.master, text="Lutar contra o monstro", command=self.lutar_contra_monstro)
        btn_lutar.pack()

        btn_fugir = tk.Button(self.master, text="Tentar fugir", command=self.tentar_fugir)
        btn_fugir.pack()

    def lutar_contra_monstro(self):
        mensagem = "Você está lutando contra o monstro!"
        messagebox.showinfo("Ação", mensagem)

    def tentar_fugir(self):
        resultado_dado = random.randint(1, 20)  

        mensagem = f"Você lançou um dado e obteve {resultado_dado}."

        if resultado_dado > 10:
            mensagem += "\nVocê conseguiu fugir da batalha!"
        else:
            mensagem += "\nVocê não conseguiu fugir e continua na batalha contra o monstro!"

        messagebox.showinfo("Resultado do dado", mensagem)

    def ir_para_guilda(self):
        mensagem = "Iria para a guilda, mas não ta completa kk tenta depois!"

    def limpar_tela(self):
        for widget in self.master.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JoguinRPG(root)
    root.mainloop()
