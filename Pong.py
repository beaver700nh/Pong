from tkinter import *
import time as animation
import random as pick_a

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 270, 270)

        from_starts = [-3, -2, -1, 1, 2, 3]
        chosen = pick_a.choice(from_starts)
        self.x = chosen
        self.y = -3
        self.window_height = self.canvas.winfo_height()
        self.window_width = self.canvas.winfo_width()
        self.hit_botom = False

    def hit_paddle(self, position):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if position[2] >= paddle_pos[0] and position [0] <= paddle_pos[2]:
            if position[3] >= paddle_pos[1] and position [3] <= paddle_pos[3]:
                return True
        return False
    
    def animate(self):
        self.canvas.move(self.id, self.x, self.y)
        ball_pos = self.canvas.coords(self.id)
        if ball_pos[0] <= 0:
            self.x = 3
        if ball_pos[1] <= 0:
            self.y = 1
        if ball_pos[2] >= self.window_width:
            self.x = -3
        if ball_pos[3] >= self.window_height:
            self.hit_botom = True
        if self.hit_paddle(ball_pos) == True:
            self.y = -3

class Paddle:
    def __init__(self, canvas, color):
                 # , x_pos, y_pos, control_left, control_right):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 450)

        self.x = 0
        self.window_width = self.canvas.winfo_width()

        self.canvas.bind_all('<KeyPress-Left>', self.move)
        self.canvas.bind_all('<KeyPress-Right>', self.move)
        
    def move(self, event):
        if event.keysym == 'Right':
            self.x = 2
        elif event.keysym == 'Left':
            self.x = -2

    def animate(self):
        self.canvas.move(self.id, self.x, 0)
        paddle_pos = self.canvas.coords(self.id)
        if paddle_pos[0] <= 0:
            self.x = 0
        elif paddle_pos[2] >= self.window_width:
            self.x = 0

tk = Tk()
tk.title('Pong')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)

canvas = Canvas(tk, width=600, height=600, bd=0, highlightthickness=0)
canvas.pack()

tk.update()

player1 = Paddle(canvas, 'blue')
                 # , 250, 150, 'a', 'd')
# player2 = Paddle(canvas, 'blue', 250, 460, 'j', 'l')
ball = Ball(canvas, player1, 'red')

while not ball.hit_botom:
    ball.animate()
    player1.animate()
    # player2.animate()
    
    tk.update_idletasks()
    tk.update()
    animation.sleep(0.01)
