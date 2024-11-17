import pygame
import math


pygame.init() # Ініціалізація pygame

pygame.display.set_caption('My game!') # Створення заголовку
screen = pygame.display.set_mode([1000, 600]) # Створення вікна

start_x = 500
start_y = 500
color = (255, 0, 0)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 255, 0)) # Зелений колір
    # screen.fill(128, 0, 128) # Фіолетовий колір
    # screen.fill(0, 0, 0) # Чорний колір

    x = start_x
    y = start_y
    angle = 0
    length = 1

    for i in range(200):
        end_x = x + length * math.cos(angle)
        end_y = y + length * math.sin(angle)
        pygame.draw.line(screen, color, (x, y), (end_x, end_y), 2)

        x = end_x
        y = end_y
        angle += math.pi / 20
        length +=1
    
    pygame.display.flip() # Оновлення екрану
    pygame.time.delay(50) #Зупиняє виконання програим на 50 мілісекунд
    
pygame.quit()