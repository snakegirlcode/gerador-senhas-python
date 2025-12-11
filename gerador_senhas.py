import tkinter as tk
import random
import string


def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
        if tamanho < 5:
            resultado.set("A senha deve ter pelo menos 5 caracteres!")
            return
    except ValueError:
        resultado.set("Digite um número válido!")
        return

    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    resultado.set(senha)


def copiar_senha():
    senha = resultado.get()
    if not senha or "Digite" in senha or "pelo menos" in senha:
        status.set("Nada para copiar.")
        return
    janela.clipboard_clear()
    janela.clipboard_append(senha)
    status.set("Senha copiada para a área de transferência!")


janela = tk.Tk()
janela.title("Gerador de Senhas 🔐")
janela.geometry("420x220")

tk.Label(janela, text="Tamanho da senha (mínimo 5):").pack(pady=5)
entry_tamanho = tk.Entry(janela, width=10, justify="center")
entry_tamanho.pack(pady=5)
entry_tamanho.insert(0, "12")

tk.Button(janela, text="Gerar Senha", command=gerar_senha).pack(pady=8)

resultado = tk.StringVar()
tk.Label(
    janela, textvariable=resultado, font=("Arial", 12), fg="blue", wraplength=380
).pack(pady=8)

tk.Button(janela, text="Copiar", command=copiar_senha).pack(pady=5)

status = tk.StringVar()
tk.Label(janela, textvariable=status, font=("Arial", 10), fg="green").pack(pady=5)

janela.mainloop()
