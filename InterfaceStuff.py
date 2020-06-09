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


def pause_message(screen, resolution, colors):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('To Pause press P To Continue press C', True, colors["green"])
    text_rect = text.get_rect()
    text_rect.center = (resolution[0] // 2, resolution[1] // 2)
    screen.blit(text, text_rect)



def show_statistics(screen, colors):
    with open('data.json', 'r') as outfile:
        data = json.load(outfile)
        avg_v = data['avg_v'][len(data['avg_v']) - 1]
        avg_vmax = data['avg_vmax'][len(data['avg_vmax']) - 1]
        i = data['iteration'][len(data['iteration']) - 1]


    avg_v = round(avg_v,3)
    avg_vmax = round(avg_vmax, 3)

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('average speed '+str(avg_v), False, colors["green"])
    text_rect = text.get_rect()
    text_rect.center = (170, 50)
    pygame.draw.rect(screen, colors['black'], (0, 0, 450, 120))
    screen.blit(text, text_rect)
    text = font.render('average max speed '+str(avg_vmax), False, colors["green"])
    text_rect.center = (170, 100)
    screen.blit(text, text_rect)