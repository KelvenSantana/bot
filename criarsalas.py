from salas1 import executar_sequencia_cliques
from salas2 import executar_sequencia_cliques2
from salas3 import executar_sequencia_cliques3
from salas4 import executar_sequencia_cliques4
import tkinter as tk

janela = tk.Tk()
janela.title("BOT SALAS")
janela.geometry("230x280")
janela.configure(bg="#708090")

botao_cliques = tk.Button(janela, text="SALA 1", bg="black", fg="white", font=("Arial", 10), command=executar_sequencia_cliques)
botao_cliques.pack(pady=15)

botao_cliques = tk.Button(janela, text="SALA 2", bg="black", fg="white", font=("Arial", 10), command=executar_sequencia_cliques2)
botao_cliques.pack(pady=15)

botao_cliques = tk.Button(janela, text="SALA 3", bg="black", fg="white", font=("Arial", 10), command=executar_sequencia_cliques3)
botao_cliques.pack(pady=15)

botao_cliques = tk.Button(janela, text="SALA 4", bg="black", fg="white", font=("Arial", 10), command=executar_sequencia_cliques4)
botao_cliques.pack(pady=15)

janela.mainloop()