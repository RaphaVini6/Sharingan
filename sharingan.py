import turtle as t
import time

# Configuração da tela
t.tracer(0, 0)
screen = t.Screen()
t.title("GenJutsu")
t.bgcolor("white")

def draw_circle():
    t.penup()
    t.goto(0, -200)  # Posição do círculo grande
    t.pendown()
    t.shape('blank')
    t.color('black', 'red')
    t.width(4)
    t.begin_fill()
    t.circle(200)  # Desenha o círculo grande
    t.end_fill()
    t.penup()
    t.goto(0, -40)  # Posição do círculo pequeno
    t.pendown()
    t.color('black')
    t.begin_fill()
    t.circle(40)  # Desenha o círculo pequeno
    t.end_fill()
    t.penup()
    t.goto(0, 0)  # Volta ao centro
    t.pendown()
    t.color('black')
    t.width(1)

def draw_tomoe(angle, distance):
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(160)  # Ajusta a distância do centro
    t.pendown()
    t.color('black', 'black')
    t.begin_fill()
    t.circle(distance, 180)
    t.right(180)
    t.circle(-2 * distance, 180)
    t.circle(-distance, 180)
    t.end_fill()

def draw_mangekyou(angle_offset):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.color('black')
    t.width(4)
    t.begin_fill()
    for _ in range(3):
        t.circle(100, steps=3)
        t.right(120)
    t.end_fill()

def draw_sharingan(stage, angle_offset):
    draw_circle()
    if stage == 1:
        draw_tomoe(angle_offset, 10)  # 1 Tomoe
    elif stage == 2:
        draw_tomoe(angle_offset, 10)  # 2 Tomoes
        draw_tomoe(angle_offset + 180, 10)
    elif stage == 3:
        draw_tomoe(angle_offset, 10)  # 3 Tomoes
        draw_tomoe(angle_offset + 120, 10)
        draw_tomoe(angle_offset + 240, 10)
    elif stage == 4:
        draw_mangekyou(angle_offset)

def clear_screen():
    t.clear()

# Variáveis de controle de estágio e tempo
stage = 1
last_time = time.time()
angle_offset = 0

try:
    while True:
        clear_screen()
        draw_sharingan(stage, angle_offset)
        screen.update()
        time.sleep(0.01)

        angle_offset += 1  # Incrementa o ângulo para rotação

        # Verifica se é hora de evoluir o Sharingan
        if time.time() - last_time > 10:
            stage += 1
            if stage > 4:
                stage = 1  # Reseta para 1 tomoe após Mangekyou
            last_time = time.time()
except:
    print("Sharingan")
