from tkinter import *
import random
import time





class Ball:
    def __init__(self, canvas, paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.x_speed = 2
        self.y_speed = 2
        self.id = canvas.create_oval(10, 10, 25, 25, fill = ball_1_color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -self.x_speed
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.secend_ball = False
        self.start_secend_ball = False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = self.y_speed
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -self.y_speed
            point_label = Label(tk, font = ('Times New Roman', 12, 'bold'),
                fg = 'red', bg = background_color)
            point_label.config(text = 'point : ' + str(points))
            point_label.place(x = 0, y = 0)
            if points == ball1_speed1:
                ball.x_speed += 1
                ball.y_speed += 1
                paddle.paddle_speed += 1.5
            if points == ball1_speed2:
                ball.x_speed += 1
                ball.y_speed += 1
                paddle.paddle_speed += 1.5
            if points == create_ball2:  
                self.secend_ball = True
                self.start_secend_ball = True
                paddle.paddle_speed += 1
        if pos[0] <= 0:
            self.x = self.x_speed
        if pos[2] >= self.canvas_width:
            self.x = -self.x_speed
    
    def hit_paddle(self, pos):
        global points
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                points += 1
                return True
        return False


class Ball_2:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.x_speed = 2
        self.y_speed = 2
        self.color = color
        self.id = canvas.create_oval(10, 10, 25, 25, fill = self.color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -self.x_speed
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = self.y_speed

        if pos[3] >= self.canvas_height:
            self.hit_bottom = True

        if self.hit_paddle(pos) == True:
            self.y = -self.y_speed
            point_label = Label(tk, font = ('Times New Roman', 12, 'bold'),
                fg = 'red', bg = background_color)
            point_label.config(text = 'point : ' + str(points))
            point_label.place(x = 0, y = 0)

            if points == ball2_speed1:
                ball_2.x_speed += 1
                ball_2.y_speed += 1
                paddle.paddle_speed += 1
            if points == ball2_speed2:
                ball_2.x_speed += 1
                ball_2.y_speed += 1
                paddle.paddle_speed += 1
        if pos[0] <= 0:
            self.x = self.x_speed

        if pos[2] >= self.canvas_width:
            self.x = -self.x_speed

    def hit_paddle(self, pos):
        global points
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                points += 1
                return True
        return False



class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color
        self.id = canvas.create_rectangle(0, 0, 150, 10, fill = self.color)
        self.canvas.move(self.id, 200, 400)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_lef)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.x = 0
        self.paddle_speed = 3
        self.canvas_width = self.canvas.winfo_width()
        self.start_game = False

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0

    def turn_lef(self, evt):
        self.start_game = True
        self.x = -self.paddle_speed

    def turn_right(self, evt):
        self.start_game = True
        self.x = self.paddle_speed



tk = Tk()
tk.title('paddle and ball game')
tk.resizable(0,0)

tk.wm_attributes('-topmost', 1)

ball_1_color = '#FF6B6B'
ball_2_color = '#FFD93D'
paddle_color = '#6BCB77'
background_color = '#4D96FF'


canvas = Canvas(tk, width = 650, height = 500, bd = 0, bg = background_color , highlightthickness = 0)

points = 0

point_label = Label(tk, font = ('Times New Roman', 12, 'bold'),fg = 'red', bg = background_color)
point_label.config(text = 'point : ' + str(points))
point_label.place(x = 0, y = 0)

canvas.pack()
tk.update()

paddle = Paddle(canvas, paddle_color)
ball = Ball(canvas, paddle)

ball1_speed1 = 2
ball1_speed2 = 4
create_ball2 = 6
ball2_speed1 = 8
ball2_speed2 = 10



while True:
    if paddle.start_game == True:
        if points <= create_ball2:
            if ball.hit_bottom == False:
                if ball.secend_ball == True:
                    ball_2 = Ball_2(canvas, paddle, ball_2_color)
                    ball.secend_ball = False
                if ball.start_secend_ball == True:
                    ball_2.draw()
                ball.draw()
                paddle.draw()
            if ball.hit_bottom == True:
                Label(tk, text = 'Game Over', font = ('Times New Roman', 26, 'bold'), bg = background_color
                , fg = 'red').place(x = ball.canvas_width/2 - 75, y = ball.canvas_height/2-50)
        else:
            if ball.hit_bottom == False and ball_2.hit_bottom == False:
                ball_2.draw()
                ball.draw()
                paddle.draw()
            else:
                Label(tk, text = 'Game Over', font = ('Times New Roman', 26, 'bold'), bg = background_color
                , fg = 'red').place(x = ball.canvas_width/2 - 75, y = ball.canvas_height/2-50)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

