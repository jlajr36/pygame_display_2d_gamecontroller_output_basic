import pygame

#start pygame
pygame.init()

#start clock
clock_ticks = 20
clock = pygame.time.Clock()

#start controller
ad_counts = 1024
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
controller = joysticks[0]

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

    #get controller x/y position
    axis0 = controller.get_axis(0)
    axis1 = controller.get_axis(1)
    axis0_value = int(axis0*ad_counts)
    axis1_value = int(axis1*ad_counts) 

    #format axis for display
    str_axis0 = "Axis 0:" + str(axis0_value)
    str_axis1 = "Axis 1:" + str(axis1_value)

    #draw screen background
    screen.fill(background_color)

    #display text position
    text_1 = text_font.render(str_axis0, True, text_color)
    text_2 = text_font.render(str_axis1, True, text_color)
    screen.blit(text_1, text_pos_1)
    screen.blit(text_2, text_pos_2)

    #draw lines
    pygame.draw.line(screen, line_color, (center_width+axis0_value, top), (center_width+axis0_value, height))
    pygame.draw.line(screen, line_color, (left_side, center_height+axis1_value), (width, center_height+axis1_value))

    #update display
    pygame.display.flip()

    #Limit to 20 fps
    clock.tick(clock_ticks)

#exit pygame
pygame.quit()