from tkinter import *
import time as animation
import random as pick_a
import sys as system

print('"Pong" by Minh Le')
print('Running using python\n' + system.version)
print('-------------------------------------------------------')

class Pong:
    def __init__(self, title, border, top):
        self.tk = Tk()
        self.tk.title(title)
        self.tk.resizable(0, 0)
        if top == True:
            self.tk.wm_attributes('-topmost', 1)

        if border == True:
            self.canvas = Canvas(self.tk, width=600, height=600, bd=0, highlightthickness=0)
        elif not border:
            self.canvas = Canvas(self.tk, width=600, height=600)
            
        self.canvas.pack()
        self.redraw()

    def redraw(self):
        self.tk.update_idletasks()
        self.tk.update()

    def kill(self, seconds):
        animation.sleep(seconds)
        self.tk.destroy()
        

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 270, 270)

        from_starts = [-10, -5, -3, -2, -1, 1, 2, 3, 5, 10]
        chosen = pick_a.choice(from_starts)
        self.x = chosen
        self.y = -3
        self.window_height = self.canvas.winfo_height()
        self.window_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def bounce(self):
        self.y = -self.y
        
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
            self.hit_bottom = True

class Paddle:
    def __init__(self, canvas, color, ball, x_pos, y_pos, control_left, control_right):
        self.left_ctrl = control_left
        self.right_ctrl = control_right
        self.canvas = canvas
        self.ball = ball
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, x_pos, y_pos)

        self.x = 0
        self.window_width = self.canvas.winfo_width()

        self.canvas.bind_all(self.left_ctrl, self.move_paddle)
        self.canvas.bind_all(self.right_ctrl, self.move_paddle)
        
    def move_paddle(self, event):
        if event.keysym == self.right_ctrl:
            self.x = 2
        elif event.keysym == self.left_ctrl:
            self.x = -2

    def hit_ball(self):
        ball_pos = self.canvas.coords(self.ball.id)
        x3 = (ball_pos[0] + ball_pos[2]) / 2
        y3 = (ball_pos[1] + ball_pos[3]) / 2
        
        def inside_paddle(x, y):
            return \
            x >= self.paddle_pos[0] and \
            y >= self.paddle_pos[1] and \
            x <= self.paddle_pos[2] and \
            y <= self.paddle_pos[3]
        
        return \
        inside_paddle(ball_pos[0], y3) or \
        inside_paddle(ball_pos[2], y3) or \
        inside_paddle(x3, ball_pos[1]) or \
        inside_paddle(x3, ball_pos[3])

    def animate(self):
        self.canvas.move(self.id, self.x, 0)
        self.paddle_pos = self.canvas.coords(self.id)
        if self.paddle_pos[0] <= 0 or \
           self.paddle_pos[2] >= self.window_width:
            self.canvas.move(self.id, -self.x, 0)
            
        if self.hit_ball():
            self.ball.bounce()

game = Pong(title='Pong', border=True, top=True)

ball = Ball(game.canvas, 'red')
player1 = Paddle(game.canvas, 'blue', ball, 250, 150, 'a', 'd')
player2 = Paddle(game.canvas, 'blue', ball, 250, 460, 'j', 'l')

try:
    while not ball.hit_bottom:
        ball.animate()
        player1.animate()
        player2.animate()
    
        game.redraw()
        animation.sleep(0.01)

except TclError:
    pass

print('Game Over')
game.kill(seconds=1.5)
