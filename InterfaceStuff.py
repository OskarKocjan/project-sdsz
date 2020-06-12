import pygame
import json
from datetime import datetime


def pause(clock):

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(5)


def message(screen, resolution, colors, text):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(text, True, colors["green"])
    text_rect = text.get_rect()
    text_rect.center = resolution
    screen.blit(text, text_rect)



def show_statistics(screen, colors):
    with open('data.json', 'r') as outfile:
        data = json.load(outfile)
        avg_v = data['avg_v'][len(data['avg_v']) - 1]
        avg_vmax = data['avg_vmax'][len(data['avg_vmax']) - 1]
        i = data['iteration'][len(data['iteration']) - 1]
        procent = data['diffrence_v_vmax'][len(data['diffrence_v_vmax']) - 1]
        num_cars = data['number_of_cars'][len(data['number_of_cars']) - 1]
        time = data['time'][len(data['time']) - 1]


    avg_v = round(avg_v, 2)
    avg_vmax = round(avg_vmax, 2)
    procent = round(procent, 2)
    time = int(time)

    avg_v = str(avg_v)
    avg_vmax = str(avg_vmax)
    i = str(i)
    procent = str(procent)
    num_cars = str(num_cars)
    time = datetime.fromtimestamp(time - 3600).strftime("%H:%M:%S")

    add_length1 = len(i)*25



    pygame.draw.rect(screen, colors['black'], (270, 0, 135, 120))
    pygame.draw.rect(screen, colors['black'], (380, 680, 220, 50))
    pygame.draw.rect(screen, colors['black'], (150, 780, 50 + add_length1, 50))
    pygame.draw.rect(screen, colors['black'], (270, 720, 200, 50))
    pygame.draw.rect(screen, colors['black'], (95, 820, 300, 50))

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(avg_v, True, colors["green"])
    text_rect = text.get_rect()
    text_rect.center = (335, 50)
    screen.blit(text, text_rect)

    text = font.render(avg_vmax, True, colors["green"])
    text_rect.center = (335, 100)
    screen.blit(text, text_rect)

    text = font.render(procent + '%', True, colors["green"])
    text_rect.center = (450, 700)
    screen.blit(text, text_rect)

    text = font.render(num_cars, True, colors["green"])
    text_rect.center = (350, 750)
    screen.blit(text, text_rect)

    text = font.render(i, True, colors["green"])
    text_rect.center = (220, 800)
    screen.blit(text, text_rect)

    text = font.render(time, True, colors["green"])
    text_rect.center = (170, 850)
    screen.blit(text, text_rect)



