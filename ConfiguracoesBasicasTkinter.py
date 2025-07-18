import tkinter as tk

# Chama o tkinter
appTeste = tk.Tk()

# Mudar o titulo padrão do app
appTeste.title('App teste')

# Tamanho da tela
appTeste.geometry('600x400')

# Para evitar que consigue redimensionar a página, Primeiro parametro Width, Segundo Height
appTeste.resizable(False,False)

# Adicionar a transparencia no app
appTeste.attributes('-alpha', 0.9)

# Adicionar um icon para o app
appTeste.iconbitmap('./assets/image-_1_.ico')

# Criação de um texto
mensagem = tk.Label(appTeste, text='Olá, mundo')
mensagem.pack() # Faz com que pareça a label

# Inicializar a janela
appTeste.mainloop()