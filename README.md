# 🔐 Gerador de Senhas em Tkinter

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Funcional-success?style=for-the-badge)

Um simples e eficiente **gerador de senhas aleatórias**, desenvolvido com **Python** e **Tkinter**, ideal para quem quer criar senhas fortes rapidamente.
O app inclui geração personalizada por tamanho e botão para copiar direto para a área de transferência.

---

## ✨ Funcionalidades

* Define o tamanho da senha (mínimo de 5 caracteres)
* Gera senhas usando:

  * letras maiúsculas e minúsculas
  * números
  * símbolos
* Interface gráfica simples e direta (usando Tkinter)
* Botão para copiar a senha para a área de transferência
* Mensagens úteis de erro e status

---

## 📸 Prévia da Interface

> *(Adicione aqui sua captura de tela após gerar a imagem)*

```
![preview](docs/preview.png)
```

---

## 🚀 Como executar

1. Certifique-se de ter o **Python 3.10+** instalado.
2. Rode o script:

```bash
python gerador_senhas.py
```

3. A interface surgirá na tela.
4. Defina o tamanho desejado ➜ clique em **Gerar Senha** ➜ opcionalmente clique em **Copiar**.

---

## 🧠 Lógica do Gerador

A senha é formada combinando:

```python
caracteres = string.ascii_letters + string.digits + string.punctuation
```

E selecionando caracteres aleatórios:

```python
senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
```

---

## 📁 Estrutura sugerida

```
📂 gerador-senhas/
 ├── gerador_senhas.py
 ├── README.md
 └── docs/
     └── preview.png
```

---

## 👩‍💻 Autor

**Thaís de Sousa Campos**

Desenvolvedora Python em evolução, apaixonada por projetos práticos e aprendizagem constante.

* 💼 GitHub: [github.com/snakegirlcode](https://github.com/snakegirlcode/)
* 🔗 LinkedIn: [linkedin.com/in/thaiscamposdev](https://www.linkedin.com/in/thaiscamposdev/)

---

## 💡 Melhorias futuras

* Adicionar opção de escolher tipos de caracteres
* Slider para ajustar o tamanho
* Tema escuro (dark mode)
* Exportar senha para arquivo `.txt`

---

## 📜 Licença

Este projeto está sob a licença **MIT**.
Sinta-se livre para usar, modificar e distribuir.
