from salas1 import executar_sequencia_cliques
from salas2 import executar_sequencia_cliques2
from salas3 import executar_sequencia_cliques3
from salas4 import executar_sequencia_cliques4
from salas1 import on_button_click
from verificar import find_bluestacks_window, find_image_on_screen, take_screenshot_bluestacks
import tkinter as tk


bluestacks_window = find_bluestacks_window()
if bluestacks_window:
    take_screenshot_bluestacks(
        (bluestacks_window.left, bluestacks_window.top, bluestacks_window.width, bluestacks_window.height))
else:
    print("Janela do Bluestacks não encontrada.")

template_image_path = "berm.png"  # Substitua pelo caminho da imagem que você deseja encontrar
screenshot_path = "bluestacks_screenshot.png"

match_locations = find_image_on_screen(template_image_path, screenshot_path)

if match_locations:
    print("Imagem encontrada nas posições:", match_locations)
    # Realize a ação desejada quando a imagem for encontrada.
else:
    print("Imagem não encontrada.")

janela = tk.Tk()
janela.title("BOT SALAS")
janela.geometry("230x300")
janela.configure(bg="darkblue")

botao_cliques = tk.Button(janela, text="Conect Inst", bg="black", fg="white", font=("Arial", 10), command=on_button_click())
botao_cliques.pack(pady=15)

botao_cliques = tk.Button(janela, text="SALA 1", bg="black", fg="white", font=("Arial", 10), command=executar_sequencia_cliques)
botao_cliques.pack(pady=15)

botao_cliques = tk.Button(janela, text="SALA 2", bg="black", fg="white", font=("Arial", 10), command=executar_sequencia_cliques2)
botao_cliques.pack(pady=15)

botao_cliques = tk.Button(janela, text="SALA 3", bg="black", fg="white", font=("Arial", 10), command=executar_sequencia_cliques3)
botao_cliques.pack(pady=15)

botao_cliques = tk.Button(janela, text="SALA 4", bg="black", fg="white", font=("Arial", 10), command=executar_sequencia_cliques4)
botao_cliques.pack(pady=15)

janela.mainloop()