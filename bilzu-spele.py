from tkinter import* #importē tkinter bibliotēku
from PIL import ImageTk,Image
import random
from tkinter import messagebox

gameWindow=Tk()
gameWindow.title("Vienādie attēli")
#count=0
#Answcount=0

#izveido pogas - jābūt pāra skaitlim, piemēram, 10
btn0=Button(width=4,height=3) #sāk no 0, jo sasaistās ar saraksta elementu indeksāciju
btn1=Button(width=4,height=3)
btn2=Button(width=4,height=3)
btn3=Button(width=4,height=3)
btn4=Button(width=4,height=3)
btn5=Button(width=4,height=3)
btn6=Button(width=4,height=3)
btn7=Button(width=4,height=3)
btn8=Button(width=4,height=3)
btn9=Button(width=4,height=3)
btn10=Button(width=4,height=3)
btn11=Button(width=4,height=3)

btn0.grid(row=0,column=0) #sāk no 0, jo sasaistās ar saraksta elementu indeksāciju
btn1.grid(row=0,column=1)
btn2.grid(row=0,column=2)
btn3.grid(row=1,column=0)
btn4.grid(row=1,column=1)
btn5.grid(row=1,column=2)
btn6.grid(row=2,column=0)
btn7.grid(row=2,column=1)
btn8.grid(row=2,column=2)
btn9.grid(row=3,column=0)
btn10.grid(row=3,column=1)
btn11.grid(row=3,column=2)
#saliek attēlus saraksta, katrs attēls 2 reizes

bulterjers=ImageTk.PhotoImage(Image.open("bulterjers.png"))
erdelterjers=ImageTk.PhotoImage(Image.open("erdelterjers.jpg"))
foksterjers=ImageTk.PhotoImage(Image.open("foksterjers.jpg"))
keribluterjers=ImageTk.PhotoImage(Image.open("keriblu-terjers.jpg"))
kviesuterjers=ImageTk.PhotoImage(Image.open("kviesu-terjers.jpg"))

#FONA ATTĒLS
bgImg=Image.Tk.PhotoImage(Image.open("kauls.jpg").resize((200,200), Image.ANTIALIAS)) #attēlu saspiešanas metode

#resize((x,y))
gameWindow.mainloop()