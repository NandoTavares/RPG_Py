import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os

class JoguinRPG:
    def __init__(self, master):
        self.master = master
        self.master.title("Mate os dragões")
        self.master.geometry("800x600")

        try:
            img_path = os.path.join("C:\\Users\\Ernandes\\Downloads\\programação\\outrosprojetos\\app_django.py\\roleplay\\imagens", "Aventura_de_RPG.jpg")
            background_image = Image.open(img_path)
            self.background_photo = ImageTk.PhotoImage(background_image)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar a imagem: {str(e)}")

        # Cria o canvas após carregar a imagem
        self.canvas = tk.Canvas(self.master, width=800, height=600)
        self.canvas.pack()

        # Exibe a imagem no canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_photo)

        # Cria um frame para organizar os widgets
        self.frame = tk.Frame(self.canvas, bg="white", highlightthickness=0)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.exibir_tela_inicial()

    def exibir_tela_inicial(self):

        label = tk.Label(self.frame, text="Bem vindo a um jogo inspirado em D&D de mesa!")
        label.pack(pady=10)

        self.limpar_tela()

        label = tk.Label(self.frame, text="Bem vindo a um jogo inspirado em D&D de mesa!")
        label.pack(pady=10)

        btn_loja = tk.Button(self.frame, text="Ir para a Loja", command=self.ir_para_loja, highlightthickness=0)
        btn_loja.pack()

        btn_dungeon = tk.Button(self.frame, text="Ir para a Dungeon", command=self.ir_para_dungeon, highlightthickness=0)
        btn_dungeon.pack()

        btn_guilda = tk.Button(self.frame, text="Ir para a Guilda", command=self.ir_para_guilda, highlightthickness=0)
        btn_guilda.pack()


    def ir_para_loja(self):
        self.limpar_tela()

        label = tk.Label(self.frame, text="Você está na Loja. O que você gostaria de fazer?")
        label.pack(pady=10)

        btn_comprar = tk.Button(self.frame, text="Comprar itens", command=self.comprar_itens, highlightthickness=0)
        btn_comprar.pack()

        btn_sair_loja = tk.Button(self.frame, text="Sair da Loja", command=self.exibir_tela_inicial, highlightthickness=0)
        btn_sair_loja.pack()

    def comprar_itens(self):
        self.limpar_tela()

        btn_espada_comum = tk.Button(self.frame, text="Espada Comum", command=self.espada_comum, highlightthickness=0)
        btn_espada_comum.pack()

        btn_espada_magica = tk.Button(self.frame, text="Espada Mágica", command=self.espada_magica, highlightthickness=0)
        btn_espada_magica.pack()

        btn_pocao_comum = tk.Button(self.frame, text="Poção Comum", command=self.pocao_comum, highlightthickness=0)
        btn_pocao_comum.pack()

        btn_sair_loja = tk.Button(self.frame, text="Sair da Loja", command=self.exibir_tela_inicial, highlightthickness=0)
        btn_sair_loja.pack()

    def espada_comum(self):
        messagebox.showinfo("Ação", "Você comprou uma Espada Comum!")

    def pocao_comum(self):
        messagebox.showinfo("Ação", "Você comprou uma Poção Comum! você recuperou 15 pontos de vida, muito bem!")

    def espada_magica(self):
        messagebox.showinfo("Ação", "Você comprou uma Espada Mágica!")

    def ir_para_dungeon(self):
        self.limpar_tela()

        label = tk.Label(self.frame, text="Você está na Dungeon. O que você gostaria de fazer?")
        label.pack(pady=10)

        btn_lutar = tk.Button(self.frame, text="Lutar contra o monstro", command=self.lutar_contra_monstro, highlightthickness=0)
        btn_lutar.pack()

        btn_fugir = tk.Button(self.frame, text="Tentar fugir", command=self.tentar_fugir, highlightthickness=0)
        btn_fugir.pack()

    def lutar_contra_monstro(self):
        mensagem = "Você está lutando contra o monstro!"
        messagebox.showinfo("Ação", mensagem)

    def tentar_fugir(self):
        resultado_dado = random.randint(1, 20)
        mensagem = f"Você lançou um dado e obteve {resultado_dado}."

        if resultado_dado > 10:
            mensagem += "\nVocê conseguiu fugir da batalha!"
            self.voltar_para_tela_inicial()
        else:
            mensagem += "\nVocê não conseguiu fugir e continua na batalha contra o monstro!"

        messagebox.showinfo("Resultado do dado", mensagem)
        
        def voltar_para_tela_inicial(self):
         self.exibir_tela_inicial()

    def ir_para_guilda(self):
        mensagem = "Iria para a guilda, mas não ta completa kk tenta depois!"
        messagebox.showinfo("Ação", mensagem)

    def limpar_tela(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JoguinRPG(root)
    root.mainloop()
