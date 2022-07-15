from tkinter import *
import random

win1 = 0
draw1 = 0
losses1 = 0
bot = 0


def gamesecond():
    #Закрытие вступления
    first.destroy()
    #Открытие игрового окна
    game = Tk()
    game.title(" Камень-ножницы-бумага ")
    game.geometry('500x300+525+200')
    game.config(bg="Antiquewhite1")

    def gamefunctionrock():
        global bot, win1, draw1, losses1
        bot = random.randint(1,3)
        def win():
            win = Label(game, text="Вы выиграли!")
            win.config(height=3, width=15, bg="Antiquewhite1", fg="green", bd=1, relief="ridge", font=15)
            win.place(x=180, y=100)
            global win1
            win1 += 1
            winscore = Label(game, text=("Побед:", win1), bg="Antiquewhite1", fg="orange red", font=10)
            winscore.place(x=56, y=1)
            win.after(1700, lambda: win.destroy())
        def draw():
            draw = Label(game, text="Ничья!")
            draw.config(height=3, width=15, bg="Antiquewhite1", fg="slate gray", bd=1, relief="ridge", font=15)
            draw.place(x=180, y=100)
            global draw1
            draw1 += 1
            drawscore = Label(game, text=("Ничьих:", draw1), bg="Antiquewhite1", fg="orange red", font=10)
            drawscore.place(x=214, y=1)
            draw.after(1700, lambda: draw.destroy())
        def losses():
            losses = Label(game, text="Вы проиграли!")
            losses.config(height=3, width=15, bg="Antiquewhite1", fg="red", bd=1, relief="ridge", font=15)
            losses.place(x=180, y=100)
            global losses1
            losses1 += 1
            lossesscore = Label(game, text=("Проигрышей:", losses1), bg="Antiquewhite1", fg="orange red", font=10)
            lossesscore.place(x=360, y=1)
            losses.after(1700, lambda: losses.destroy())
        if bot==1:
            draw()
        if bot==2:
            win()
        if bot==3:
            losses()
    def gamefunctionscis():
        global bot, win1, draw1, losses1
        bot = random.randint(1,3)
        def win():
            win = Label(game, text="Вы выиграли!")
            win.config(height=3, width=15, bg="Antiquewhite1", fg="green", bd=1, relief="ridge", font=15)
            win.place(x=180, y=100)
            global win1
            win1 += 1
            winscore = Label(game, text=("Побед:", win1), bg="Antiquewhite1", fg="orange red", font=10)
            winscore.place(x=56, y=1)
            win.after(1700, lambda: win.destroy())
        def draw():
            draw = Label(game, text="Ничья!")
            draw.config(height=3, width=15, bg="Antiquewhite1", fg="slate gray", bd=1, relief="ridge", font=15)
            draw.place(x=180, y=100)
            global draw1
            draw1 += 1
            drawscore = Label(game, text=("Ничьих:", draw1), bg="Antiquewhite1", fg="orange red", font=10)
            drawscore.place(x=214, y=1)
            draw.after(1700, lambda: draw.destroy())
        def losses():
            losses = Label(game, text="Вы проиграли!")
            losses.config(height=3, width=15, bg="Antiquewhite1", fg="red", bd=1, relief="ridge", font=15)
            losses.place(x=180, y=100)
            global losses1
            losses1 += 1
            lossesscore = Label(game, text=("Проигрышей:", losses1), bg="Antiquewhite1", fg="orange red", font=10)
            lossesscore.place(x=360, y=1)
            losses.after(1700, lambda: losses.destroy())
        if bot==1:
            losses()
        if bot==2:
            draw()
        if bot==3:
            win()
    def gamefunctionpaper():
        global bot, win1, draw1, losses1
        bot = random.randint(1,3)
        def win():
            win = Label(game, text="Вы выиграли!")
            win.config(height=3, width=15, bg="Antiquewhite1", fg="green", bd=1, relief="ridge", font=15)
            win.place(x=180, y=100)
            global win1
            win1 += 1
            winscore = Label(game, text=("Побед:", win1), bg="Antiquewhite1", fg="orange red", font=10)
            winscore.place(x=56, y=1)
            win.after(1700, lambda: win.destroy())
        def draw():
            draw = Label(game, text="Ничья!")
            draw.config(height=3, width=15, bg="Antiquewhite1", fg="slate gray", bd=1, relief="ridge", font=15)
            draw.place(x=180, y=100)
            global draw1
            draw1 += 1
            drawscore = Label(game, text=("Ничьих:", draw1), bg="Antiquewhite1", fg="orange red", font=10)
            drawscore.place(x=214, y=1)
            draw.after(1700, lambda: draw.destroy())
        def losses():
            losses = Label(game, text="Вы проиграли!")
            losses.config(height=3, width=15, bg="Antiquewhite1", fg="red", bd=1, relief="ridge", font=15)
            losses.place(x=180, y=100)
            global losses1
            losses1 += 1
            lossesscore = Label(game, text=("Проигрышей:", losses1), bg="Antiquewhite1", fg="orange red", font=10)
            lossesscore.place(x=360, y=1)
            losses.after(1700, lambda: losses.destroy())
        if bot==1:
            win()
        if bot==2:
            losses()
        if bot==3:
            draw()

    rock = Button(game, text="Камень") # Кнопка - Камень
    rock.config(height = 3, width = 15, bg="azure3", fg="black",
            activebackground="black", activeforeground="white", bd=1, relief= "ridge",
            )
    rock.place(x=35,y=246)
    rock.configure(command=gamefunctionrock)
    #rock.grid(column = 1, row = 0)

    scis = Button(game, text="Ножницы") #Кнопка - Ножницы
    scis.config(height = 3, width = 15, bg="slategray2", fg="black",
            activebackground="black", activeforeground="white", bd=1, relief= "ridge")
    scis.place(x=195, y=246)
    scis.configure(command=gamefunctionscis)
    # scis.grid(column = 1, row = 2)

    paper = Button(game, text="Бумага")  #Кнопка - Бумага
    paper.config(height = 3, width = 15, bg="white", fg="black",
             activebackground="black", activeforeground="white", bd=1, relief= "ridge")
    paper.place(x=350,y=246)
    paper.configure(command=gamefunctionpaper)
    # paper.grid(column = 1, row = 4)

    global win1,draw1,losses1
    winscore = Label(game, text=("Побед:",win1), bg="Antiquewhite1", fg="orange red", font = 10)
    winscore.place(x=56,y=1)
    drawscore = Label(game, text=("Ничьих:", draw1), bg="Antiquewhite1", fg="orange red", font=10)
    drawscore.place(x=214, y=1)
    lossesscore = Label(game, text=("Проигрышей:", losses1), bg="Antiquewhite1", fg="orange red", font=10)
    lossesscore.place(x=360,y=1)

    game.mainloop()

#Окно вступления
first = Tk()
first.title("Добро пожаловать!")
first.geometry('500x300+525+200')
first.config(bg="Antiquewhite1")
#Кнопка перехода
welc = Button(first, text="Приветствую, поиграем?")
welc.config(height = 6, width = 25, bg="salmon3", fg="white",
            activebackground="sienna1", activeforeground="white", bd=1, relief= "ridge")
welc.place(x=155,y=80)
me = Label(first, text="DK", bg="Antiquewhite1", fg="orange red")
me.place(x=481,y=284)
version = Label(first, text="version-1.0", bg="Antiquewhite1", fg="orange red")
version.place(x=0,y=284)
welc.configure(command=gamesecond)
first.mainloop()



