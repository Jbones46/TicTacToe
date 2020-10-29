# import the pygame module, so you can use it
import pygame
import gamestate


# bad boy global variables
game_state = gamestate.Gamestate()


def drawXY(screen, player):
    pos = pygame.mouse.get_pos()
    x = int(pos[0]/160)
    y = int(pos[1] /120)
    x_pixel = x * 160 + 35
    y_pixel = y * 120 + 15
    # Debug print statement
    # print('x = ' + str(x) + ', y = ' + str(y))
    if game_state.check_and_update_board(x, y) == True:
        screen.blit(player, (x_pixel, y_pixel))
        pygame.display.flip()
        if game_state.check_win_condition(x, y) == True:
            # do stuff to indicate who won!
            print('TODO: add victory logic here')
        print()
        game_state.print_game_board()
        print('\nkey: ' + str(game_state.key))

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
    bgd_image = pygame.transform.scale(bgd_image, (480, 360))
    player_X = pygame.image.load("../assets/player_X.png")
    player_O = pygame.image.load("../assets/player_O.png")
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
                if game_state.player_Xs_turn == True:
                    drawXY(screen, player_X)
                    game_state.player_Xs_turn = False
                else:
                    drawXY(screen, player_O)
                    game_state.player_Xs_turn = True
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
