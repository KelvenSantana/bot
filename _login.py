import tkinter as tk
from datetime import datetime, timedelta, timezone
from tkinter import messagebox
import subprocess

class LoginPage(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("250x150")
        self.configure(bg="black")


        self.label_username = tk.Label(self, text="Usuário:", bg="black", fg="white", font=("Arial", 12), pady=5)
        self.label_username.pack()
        self.entry_username = tk.Entry(self)
        self.entry_username.pack()

        self.label_password = tk.Label(self, text="Senha:", bg="black", fg="white", font=("Arial", 12), pady=5)
        self.label_password.pack()
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()

        self.button_login = tk.Button(self,  text="Entrar", bg="white",
            fg="black",
            font=("Arial", 10),
            relief=tk.RAISED,
            bd=2,
            padx=15,
            pady=8,
            activebackground="red",
            activeforeground="white",
            command=self.login)
        self.button_login.pack(pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if (
                username == "teste"
                and password == "teste"
                and self.verificar_login_valido()
        ):
            self.destroy()  # Fechar a tela de login
            self.executar_outro_arquivo()
        else:
            messagebox.showerror("Erro de Login", "Nome de usuário ou senha incorretos ou login expirado.")

    def verificar_login_valido(self):
        expiration_date = datetime(2023, 8, 24) + timedelta(days=30)
        data_atual = datetime.utcnow()
        return data_atual <= expiration_date


    def executar_outro_arquivo(self):
        try:
            subprocess.run(["python", "criarsalas.py"])
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo não encontrado.")



if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()
