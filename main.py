import pygame
import pygame_gui

import objects

pygame.init()

screen_height : int = 800
screen_width : int = 600

screen = pygame.display.set_mode((screen_height, screen_width), pygame.FULLSCREEN)
pygame.display.set_caption("Skee-ball test")

clock = pygame.time.Clock()

manager = pygame_gui.UIManager((screen_height, screen_width))

count = 0 

header = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((300,100), (200,50)), 
    text=f"Count: {count}", 
    manager=manager
)

button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((300,200), (200,50)),
    text="Add Point",
    manager=manager
)

running : bool = True

while running:
    time_delta = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        manager.process_events(event)

        if event.type == pygame_gui.UI_BUTTON_PRESSED:

            if event.ui_element == button:
                count += 1
                header.set_text(f"Count: {count}")

    manager.update(time_delta)

    screen.fill("black")

    manager.draw_ui(screen)

    pygame.display.update()

pygame.quit()

