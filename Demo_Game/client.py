import pygame
from pygame import color

# Global variables
width = 500
height = 500
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

ClientNumber = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed() # this gives us all the key dictionaries where every key has a value

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)



def redrawWindow(win, player):
    win.fill(WHITE)
    player.draw(win)
    pygame.display.update()



def main():  # the main loop is continues constantly checking the server for events
    p = Player(50, 50, 100, 100, GREEN)
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p)


main()