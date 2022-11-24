import pygame

#start pygame
pygame.init()

#colors
background_color = (255, 255, 255)

#window setup
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('2D Controller Display')


#main game loop
running = True
while running:
    #process game events
    for event in pygame.event.get():
        #Check for user exit
        if event.type == pygame.QUIT:
            running = False

    #draw screen and elements
    screen.fill(background_color)

    #update display
    pygame.display.flip()

#exit pygame
pygame.quit()