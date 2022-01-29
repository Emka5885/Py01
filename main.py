#Jest to projekt Snake Game z kursu 02, kursiku 101, jednak trochę przerobiony i z samouczkiem ^^

from tkinter import *
import random
import time

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100   #Im mniejsza liczba, tym szybsza gra
SPACE_SIZE = 50   #Ustawiamy jak duże mają być nasze części gry (jedzenie, części węża)
BODY_PARTS = 3   #Tłumaczenie - (parts) "części";   #Ustawiamy ile części ciała ma nasz wąż, gdy zaczynamy grę
snake_color = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append(([0, 0]))

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=snake_color, tag="snake")
            self.squares.append(square)

class Food:

    def __init__(self):

        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE   #".randint(początek, koniec)" - zwraca losową liczbę całkowitą pomiędzy dwoma dolnymi i górnymi limitami (w tym obydwoma limitami) podanymi jako dwa parametry
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):   #Tłumaczenie - (next_turn) "następny ruch"

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    if x < 0:
        x = GAME_WIDTH
    elif x >= GAME_WIDTH:
        x = 0
    elif y < 0:
        y = GAME_HEIGHT
    elif y >= GAME_HEIGHT:
        y = 0

    snake.coordinates.insert(0, (x, y))   #Tłumaczenie - (insert) "wstawić"

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=snake_color)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:   #Jeśli nie zjedliśmy obiektu "food", to usuniemy ostatnią część węża
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 and x >= GAME_WIDTH:
        return False
    elif y < 0 and y >= GAME_HEIGHT:
        return False

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")

    button.config(fg='black', activeforeground="black", command=new_game)

def new_game():

    try:

        canvas.delete(ALL)
        button.config(fg='#F0F0F0', activeforeground="#F0F0F0", command=nothing)

        global snake
        global food
        global score
        global direction

        del snake
        del food

        score = 0
        direction = 'down'

        label.config(text="Score:{}".format(score))

        window.update()

        snake = Snake()
        food = Food()

        next_turn(snake,food)

    except NameError:
        canvas.delete(ALL)
        button.config(fg='#F0F0F0', activeforeground="#F0F0F0", command=nothing)

        label.config(text="Score:{}".format(score))

        window.update()

        snake = Snake()
        food = Food()

        next_turn(snake, food)

def nothing():
    pass


