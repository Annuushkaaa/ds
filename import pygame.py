import pygame
import sys
pygame.init()
WIDTH,HEIGHT=800,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("DDA line algorithm")
WHITE=(255,255,255)
BLACK=(0,0,0)

def draw(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    steps=max(abs(dx),abs(dy))
    x_inc=dx/steps
    y_inc=dy/steps
    x=x1
    y=y1
    for i in range(steps):
        screen.set_at((round(x), round(y)), WHITE)
        x+=x_inc
        y+=y_inc

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Draw a line using DDA algorithm
        draw(20,20 , 100, 100)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
    
