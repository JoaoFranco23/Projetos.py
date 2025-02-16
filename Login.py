#importando uma interface tkinter
from tkinter import * 
from tkinter import ttk
from tkinter import Frame
from tkinter import Entry
from tkinter import Label

Login = Tk() 

#Foi criado uma funçao "Loop" dentro da classe
class Application():
    def __init__(self):
        self.Login = Login
        self.tela()
        Login.mainloop()
        
    def tela(self):#Esta funçao, estou definindo o tamanho da dimensão que a tela sera iniciada
        self.Login.title("Login")
        self.Login.configure(background='lightblue')#Configuração da tela e cores do fundo
        self.Login.geometry("600x500")#Definindo o Tamanho da tela
        self.Login.resizable(FALSE, FALSE)#Definindo se a tela sera expansiva
        self.Login = Label(Login, text="Login", background='lightblue', font=("Arial", 20)).pack() #Nesta variavel, definimos um titulo dentro do card
        
        #Frame para criarmos o card, login de acesso do usuario 
        Email = Frame(Login, bg="lightblue", bd=2, relief="groove")
        Email = Entry(Login, textvariable= "Informe o email")
        Email.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.07)
        
        def frame_senha_tela(self):
            
Application()
