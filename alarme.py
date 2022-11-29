from customtkinter import *
from tkinter import PhotoImage, messagebox
import time
from pygame import mixer

#Funçao para criar o alarme
def alarme():
    hora = int(caixa.get())
    minuto= int(caixa2.get())
    segundo= int(caixa3.get())
    
    r= hora*3600 + minuto*60 + segundo*1
    
    if r != 0:
        time.sleep(r)
        mixer.init()
        mixer.music.load("audio/alarme.mp3")
        mixer.music.play()
    else:
        messagebox.showinfo("ERRO", "Por favor digite um valor válido")
    
#Tela
root = CTk()
root.geometry("600x320")
root.configure(background="#575656")
root.title("Alarme")
root.iconbitmap("img/clock.ico")

#Imagem
imagem = PhotoImage(file="img/off.png")

#Labels
txt=CTkLabel(text="Alarme", fg_color="#575656", text_color="white",text_font="Arial 42 bold")
hora=CTkLabel(text="Hora(s)", fg_color="#575656", text_color="white",text_font="Arial 12 bold")
minutos=CTkLabel(text="Minuto(s)", fg_color="#575656", text_color="white",text_font="Arial 12 bold")
segundos=CTkLabel(text="Segundo(s)", fg_color="#575656", text_color="white",text_font="Arial 12 bold")

#Frame
f= CTkFrame(root, fg_color="#FFA800",width=547)

#ComboBoxs
caixa = CTkComboBox(root,text_font = "Arial 18 bold",values=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"),width=75,height=35)
caixa2 = CTkComboBox(root,text_font = "Arial 18 bold",values=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"),width=75,height=35)
caixa3 = CTkComboBox(root,text_font = "Arial 18 bold",values=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"),width=75,height=35)

#Sets
caixa.set("00")
caixa2.set("00")
caixa3.set("00")

#Botões
boff= CTkButton(root,text="OFF",fg_color="#B73F2A", hover_color="#963826", text_color="white",width=95,height=85, command=lambda:[mixer.music.pause()],text_font="Arial 16 bold")
bon= CTkButton(root,text="ON",fg_color="#349238", hover_color="#2D7D31", text_color="white",width=95,height=85, command=alarme,text_font="Arial 16 bold")
bexit= CTkButton(image=imagem, text= "", fg_color="#585757", width= 15, height=15, hover=OFF, command=exit)

#Places
hora.place(x=110,y=90)
minutos.place(x=220,y=90)
segundos.place(x=330,y=90)
txt.place(x=205,y=10)
f.place(x=25,y=70,height=5)
caixa.place(x=150,y=120)
caixa2.place(x=250,y=120)
caixa3.place(x=350,y=120)
boff.place(x=290, y=200)
bon.place(x=195, y=200)
bexit.place(x=5, y=260)
root.mainloop()