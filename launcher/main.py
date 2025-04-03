import subprocess, pygame
from button import Button
pygame.init()

def get_font(size):
    return pygame.font.Font("assets/fonts/font.ttf", size)

play_image = pygame.image.load('assets/images/play_button.png')
settings_image = pygame.image.load('assets/images/settings_button.png')

#subprocess.run(["python", "../game/main.py"])

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('PyCraft Launcher')

running = True

pygame.mouse.set_cursor(pygame.cursors.broken_x)

while running:
    screen.fill((23, 21, 79))

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    play_button = Button(play_image, pos=(640, 500), font=get_font(75),text_input="Play",hovering_color=(64,64,64),base_color="BLACK")
    title = Button(None, pos=(640, 200), font=get_font(100), text_input="PyCraft", hovering_color='BLACK',base_color='BLACK')
    quit_button = Button(play_image, pos=(640, 650), font=get_font(75), text_input="Quit", hovering_color=(64, 64, 64),base_color="BLACK")

    for button in [play_button,quit_button,title]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.checkForInput(MENU_MOUSE_POS):
                subprocess.run(["python", "../game/main.py"])
            if quit_button.checkForInput(MENU_MOUSE_POS):
                running = False

    pygame.display.update()