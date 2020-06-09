import pygame
import json

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


    avg_v = round(avg_v, 3)
    avg_vmax = round(avg_vmax, 3)
    procent = round(procent, 3)

    avg_v = str(avg_v)
    avg_vmax = str(avg_vmax)
    i = str(i)
    procent = str(procent)
    num_cars = str(num_cars)

    if(len(avg_vmax) == 3):
        avg_vmax += '0'

    if(len(avg_v) == 3):
        avg_v += '0'

    if (len(procent) == 3):
        procent += '0'

    add_length1 = len(i)*20
    add_length2 = len(num_cars)*20


    pygame.draw.rect(screen, colors['black'], (270, 0, 100, 120))
    pygame.draw.rect(screen, colors['black'], (410, 680, 120, 50))
    pygame.draw.rect(screen, colors['black'], (160, 780, 20 + add_length1, 50))
    pygame.draw.rect(screen, colors['black'], (280, 720, 20 + add_length2, 50))

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(avg_v, True, colors["green"])
    text_rect = text.get_rect()
    text_rect.center = (320, 50)
    screen.blit(text, text_rect)

    text = font.render(avg_vmax, True, colors["green"])
    text_rect.center = (320, 100)
    screen.blit(text, text_rect)

    text = font.render(procent + '%', True, colors["green"])
    text_rect.center = (450, 700)
    screen.blit(text, text_rect)

    text = font.render(num_cars, True, colors["green"])
    text_rect.center = (320, 750)
    screen.blit(text, text_rect)

    text = font.render(i, True, colors["green"])
    text_rect.center = (200, 800)
    screen.blit(text, text_rect)