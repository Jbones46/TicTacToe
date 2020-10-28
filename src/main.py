# import the pygame module, so you can use it
import pygame


# define a main function
def main():

    # initialize the pygame module
    pygame.init()

    # load and set the logo
    # logo = pygame.image.load("./assets/icon.png")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("Tic Tac Toe")

    # create a surface on screen
    screen = pygame.display.set_mode((480, 360))

    # paint the gameboard background on screen
    # image set up for unix environment

    bgd_image = pygame.image.load("../assets/gameboard_01.png")
    player_X = pygame.image.load("../assets/player_X.png")
    player_O = pygame.image.load("../assets/player_O.png")
    bgd_image = pygame.transform.scale(bgd_image, (480, 360))
    screen.fill((255, 255, 255))
    screen.blit(bgd_image, (0, 0))
    pygame.display.flip()

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # mouse click event
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x = int(pos[0]/160) * 160 + 35
                y = int(pos[1] /120) * 120 + 15

                print('x = ' + str(int(pos[0] / 160)) + ', y = ' + str(int(pos[1] / 120)))

                screen.blit(player_O, (x,y))
                pygame.display.flip()


            # only do something if the event is of type QUIT





            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
