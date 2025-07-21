'''
# 개인 프로젝트
# turtle을 활용한 슬롯머신 만들기

import turtle
import random

# 줄(배경) 생성
line_maker = turtle.Turtle()
line_maker.penup()
line_maker.goto(-300, 0)
line_maker.pendown()
line_maker.goto(-105, 0)

line_maker.penup()
line_maker.goto(-95, 0)
line_maker.pendown()
line_maker.goto(95, 0)

line_maker.penup()
line_maker.goto(105, 0)
line_maker.pendown()
line_maker.goto(300, 0)

line_maker.penup()
line_maker.goto(-200, 100)
line_maker.pendown()
line_maker.goto(-200, -100)

line_maker.penup()
line_maker.goto(0, 100)
line_maker.pendown()
line_maker.goto(0, -100)

line_maker.penup()
line_maker.goto(200, 100)
line_maker.pendown()
line_maker.goto(200, -100)

# 1번 슬롯
position_one = line_maker.clone()
position_one.shape("turtle")
position_one.fillcolor("red")
position_one.penup()
position_one.goto(-200, -50)

# 2번 슬롯
position_two = position_one.clone()
position_two.shape("turtle")
position_two.fillcolor("blue")
position_two.penup()
position_two.goto(0, -50)

# 3번 슬롯
position_three = position_two.clone()
position_three.shape("turtle")
position_three.fillcolor("green")
position_three.penup()
position_three.goto(200, -50)
'''
#--------------------------------------------------------------------------
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


# screen.listen()            # ← 삭제됨
# screen.onkey(start_spin, "Return")  # ← 삭제됨

print("엔터를 누르세요")

input() # 터미널에서 엔터 입력 받기위해 추가함, 원래는 없었음

start_spin()  # ← 추가됨: 직접 함수 호출로 회전 시작 (이전엔 키 입력 대기 방식)

turtle.done()