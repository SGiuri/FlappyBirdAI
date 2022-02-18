import pygame
from stuff.pipe import Pipes

pygame.init()


HEALTH_FONT = pygame.font.SysFont("Comicsans", 40)
END_FONT = pygame.font.SysFont("Comicsans", 50)

WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

FPS = 60

def draw_window():
    WIN.fill(WHITE)




    pygame.display.update()

####################################
def main():
    # Use a breakpoint in the code line below to debug your script.
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()
        draw_window()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
