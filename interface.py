import tkinter as tk
import requests

API_URL = "http://SEU_IP:5000"

def enviar_comando(comando):
    try:
        r = requests.post(f"{API_URL}/comando", json={"comando": comando})
        atualizar_status()
    except Exception as e:
        status_var.set("Erro ao enviar comando")

def atualizar_status():
    try:
        estado = requests.get(f"{API_URL}/comando").json()["estado"]
        erro = requests.get(f"{API_URL}/status").json()["erro"]
        status_var.set(f"Porta: {estado.upper()}")
        erro_var.set(f"Erro: {erro or 'Nenhum'}")
    except:
        status_var.set("Falha ao consultar API")

# Interface
root = tk.Tk()
root.title("Controle da Porta")

status_var = tk.StringVar()
erro_var = tk.StringVar()

tk.Label(root, text="Controle da Porta via Wi-Fi", font=("Arial", 16)).pack(pady=10)
tk.Button(root, text="ABRIR", command=lambda: enviar_comando("abrir"), width=20).pack(pady=5)
tk.Button(root, text="FECHAR", command=lambda: enviar_comando("fechar"), width=20).pack(pady=5)
tk.Label(root, textvariable=status_var, font=("Arial", 12)).pack(pady=10)
tk.Label(root, textvariable=erro_var, fg="red", font=("Arial", 10)).pack()

atualizar_status()
root.mainloop()
