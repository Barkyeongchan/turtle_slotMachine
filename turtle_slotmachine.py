'''
목표: turtle을 활용하여 슬롯머신을 만들어본다.
'''
import turtle
import random
import threading
import time

# --- 터틀 세팅 ---
screen = turtle.Screen()

def draw_slots():
    drawer = turtle.Turtle()
    drawer.hideturtle()
    drawer.speed(0)
    drawer.penup()
    drawer.goto(-300, 0)
    drawer.pendown()
    drawer.goto(-105, 0)
    drawer.penup()
    drawer.goto(-95, 0)
    drawer.pendown()
    drawer.goto(95, 0)
    drawer.penup()
    drawer.goto(105, 0)
    drawer.pendown()
    drawer.goto(300, 0)
    for x in [-200, 0, 200]:
        drawer.penup()
        drawer.goto(x, 100)
        drawer.pendown()
        drawer.goto(x, -100)

draw_slots()

# --- 슬롯 거북이 3마리 ---
slots = []
colors = ["red", "blue", "green"]
positions = [-200, 0, 200]

for i in range(3):
    t = turtle.Turtle()
    t.shape("turtle")
    t.fillcolor(colors[i])
    t.penup()
    t.goto(positions[i], -50)
    t.speed(0)
    slots.append(t)

# --- 거북이 개별 회전 쓰레드 ---
def spin_turtle(turtle_obj, spin_count):
    for _ in range(spin_count):
        angle = random.choice([30, 45, 60, 90])
        turtle_obj.circle(50, angle)
        time.sleep(0.1) 

def start_spin():
    threads = []
    for i in range(3):
        count = random.randint(30, 60)
        thread = threading.Thread(target=spin_turtle, args=(slots[i], count))
        threads.append(thread)
        thread.start()

print("엔터를 누르세요")
input()
start_spin()
turtle.done()