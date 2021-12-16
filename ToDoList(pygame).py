import pygame

pygame.init()

Xval, Yval = 640, 480
screen = pygame.display.set_mode((Xval, Yval))

#  Text
font = pygame.font.SysFont("verdana", 36)


def main():
    #  Game vars
    CLOCK = pygame.time.Clock()
    FPS = 60
    RUN = True

    #  Colours
    Black = (0, 0, 0)
    White = (255, 255, 255)
    Red = (255, 0, 0)
    Green = (0, 255, 0)
    Blue = (0, 0, 255)

    #  Inputbox
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    Itext = ''

    #  Header
    Headerfont = pygame.font.SysFont("verdana", 48)
    HeaderSent = 'TO DO LIST'
    HeaderText = Headerfont.render(HeaderSent, True, Red)
    HeaderRect = HeaderText.get_rect(center=(Xval / 2, 20))
    

    while RUN:
        #  Catch game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                #  if the user clicked in the input rect.
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False

                #  Change the current color of the input box.
                color = color_active if active else color_inactive

            if event.type == pygame.KEYDOWN:
                #  active is represented as a colour change
                if active:
                    if event.key == pygame.K_RETURN:
                        Itext = ''
                    elif event.key == pygame.K_BACKSPACE:
                        Itext = Itext[:-1]
                    else:
                        Itext += event.unicode

        #  Inputbox rect

    	#  Render the current text.
        #  txt_surface = font.render(Itext, True, color)

        #  Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width


        #  PLace obj on sceen surface
        screen.fill(Black)
        screen.blit(HeaderText, HeaderRect)

        #  Inputbox rect

        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        #  update
        pygame.display.flip()
        CLOCK.tick(FPS)

if __name__ == "__main__":
    main()
