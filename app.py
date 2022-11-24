import pygame

#window setup
background_color = (255, 255, 255)
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('2D Controller Display')
screen.fill(background_color)
pygame.display.flip()

#main game loop
running = True
while running:
    #process game events
    for event in pygame.event.get():
        #Check for user exit
        if event.type == pygame.QUIT:
            running = False