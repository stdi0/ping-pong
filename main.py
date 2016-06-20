# -*- coding: UTF-8 -*-
from tkinter import *
from time import sleep

WIDTH = 300
HEIGHT = 700
PADDLE_W = 50
PADDLE_H = 15

class PingPongGame:
    x = 4 #angle
    y = 6 #speed
    score_c = 0
    score_p = 0

    def move(self, event):
        if event.keysym == 'Right' and self.canv.coords(self.PADDLE_P)[2] < WIDTH:
                self.canv.move(self.PADDLE_P,10,0)
        if event.keysym == 'Left' and self.canv.coords(self.PADDLE_P)[0] > 0:
                self.canv.move(self.PADDLE_P,-10,0)

    #The second player        
    #if event.keysym == 'd' and canv.coords(PADDLE_C)[2] < WIDTH:
    #        canv.move(PADDLE_C,10,0)
    #if event.keysym == 'a' and canv.coords(PADDLE_C)[0] > 0:
    #        canv.move(PADDLE_C,-10,0)        

    def __init__(self):

        self.canv = Canvas(root, width = WIDTH, height = HEIGHT, background="#003300")
        self.canv.pack()

        self.im ='/Users/irina_dashevskaya/project/example.gif'
        self.ph_im = PhotoImage(file=self.im)
        self.canv.create_image(1,1,anchor=NW,image=self.ph_im)
        self.canv.create_line(0,HEIGHT/2,WIDTH,HEIGHT/2, width=3, fill="white")
        self.canv.create_line(0,HEIGHT-PADDLE_H,WIDTH,HEIGHT-PADDLE_H, width=1, fill="white")
        self.canv.create_line(0,PADDLE_H,WIDTH,PADDLE_H, width=1, fill="white")

        self.PADDLE_C = self.canv.create_rectangle(0,0,PADDLE_W,PADDLE_H, fill="White", outline="white")
        self.PADDLE_P = self.canv.create_rectangle(0,HEIGHT-PADDLE_H,PADDLE_W,HEIGHT, fill="White", outline="white")
        self.BALL = self.canv.create_oval([140,340],[160,360], fill="white")

        self.score_block_c = self.canv.create_text(30,HEIGHT/2/2, text="0", font="Verdana 12", fill="white")
        self.score_block_p = self.canv.create_text(30,HEIGHT/2+HEIGHT/2/2, text="0", font="Verdana 12", fill="white")

        root.bind("<KeyPress>", self.move)


    def collision_checking(self):
        if self.canv.coords(self.BALL)[3] >= HEIGHT-PADDLE_H and self.canv.coords(self.PADDLE_P)[0] <= (self.canv.coords(self.BALL)[2] - self.canv.coords(self.BALL)[0])  / 2 + self.canv.coords(self.BALL)[0] <= self.canv.coords(self.PADDLE_P)[2]:
            self.y = -6
        if self.canv.coords(self.BALL)[1] <= PADDLE_H and self.canv.coords(self.PADDLE_C)[0] <= (self.canv.coords(self.BALL)[2] - self.canv.coords(self.BALL)[0])  / 2 + self.canv.coords(self.BALL)[0] <= self.canv.coords(self.PADDLE_C)[2]:
            self.y = 6
        if self.canv.coords(self.BALL)[2] == WIDTH:
            self.x = -4
        if self.canv.coords(self.BALL)[0] == 0: 
            self.x = 4

    def spawn_ball(self):
        self.canv.coords(self.BALL,140,340,160,360)

    def update_score(self, player):
        if player == 'second':
            self.score_c += 1
            self.canv.itemconfig(self.score_block_c, text=str(self.score_c))
            self.spawn_ball()
        if player == 'first':
            self.score_p += 1
            self.canv.itemconfig(self.score_block_p, text=str(self.score_p))
            self.spawn_ball()

    def goal_checking(self):
        if self.canv.coords(self.BALL)[1] <= 0:
            self.update_score('first')
        if self.canv.coords(self.BALL)[3] >= HEIGHT:
            self.update_score('second')

    def go(self):
        #Collision checking
        #Сhecking on the goal
        self.collision_checking()
        self.goal_checking()

        #AI:
        #if canv.coords(BALL)[1] <= HEIGHT / 2:
        if (self.canv.coords(self.PADDLE_C)[2] - self.canv.coords(self.PADDLE_C)[0]) / 2 + self.canv.coords(self.PADDLE_C)[0] < (self.canv.coords(self.BALL)[2] - self.canv.coords(self.BALL)[0])  / 2 + self.canv.coords(self.BALL)[0] and self.canv.coords(self.PADDLE_C)[2] < WIDTH:
            self.canv.move(self.PADDLE_C,3,0)
        if (self.canv.coords(self.PADDLE_C)[2] - self.canv.coords(self.PADDLE_C)[0]) / 2 + self.canv.coords(self.PADDLE_C)[0] > (self.canv.coords(self.BALL)[2] - self.canv.coords(self.BALL)[0])  / 2 + self.canv.coords(self.BALL)[0] and self.canv.coords(self.PADDLE_C)[0] > 0:
            self.canv.move(self.PADDLE_C,-3,0)    

        self.canv.move(self.BALL,self.x,self.y)
        self.canv.after(30,self.go)
       
root = Tk()
newgame = PingPongGame()
newgame.go()
root.mainloop()

if __name__ == "__main__":
    newgame.go()

