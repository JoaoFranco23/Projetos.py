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
        self.button()
        Login.mainloop()
        
    def tela(self):#Esta funçao, estou configurando o tamanho da dimensão que a tela sera iniciada
        self.Login.title("Login")
        self.Login.configure(background='lightblue')#Configuração da tela e cores do fundo
        self.Login.geometry("600x500")#Definindo o Tamanho da tela
        self.Login.resizable(FALSE, FALSE)#Definindo se a tela sera expansiva
        self.Login = Label(Login, text="Login", background='lightblue', font=("Arial", 20)).pack() #Nesta variavel, definimos um titulo dentro do card
        
        #Frame para criarmos o card, login de acesso do usuario 
        #Email = Label(Login, text="Email", anchor=NW, font=('arial 10'))
        Email = Frame(Login, bg="lightblue", bd=1, relief="groove")
        Email = Entry(Login, textvariable= "Informe o email")
        Email.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.07)
        pass
        
        Senha = Frame(Login, bg="lightblue", bd=2, relief="groove", highlightthickness=1)
        Senha = Entry(Login, show="*", bd=1, width=25, justify='left', font=("", 15), highlightthickness=1,  relief="solid")
        Senha.place(y=2, x=2, relx=0.5, rely= 0.5, relwidth=0.6, relheight=0.07, anchor="center") 
        
    def button(self):
        self.btn = Frame(Login, bd=2, highlightthickness=1)
        self.btn = Button(self.Login, text="ENTRAR")
        self.btn.place(relx=0.5, rely=0.9, anchor="center", relwidth=0.3, width=55)
        
Application()
