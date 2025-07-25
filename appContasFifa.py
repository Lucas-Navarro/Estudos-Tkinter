import tkinter as tk

appFifa = tk.Tk()

appFifa.geometry('768x660')
appFifa.title('Sequência Fifa Contas')
appFifa.iconbitmap('./assets/LogoCoins.ico')
appFifa.configure(background='#2e2e2e')

botaoSair = tk.Button(appFifa, text='Sair', command=quit)
botaoSair.pack()

appFifa.mainloop()