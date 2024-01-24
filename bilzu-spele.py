from tkinter import* #importē tkinter bibliotēku
from PIL import ImageTk, Image
import random
from tkinter import messagebox
import time


gameWindow=Tk()
gameWindow.title("Vienādie attēli")
gameWindow.configure(bg="black")
gameWindow.resizable(1,1)


#ATTĒLU IMPORTS
IMG0=ImageTk.PhotoImage(Image.open("bulterjers.png").resize((180,180)))
IMG1=ImageTk.PhotoImage(Image.open("erdelterjers.jpg").resize((180,180)))
IMG2=ImageTk.PhotoImage(Image.open("foksterjers.jpg").resize((180,180)))
IMG3=ImageTk.PhotoImage(Image.open("keriblu-terjers.jpg").resize((180,180)))
IMG4=ImageTk.PhotoImage(Image.open("kviesu-terjers.jpg").resize((180,180)))


#ATTĒLU MASĪVS
imageList=[IMG0,IMG0,IMG1,IMG1,IMG2,IMG2,
IMG3,IMG3,IMG4,IMG4] #2 reizes katru, jo jābut pa pāriem
myLabel=Label(image=IMG1)


#FONA ATTĒLS
bgImg=ImageTk.PhotoImage(Image.open("kauls.jpg").resize((180,180))) #Image.ANTIALIAS


#izveido pogas - jābūt pāra skaitlim, piemēram, 10
btn0=Button(width=180,height=180,image=bgImg,command=lambda:btnClick(btn0,0)) #sāk no 0, jo sasaistās ar saraksta elementu indeksāciju
btn1=Button(width=180,height=180,image=bgImg,command=lambda:btnClick(btn1,1))
btn2=Button(width=180,height=180,image=bgImg,command=lambda:btnClick(btn2,2))
btn3=Button(width=180,height=180,image=bgImg,command=lambda:btnClick(btn3,3))
btn4=Button(width=180,height=180,image=bgImg,command=lambda:btnClick(btn4,4))
btn5=Button(width=180,height=180,image=bgImg,command=lambda:btnClick(btn5,5))
btn6=Button(width=180,height=180,image=bgImg,command=lambda:btnClick(btn6,6))
btn7=Button(width=180,height=180,image=bgImg,command=lambda:btnClick(btn7,7))
btn8=Button(width=180,height=180,image=bgImg,command=lambda:btnClick(btn8,8))
btn9=Button(width=180,height=180,image=bgImg,command=lambda:btnClick(btn9,9))

btn0.grid(row=0,column=0) #sāk no 0, jo sasaistās ar saraksta elementu indeksāciju
btn1.grid(row=0,column=1)
btn2.grid(row=0,column=2)
btn3.grid(row=0,column=3)
btn4.grid(row=0,column=4)
btn5.grid(row=1,column=0)
btn6.grid(row=1,column=1)
btn7.grid(row=1,column=2)
btn8.grid(row=1,column=3)
btn9.grid(row=1,column=4)
#saliek attēlus saraksta, katrs attēls 2 reizes


#ATTĒLU SAJAUKŠANA
random.shuffle(imageList)


count=0 #cik rūtiņu atvērtas
correctAnswers=0 #skaita pareizās atbildes
answers=[] #saraksts ar atbildēm. definē tukšu sarakstu - spēles laika tas aizpildās
answer_dict={} #kas ir piespiests, salīdzina ar attēliem no saraksta
answerCount=0


#"ATSTATĪŠANAS" FUNKCIJA
def reset():
    global count, correctAnswers, answers, answer_dict, answerCount
    btn0.config(state=NORMAL, image=bgImg)
    btn1.config(state=NORMAL, image=bgImg)
    btn2.config(state=NORMAL, image=bgImg)
    btn3.config(state=NORMAL, image=bgImg)
    btn4.config(state=NORMAL, image=bgImg)
    btn5.config(state=NORMAL, image=bgImg)
    btn6.config(state=NORMAL, image=bgImg)
    btn7.config(state=NORMAL, image=bgImg)
    btn8.config(state=NORMAL, image=bgImg)
    btn9.config(state=NORMAL, image=bgImg)

    btn0.config(image=bgImg)
    btn1.config(image=bgImg)
    btn2.config(image=bgImg)
    btn3.config(image=bgImg)
    btn4.config(image=bgImg)
    btn5.config(image=bgImg)
    btn6.config(image=bgImg)
    btn7.config(image=bgImg)
    btn8.config(image=bgImg)
    btn9.config(image=bgImg)


    random.shuffle(imageList)

    count=0
    correctAnswers=0
    answers=[]
    answer_dict={}
    answerCount=0


#INFOLOGA IZVEIDE
def infoLogs():
        gameWindow=Toplevel()
        gameWindow.title('Par programmu')
        gameWindow.geometry("500x300")
        apraksts=Label(gameWindow,text="Atrodi visas vienādās kartītes!")
        apraksts.grid(row=0,column=0)
        return 0


#FUNKCIJA
def btnClick(btn,number):
    global count,correctAnswers,answers,answer_dict, answerCount
    if btn["image"]=="pyimage5"and count<2: #pēc sistēmas nosauc šādi
        btn["image"]=imageList[number]
        count+=1 #viena rūtiņa atklāta
        answers.append(number) #pievieno pie atbildēm
        answer_dict[btn]=imageList[number]
    if len(answers)==2: #ja atvertas divas kartītes
        if imageList[answers[0]]==imageList[answers[1]]: #salīdzina attēlus, kas saglabats vārdnīcā ar attēlu sarakstā
            for key in answer_dict:
                key["state"]=DISABLED
            correctAnswers+=2
            if correctAnswers==2:
                correctAnswers=0
                answerCount+=1
        else:
            Tk.update(btn)
            time.sleep(1)
            for key in answer_dict:
                key["image"]="pyimage5"
        count = 0
        answers = []
        answer_dict = {}
    if answerCount==5:
        messagebox.showinfo("Super, Tu uzvarēji!")
        reset()


galvenaIzvelne=Menu(gameWindow)
gameWindow.config(menu=galvenaIzvelne)

opcijas=Menu(galvenaIzvelne,tearoff=False)
galvenaIzvelne.add_cascade(label="Opcijas", menu=opcijas)

opcijas.add_command(label="Jauna spēle",command=reset)
opcijas.add_command(label="Pārtraukt sesiju",command=gameWindow.quit)

galvenaIzvelne.add_command(label="Par programmu",command=infoLogs)


gameWindow.mainloop()