def Help():

    def next():

        global text

        text = 1

        while True:

            if text == 1:
                text = 0

                canvas1.delete('arrow1')
                canvas1.delete('arrow2')
                canvas1.delete('arrow3')
                canvas1.create_line(150, 150, 150, 300, fill='white', width=5, tag='arrow1')
                canvas1.create_line(125, 300, 150, 325, fill='white', width=5, tag='arrow2')
                canvas1.create_line(175, 300, 150, 325, fill='white', width=5, tag='arrow3')
                canvas.update()
                time.sleep(1)

            elif text == 0:
                text = 1

                canvas1.delete('arrow1')
                canvas1.delete('arrow2')
                canvas1.delete('arrow3')
                canvas1.create_line(150, 200, 150, 350, fill='white', width=5, tag='arrow1')
                canvas1.create_line(125, 350, 150, 375, fill='white', width=5, tag='arrow2')
                canvas1.create_line(175, 350, 150, 375, fill='white', width=5, tag='arrow3')
                canvas.update()
                time.sleep(1)
            else:
                break

    def next1():

        def next2():

            def next3():

                def next4():

                    def close():
                        canvas.delete(ALL)
                        new_window.destroy()

                    next4.destroy()

                    next5 = Button(new_window, text='Close', font=('consolas', 10), command=close)
                    next5.pack(side='right')

                    try:
                        global text

                        text = 10
                        score2 = 0
                        score3 = 1

                        canvas1.delete('left')
                        canvas1.create_text(250, 450, fill='white', font=('consolas', 15),
                                            text='To score points and feed the snake\nyou have to move its head on the food', tag='left')

                        canvas1.delete('snakea1')
                        canvas1.delete('snakea2')
                        canvas1.delete('snakea3')
                        canvas1.create_rectangle(300, 250, 0 + 250, 0 + 200, fill=snake_color, tag='snakea1')
                        canvas1.create_rectangle(350, 250, 0 + 250, 0 + 200, fill=snake_color, tag='snakea2')
                        canvas1.create_rectangle(400, 250, 0 + 250, 0 + 200, fill=snake_color, tag='snakea3')

                        canvas1.delete('food')
                        canvas1.create_oval(200, 250, 0 + 150, 0 + 200, fill=FOOD_COLOR, tag='food')

                        canvas1.delete('arrow4')
                        canvas1.delete('arrow5')
                        canvas1.delete('arrow6')

                        while True:

                            if text == 10:
                                text = 9

                                label.config(text="Score:{}".format(score2))
                                canvas1.create_oval(200, 250, 0 + 150, 0 + 200, fill=FOOD_COLOR, tag='food')
                                canvas1.delete('snakea1')
                                canvas1.delete('snakea2')
                                canvas1.delete('snakea3')
                                canvas1.delete('snakea4')
                                canvas1.create_rectangle(300, 250, 0 + 250, 0 + 200, fill=snake_color, tag='snakea1')
                                canvas1.create_rectangle(350, 250, 0 + 250, 0 + 200, fill=snake_color, tag='snakea2')
                                canvas1.create_rectangle(400, 250, 0 + 250, 0 + 200, fill=snake_color, tag='snakea3')
                                canvas.update()
                                time.sleep(1)

                            elif text == 9:
                                text = 8

                                canvas1.delete('snakea1')
                                canvas1.delete('snakea2')
                                canvas1.delete('snakea3')
                                canvas1.create_rectangle(250, 250, 0 + 200, 0 + 200, fill=snake_color, tag='snakea1')
                                canvas1.create_rectangle(300, 250, 0 + 200, 0 + 200, fill=snake_color, tag='snakea2')
                                canvas1.create_rectangle(350, 250, 0 + 200, 0 + 200, fill=snake_color, tag='snakea3')
                                canvas.update()
                                time.sleep(1)

                            elif text == 8:
                                text = 10

                                label.config(text="Score:{}".format(score3))
                                canvas1.delete('snakea1')
                                canvas1.delete('snakea2')
                                canvas1.delete('snakea3')
                                canvas1.create_rectangle(200, 250, 0 + 150, 0 + 200, fill=snake_color, tag='snakea1')
                                canvas1.create_rectangle(250, 250, 0 + 150, 0 + 200, fill=snake_color, tag='snakea2')
                                canvas1.create_rectangle(300, 250, 0 + 150, 0 + 200, fill=snake_color, tag='snakea3')
                                canvas1.create_rectangle(350, 250, 0 + 150, 0 + 200, fill=snake_color, tag='snakea4')
                                canvas1.delete('food')
                                canvas.update()
                                time.sleep(1)
                            else:
                                break
                    except:
                        pass


                next3.destroy()

                next4 = Button(new_window, text='Next', font=('consolas', 10), command=next4)
                next4.pack(side='right')

                try:
                    global text

                    text = 7

                    canvas1.delete('right')
                    canvas1.create_text(250, 450, fill='white', font=('consolas', 15),
                                        text='To move the snake down press <a> or <Left>.', tag='left')

                    canvas1.delete('snake7')
                    canvas1.delete('snake8')
                    canvas1.delete('snake9')

                    canvas1.create_rectangle(300, 250, 0 + 250, 0 + 200, fill=snake_color, tag='snakea1')
                    canvas1.create_rectangle(350, 250, 0 + 250, 0 + 200, fill=snake_color, tag='snakea2')
                    canvas1.create_rectangle(400, 250, 0 + 250, 0 + 200, fill=snake_color, tag='snakea3')

                    while True:

                        if text == 6:
                            text = 7

                            canvas1.delete('arrow4')
                            canvas1.delete('arrow5')
                            canvas1.delete('arrow6')
                            canvas1.create_line(150, 150, 300, 150, fill='white', width=5, tag='arrow4')
                            canvas1.create_line(125, 150, 150, 125, fill='white', width=5, tag='arrow5')
                            canvas1.create_line(125, 150, 150, 175, fill='white', width=5, tag='arrow6')
                            canvas.update()
                            time.sleep(1)

                        elif text == 7:
                            text = 6

                            canvas1.delete('arrow4')
                            canvas1.delete('arrow5')
                            canvas1.delete('arrow6')
                            canvas1.create_line(200, 150, 350, 150, fill='white', width=5, tag='arrow4')
                            canvas1.create_line(175, 150, 200, 125, fill='white', width=5, tag='arrow5')
                            canvas1.create_line(175, 150, 200, 175, fill='white', width=5, tag='arrow6')
                            canvas.update()
                            time.sleep(1)
                        else:
                            break
                except:
                    pass


            next2.destroy()

            next3 = Button(new_window, text='Next', font=('consolas', 10), command=next3)
            next3.pack(side='right')

            try:
                global text

                text = 4

                canvas1.delete('up')
                canvas1.create_text(250, 450, fill='white', font=('consolas', 15),
                                    text='To move the snake down press <d> or <Right>.', tag='right')

                canvas1.delete('snake4')
                canvas1.delete('snake5')
                canvas1.delete('snake6')

                canvas1.create_rectangle(100, 250, 0 + 50, 0 + 200, fill=snake_color, tag='snake7')
                canvas1.create_rectangle(150, 250, 0 + 50, 0 + 200, fill=snake_color, tag='snake8')
                canvas1.create_rectangle(200, 250, 0 + 50, 0 + 200, fill=snake_color, tag='snake9')

                canvas1.delete('arrow1')
                canvas1.delete('arrow2')
                canvas1.delete('arrow3')

                canvas1.create_line(150, 150, 300, 150, fill='white', width=5, tag='arrow4')
                canvas1.create_line(325, 150, 300, 125, fill='white', width=5, tag='arrow5')
                canvas1.create_line(325, 150, 300, 175, fill='white', width=5, tag='arrow6')
                canvas.update()

                while True:

                    if text == 4:
                        text = 5

                        canvas1.delete('arrow4')
                        canvas1.delete('arrow5')
                        canvas1.delete('arrow6')
                        canvas1.create_line(150, 150, 300, 150, fill='white', width=5, tag='arrow4')
                        canvas1.create_line(325, 150, 300, 125, fill='white', width=5, tag='arrow5')
                        canvas1.create_line(325, 150, 300, 175, fill='white', width=5, tag='arrow6')
                        canvas.update()
                        time.sleep(1)

                    elif text == 5:
                        text = 4

                        canvas1.delete('arrow4')
                        canvas1.delete('arrow5')
                        canvas1.delete('arrow6')
                        canvas1.create_line(200, 150, 350, 150, fill='white', width=5, tag='arrow4')
                        canvas1.create_line(375, 150, 350, 125, fill='white', width=5, tag='arrow5')
                        canvas1.create_line(375, 150, 350, 175, fill='white', width=5, tag='arrow6')
                        canvas.update()
                        time.sleep(1)
                    else:
                        break
            except:
                pass


        next1.destroy()

        next2 = Button(new_window, text='Next', font=('consolas', 10), command=next2)
        next2.pack(side='right')

        try:
            global text

            text = 2

            canvas1.delete('down')
            canvas1.create_text(250, 450, fill='white', font=('consolas', 15), text='To move the snake down press <w> or <Up>.', tag='up')

            canvas1.delete('snake1')
            canvas1.delete('snake2')
            canvas1.delete('snake3')

            canvas1.create_rectangle(100, 300, 0 + 50, 0 + 250, fill=snake_color, tag='snake4')
            canvas1.create_rectangle(100, 350, 0 + 50, 0 + 250, fill=snake_color, tag='snake5')
            canvas1.create_rectangle(100, 400, 0 + 50, 0 + 250, fill=snake_color, tag='snake6')

            while True:

                if text == 2:
                    text = 3

                    canvas1.delete('arrow1')
                    canvas1.delete('arrow2')
                    canvas1.delete('arrow3')
                    canvas1.create_line(150, 150, 150, 300, fill='white', width=5, tag='arrow1')
                    canvas1.create_line(125, 150, 150, 125, fill='white', width=5, tag='arrow2')
                    canvas1.create_line(175, 150, 150, 125, fill='white', width=5, tag='arrow3')
                    canvas.update()
                    time.sleep(1)

                elif text == 3:
                    text = 2

                    canvas1.delete('arrow1')
                    canvas1.delete('arrow2')
                    canvas1.delete('arrow3')
                    canvas1.create_line(150, 100, 150, 250, fill='white', width=5, tag='arrow1')
                    canvas1.create_line(125, 100, 150, 75, fill='white', width=5, tag='arrow2')
                    canvas1.create_line(175, 100, 150, 75, fill='white', width=5, tag='arrow3')
                    canvas.update()
                    time.sleep(1)
                else:
                    break
        except:
            pass



    try:
        new_window = Toplevel()

        new_window.title("Snake game help")
        new_window.resizable(False, False)

        score1 = 0

        frame1 = Frame(new_window)
        frame1.pack()

        label1 = Label(frame1, text='', font=('consolas', 30))
        label1.grid(row=0, column=0)

        label2 = Label(frame1, width=25)
        label2.grid(row=0, column=1)

        label = Label(frame1, text="Score:{}".format(score1), font=('consolas', 30))
        label.grid(row=0, column=2)

        canvas1 = Canvas(new_window, bg='#161717', height=500, width=500)
        canvas1.pack()

        canvas1.create_rectangle(100, 100, 0+50, 0+50, fill=snake_color, tag='snake1')
        canvas1.create_rectangle(100, 150, 0 + 50, 0 + 50, fill=snake_color, tag='snake2')
        canvas1.create_rectangle(100, 200, 0 + 50, 0 + 50, fill=snake_color, tag='snake3')

        canvas1.create_line(150, 150, 150, 300, fill='white', width=5, tag='arrow1')
        canvas1.create_line(125, 300, 150, 325, fill='white', width=5, tag='arrow2')
        canvas1.create_line(175, 300, 150, 325, fill='white', width=5, tag='arrow3')

        canvas1.create_text(250, 450, fill='white', font=('consolas', 15), text='To move the snake down press <s> or <Down>.', tag='down')

        canvas1.create_oval(400, 400, 0 + 350, 0 + 350, fill=FOOD_COLOR, tag='food')

        canvas.update()

        next1 = Button(new_window, text='Next', font=('consolas', 10), command=next1)
        next1.pack(side='right')

        new_window.update()

        new_window_width = new_window.winfo_width()
        new_window_height = new_window.winfo_height()
        screen_width = new_window.winfo_screenwidth()
        screen_height = new_window.winfo_screenheight()

        x = int((screen_width / 2) - (new_window_width / 2))
        y = int((screen_height / 2) - (new_window_height / 2))

        new_window.geometry(f"{new_window_width}x{new_window_height}+{x}+{y}")

        next()

    except:
        pass


window = Tk()
window.title("Snake game")
icon = PhotoImage(file='C:\\Users\\Emi\\Desktop\\Programowanie\\Python\\obrazki\\snake.png')
window.iconphoto(True,icon)
window.resizable(False, False)   #Tłumaczenie - (resizable) "możliwość zmiany rozmiaru";   #Wyłączymy możliwość zmiany rozmiaru naszego okna

score = 0
direction = 'down'

frame = Frame(window, bg='#F0F0F0')
frame.pack()

button = Button(frame, text='New game', fg='black', bg='#F0F0F0',activeforeground="black", font=('consolas', 20), command=new_game)
button.grid(row=0, column=0)

label1 = Label(frame, width=25)
label1.grid(row=0, column=1)

label = Label(frame, text="Score:{}".format(score), font=('consolas', 40))
label.grid(row=0, column=2)

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<a>', lambda event: change_direction('left'))
window.bind('<d>', lambda event: change_direction('right'))
window.bind('<w>', lambda event: change_direction('up'))
window.bind('<s>', lambda event: change_direction('down'))

Help()

window.mainloop()