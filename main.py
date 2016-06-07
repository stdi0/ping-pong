# -*- coding: UTF-8 -*-
from tkinter import *
from time import sleep


WIDTH = 300
HEIGHT = 700
PADDLE_W = 50
PADDLE_H = 15

def collision_checking():
    global x, y
    if canv.coords(BALL)[3] >= HEIGHT-PADDLE_H and canv.coords(PADDLE_P)[0] <= (canv.coords(BALL)[2] - canv.coords(BALL)[0])  / 2 + canv.coords(BALL)[0] <= canv.coords(PADDLE_P)[2]:
        y = -6
    if canv.coords(BALL)[1] <= PADDLE_H and canv.coords(PADDLE_C)[0] <= (canv.coords(BALL)[2] - canv.coords(BALL)[0])  / 2 + canv.coords(BALL)[0] <= canv.coords(PADDLE_C)[2]:
        y = 6
    if canv.coords(BALL)[2] == WIDTH:
        x = -4
    if canv.coords(BALL)[0] == 0: 
        x = 4

def spawn_ball():
    canv.coords(BALL,140,340,160,360)

def update_score(player):
    global score_c, score_p
    if player == 'second':
        score_c += 1
        canv.itemconfig(score_block_c, text=str(score_c))
        spawn_ball()
    if player == 'first':
        score_p += 1
        canv.itemconfig(score_block_p, text=str(score_p))
        spawn_ball()

def goal_checking():
    if canv.coords(BALL)[1] <= 0:
        update_score('first')
        #score_p += 1
        #canv.itemconfig(score_block_p, text=str(score_p))
        #canv.coords(BALL,140,340,160,360)
    if canv.coords(BALL)[3] >= HEIGHT:
        update_score('second')
        #score_c += 1
        #canv.itemconfig(score_block_c, text=str(score_c))
        #canv.coords(BALL,140,340,160,360)     


def go():
    #Collision checking
    #Сhecking on the goal
    global x, y
    collision_checking()
    goal_checking()

    #AI:
    #if canv.coords(BALL)[1] <= HEIGHT / 2:
    #if (canv.coords(PADDLE_C)[2] - canv.coords(PADDLE_C)[0]) / 2 + canv.coords(PADDLE_C)[0] < (canv.coords(BALL)[2] - canv.coords(BALL)[0])  / 2 + canv.coords(BALL)[0] and canv.coords(PADDLE_C)[2] < WIDTH:
    #        canv.move(PADDLE_C,3,0)
    #if (canv.coords(PADDLE_C)[2] - canv.coords(PADDLE_C)[0]) / 2 + canv.coords(PADDLE_C)[0] > (canv.coords(BALL)[2] - canv.coords(BALL)[0])  / 2 + canv.coords(BALL)[0] and canv.coords(PADDLE_C)[0] > 0:
    #        canv.move(PADDLE_C,-3,0)    

    canv.move(BALL,x,y)
    canv.after(30,go)

def move(event):
    print(event.keysym)
    #if event.state == 'KeyRelease':
    #    pass
    #else:    
    #    print(event.keysym)
    if event.keysym == 'Right' and canv.coords(PADDLE_P)[2] < WIDTH:
            canv.move(PADDLE_P,10,0)
    if event.keysym == 'Left' and canv.coords(PADDLE_P)[0] > 0:
            canv.move(PADDLE_P,-10,0)
    if event.keysym == 'd' and canv.coords(PADDLE_C)[2] < WIDTH:
            canv.move(PADDLE_C,10,0)
    if event.keysym == 'a' and canv.coords(PADDLE_C)[0] > 0:
            canv.move(PADDLE_C,-10,0)        


root = Tk()
canv = Canvas(root, width = WIDTH, height = HEIGHT, background="#003300")
canv.pack()


canv.create_line(0,HEIGHT/2,WIDTH,HEIGHT/2, width=3, fill="white")
canv.create_line(0,HEIGHT-PADDLE_H,WIDTH,HEIGHT-PADDLE_H, width=1, fill="white")
canv.create_line(0,PADDLE_H,WIDTH,PADDLE_H, width=1, fill="white")

PADDLE_C = canv.create_rectangle(0,0,PADDLE_W,PADDLE_H, fill="White", outline="white")
PADDLE_P = canv.create_rectangle(0,HEIGHT-PADDLE_H,PADDLE_W,HEIGHT, fill="White", outline="white")
BALL = canv.create_oval([140,340],[160,360], fill="white")

score_block_c = canv.create_text(30,HEIGHT/2/2, text="0", font="Verdana 12", fill="white")
score_block_p = canv.create_text(30,HEIGHT/2+HEIGHT/2/2, text="0", font="Verdana 12", fill="white")

root.bind("<Right>", move)
root.bind("<Left>", move)
#The second player
root.bind("<a>", move)
root.bind("<d>", move)


x = 4 #angle
y = 6 #speed
score_c = 0
score_p = 0
go()

root.mainloop()
