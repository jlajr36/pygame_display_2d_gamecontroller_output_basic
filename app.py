import pygame

#start pygame
pygame.init()

#colors
background_color = (255, 255, 255)
text_color = (0, 0, 0)
line_color = (255, 0, 0)

#window setup
width = 640
height = 480
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('2D Controller Display')

#lines start pos
top = 0
left_side = 0
center_width = width/2
center_height = height/2

#setup position font
font_size = 18
bold = False
italicized = False
text_pos_1 = [500, 0]
text_pos_2 = [500, 20]
text_font = pygame.font.SysFont('Calibri', font_size, bold, italicized)

#main game loop
running = True
while running:
    #process game events
    for event in pygame.event.get():
        #Check for user exit
        if event.type == pygame.QUIT:
            running = False

    #draw screen background
    screen.fill(background_color)

    #display text position
    text_1 = text_font.render("test1", True, text_color)
    text_2 = text_font.render("test2", True, text_color)
    screen.blit(text_1, text_pos_1)
    screen.blit(text_2, text_pos_2)

    #draw lines
    pygame.draw.line(screen, line_color, (center_width, top), (center_width, height))
    pygame.draw.line(screen, line_color, (left_side, center_height), (width, center_height))

    #update display
    pygame.display.flip()

#exit pygame
pygame.quit()