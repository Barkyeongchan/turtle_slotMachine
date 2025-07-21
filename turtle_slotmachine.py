'''
목표: turtle을 활용하여 슬롯머신을 만들어본다.
'''
import turtle
import random
import threading
import time

# --- 터틀 세팅 ---
screen = turtle.Screen()

# --- 슬롯 그리기 함수 ---
def draw_slots():
    drawer = turtle.Turtle()
    drawer.hideturtle()
    drawer.speed(0)
    drawer.pensize(1)

    positions = [-200, 0, 200]
    radius = 100
    sector_colors = ["black", "red", "black", "red"]

    for x in positions:
        for i in range(4):
            angle = 90 * i
            drawer.penup()
            drawer.goto(x, 0)
            drawer.setheading(angle)
            drawer.fillcolor(sector_colors[i])
            drawer.begin_fill()
            drawer.forward(radius)
            drawer.left(90)
            drawer.circle(radius, 90)
            drawer.goto(x, 0)
            drawer.end_fill()

        drawer.penup()
        drawer.goto(x, -radius)
        drawer.setheading(0)
        drawer.pensize(3)
        drawer.pencolor("gold")
        drawer.pendown()
        drawer.circle(radius)

draw_slots()

slots = []
colors = ["red", "deepskyblue", "lime"]
positions = [-200, 0, 200]

for i in range(3):
    t = turtle.Turtle()
    t.shape("turtle")
    t.fillcolor(colors[i])
    t.pencolor("white")
    t.penup()
    t.goto(positions[i], -50)
    t.speed(0)
    slots.append(t)

def spin_turtle(turtle_obj, spin_count):
    for _ in range(spin_count):
        angle = random.choice([30, 45, 60, 90])
        turtle_obj.circle(50, angle)
        time.sleep(0.1)

def start_spin():
    threads = []
    for i in range(3):
        count = random.randint(20, 40)
        thread = threading.Thread(target=spin_turtle, args=(slots[i], count))
        threads.append(thread)
        thread.start()

# --- 엔터키 이벤트 핸들러 등록 ---
def on_enter_key():
    start_spin()

screen.listen()
screen.onkey(on_enter_key, "Return")  # Enter 키 이벤트 연결

print("터틀창에서 엔터키 누르면 슬롯이 돌기 시작합니다.")
turtle.done()
