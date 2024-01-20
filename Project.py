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

        self.canvas = tk.Canvas(self.master, width=800, height=600)
        self.canvas.grid(row=0, column=0, sticky="NSEW")

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_photo)

        self.frame = tk.Frame(self.canvas, bg="white", highlightthickness=0)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.vida = 100
        self.var_vida = tk.StringVar()
        self.var_vida.set(f"Vida: {self.vida}")
        self.label_vida = tk.Label(self.master, textvariable=self.var_vida, font=('Helvetica', 12), bg="white")
        self.label_vida.place(relx=0.15, rely=0.05, anchor=tk.W)

        self.exibir_tela_inicial()

    class Monstro:
     def __init__(self, nome, vida, ataque):
      self.nome = nome
      self.vida = vida
      self.ataque = ataque

    class Goblin(Monstro):
     def __init__(self):
         super().__init__(nome="Goblin", vida=40, ataque=10)

    class Orc(Monstro):
     def __init__(self):
         super().__init__(nome="Orc", vida=120, ataque=15)

    class Golem(Monstro):
     def __init__(self):
         super().__init__(nome="Golem", vida=200, ataque=25)
    
    class Elemental(Monstro):
     def __init__(self):
         super().__init__(nome="Elemental", vida=300, ataque=35)

    class ElementalAncião(Monstro):
     def __init__(self):
         super().__init__(nome="Elemental Ancião", vida=500, ataque=45)
    
    class ElementalAncião(Monstro):
     def __init__(self):
         super().__init__(nome="Dragão Morto Vivo", vida=700, ataque=45)
    
    class Dragao(Monstro):
     def __init__(self):
        super().__init__(nome="Dragão", vida=1000, ataque=50)

    class DragaoAncião(Monstro):
     def __init__(self):
        super().__init__(nome="Dragão Ancião", vida=1400, ataque=100)

    class ReiDragão(Monstro):
     def __init__(self):
        super().__init__(nome="Rei Dragão do Mal", vida=2200, ataque=200)

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

        btn_ReiDragao = tk.Button(self.frame, text="Enfrentar o Rei Dragão Maligno", command=self.para_ReiDragao, highlightthickness=0)
        btn_ReiDragao.pack()


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

        btn_pocao_comum = tk.Button(self.frame, text="Poção Comum", command=self.pocao_comum, highlightthickness=0)
        btn_pocao_comum.pack()

        btn_espada_comum = tk.Button(self.frame, text="Espada Comum", command=self.espada_comum, highlightthickness=0)
        btn_espada_comum.pack()

        btn_espada_magica = tk.Button(self.frame, text="Espada Mágica", command=self.espada_magica, highlightthickness=0)
        btn_espada_magica.pack()

        btn_Martelo_Anão = tk.Button(self.frame, text="Martelo Anão ", command=self.Martelo_Anão, highlightthickness=0)
        btn_Martelo_Anão.pack()
        
        btn_Alabarda_Dourada = tk.Button(self.frame, text="Alabarda Dourada", command=self.Alabarda_Dourada, highlightthickness=0)
        btn_Alabarda_Dourada.pack()

        btn_Espada_elfica = tk.Button(self.frame, text="Espada Elfica", command=self.Espada_elfica, highlightthickness=0)
        btn_Espada_elfica.pack()
        
        btn_Matadora_de_Dragões = tk.Button(self.frame, text="Lendária Matadora de Dragões", command=self.Matadora_de_Dragões, highlightthickness=0)
        btn_Matadora_de_Dragões.pack()

        btn_sair_loja = tk.Button(self.frame, text="Sair da Loja", command=self.exibir_tela_inicial, highlightthickness=0)
        btn_sair_loja.pack()

    #aq vão as poções
    def pocao_comum(self):
        messagebox.showinfo("Ação", "Você comprou uma Poção Comum! você recuperou 15 pontos de vida, muito bem!")
        self.vida += 15
        print(f"Vida após a poção: {self.vida}")  
        self.atualizar_vida()

    def pocao_media(self):
        messagebox.showinfo("Ação", "Você comprou uma Poção Media! você recuperou 30 pontos de vida, muito bem!")
        self.vida += 30
        print(f"Vida após a poção: {self.vida}")  
        self.atualizar_vida()

    def pocao_grande(self):
        messagebox.showinfo("Ação", "Você comprou uma Poção Grande! você recuperou 50 pontos de vida, muito bem!")
        self.vida += 50
        print(f"Vida após a poção: {self.vida}")  
        self.atualizar_vida()

    def sangue_vampirico(self):
        messagebox.showinfo("Ação", "Você comprou uma Poção feita com sangue vampirico, que feito raro! você recuperou 90 pontos de vida, muito bem!")
        self.vida += 90
        print(f"Vida após a poção: {self.vida}")  
        self.atualizar_vida()

    def Lagrimas_de_sereias(self):
        messagebox.showinfo("Ação", "UOU, Você comprou uma Poção de Lagrimas de sereias, isso foi épico! você recuperou 90 pontos de vida, muito bem!")
        self.vida += 150
        print(f"Vida após a poção: {self.vida}")  
        self.atualizar_vida()

    def Fruto_elfico(self):
        messagebox.showinfo("Ação", "QUE? Você acaba de comer o fruto da árvoré dos Elfos, seu feito não será esquecido! você recuperou 400 pontos de vida, muito bem!")
        self.vida += 400
        print(f"Vida após a poção: {self.vida}")  
        self.atualizar_vida()

    
    #aq vão as armas
    def espada_comum(self):
        messagebox.showinfo("Ação", "Você comprou uma Espada Comum!")
        self.dano += 15  
        self.atualizar_vida()

    def espada_magica(self):
        messagebox.showinfo("Ação", "Você comprou uma Espada Mágica!")
        self.dano += 30  
        self.atualizar_vida()

    def Martelo_Anão(self):
        messagebox.showinfo("Ação", "Você comprou uma Martelo dos anões!")
        self.dano += 60  
        self.atualizar_vida()

    def Alabarda_Dourada(self):
        messagebox.showinfo("Ação", "Você comprou uma Alabarda Dourada!")
        self.dano += 120  
        self.atualizar_vida()

    def Espada_elfica(self):
        messagebox.showinfo("Ação", "Parabéns, você comprou uma espada dos tempos dos elfos. Talvez agora possa enfrentar o dragão Rei que assola as Terras!")
        self.dano += 240  
        self.atualizar_vida()

    def Matadora_de_Dragões(self):
        messagebox.showinfo("Ação", "Parabéns, você comprou uma espada matadora de dragões com poder de quebrar nações com seus golpes. Agora pode facilmente enfrentar o dragão Rei que assola as Terras!")
        self.dano += 400  
        self.atualizar_vida()

    def atualizar_vida(self):
     nova_vida = f"Vida: {self.vida}"
     self.var_vida.set(nova_vida)
     self.label_vida.config(text=nova_vida)


    def voltar_para_tela_inicial(self):
        self.exibir_tela_inicial()

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
            #aqui eu vou terminar o sistema de vida
            self.atualizar_vida()

        messagebox.showinfo("Resultado do dado", mensagem)
        
        def voltar_para_tela_inicial(self):
         self.exibir_tela_inicial()

    def ir_para_guilda(self):
        mensagem = "Iria para a guilda, mas não ta completa kk tenta depois!"
        messagebox.showinfo("Ação", mensagem)
        #label = tk.Label(self.frame, text="Você está na Guilda. O que você gostaria de fazer?")
        #label.pack(pady=10)

        #btn_pegar_missão = tk.Button(self.frame, text="Pegue sua missão", command=self.pegar_missão, highlightthickness=0)
        #btn_pegar_missão.pack()

        #btn_receber_pagamento = tk.Button(self.frame, text="Receba o pagamento de suas missões", command=self.receber_pagamento, highlightthickness=0)
        #btn_receber_pagamento.pack()

    def limpar_tela(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JoguinRPG(root)
    root.mainloop()
