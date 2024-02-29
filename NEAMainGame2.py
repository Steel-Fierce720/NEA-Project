import pygame
import random
import time

#ISSUES WITH GAME CURRENTLY
#Collision ceases to function when snake speed is set to anything higher than 10 - ISSUE FIXED - Movement per frame, snake cube dimensions and the dimensions have to be the same for the collision to function 
#Cubes that make up the body of the snake become more and more seperated the higher the speed of the snake

def run_game(choice): 
    #getting the player to select a difficulty
    #choice = choose_difficulty()
    
    #setting the speed and score multiplier based on the difficulty chosen
    #the speed set (snake_speed) adjusts the refresh rate which in turn adjusts the speed of the snake by having more fps and therefor more movements per seccond
    if choice == 1:
        snake_speed = 1
        score_multiplier = 0.5
        print("speed has been adjusted")
    if choice == 2: 
        snake_speed = 1.5
        score_multiplier = 1
        print("speed has been adjusted")
    if choice == 3:
        snake_speed = 2
        score_multiplier = 1.5
        print("speed has been adjusted")
    if choice == 4: 
        snake_speed = 3
        score_multiplier = 2
        print("speed has been adjusted")

    #adjusting the size of the window 
    window_x = 1400
    window_y = 830

    #setting up the colours to be used in the game
    black = pygame.Color(0,0,0)
    white = pygame.Color(255,255,255)
    red = pygame.Color(255,0,0)
    green = pygame.Color(0,255,0)
    dark_green = pygame.Color(1,50,32)

    #initialising pygame
    pygame.init()

    #creating the game window
    pygame.display.set_caption('Snake')
    game_window = pygame.display.set_mode((window_x, window_y))

    #setting the background image for the game
    image = pygame.image.load('grass_background.jpeg')

    #setting up the fps
    fps = pygame.time.Clock()

    #setting up the snakes default position
    snake_pos = [100,50]

    #creating the four blocks of the snakes body
    snake_body = [[100,50], [90,50], [80,50], [70,50]]

    #setting the score objects position
    score_object_pos = [random.randrange(1, (window_x//10)) *10, random.randrange(1, (window_y//10)) *10]
    score_object_spawn = True

    #defining the snakes default starting direction
    direction = 'RIGHT'
    change_to = direction

    #initialising the score
    score = 0

    #creating a function to display the score
    def show_score(choice, color, font, size):
        #creating a font for the score
        score_font = pygame.font.SysFont(font,size)

        #creating the surface to display the score on
        score_surface = score_font.render('Score : ' +str(score), True, color)

        #creating a rectangular object for the score surface to sit on
        score_rect =  score_surface.get_rect()

        #displaying the text
        game_window.blit(score_surface, score_rect)

    #creating a function to handle a game over state
    def game_over():
        #creating an object called my_font
        my_font = pygame.font.SysFont('times new roman', 50)

        #creating a surface on which the text will be displayed
        game_over_surface = my_font.render('Your score is: ' + str(score), True, red)

        #creating a rectangle object for the text to sit on
        game_over_rect = game_over_surface.get_rect()

        #defining the position of the text
        game_over_rect.midtop = (window_x/ 2, window_y/4)

        #using blit to draw the text
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()

        #closes the game after 2 secconds
        time.sleep(2)

        #deactivating pygame library
        pygame.quit()

        #quitting the program
        quit()

    #main loop of the game
    while True:
        #checks for key presses and changes the direction of the snake accordingly
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
        
        #makes sure that the snake cannot recive two opposite directions at once
        if change_to == 'UP' and direction !='DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction !='UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction !='RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction !='LEFT':
            direction = 'RIGHT'
        
        #Snake movement
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10
        
        #snake size increase mechanism
        #collision with a score object will increase the length of the snake by 10
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == score_object_pos[0] and snake_pos[1] == score_object_pos[1]:
            score += (1 * score_multiplier)
            score_object_spawn = False
        else:
            snake_body.pop()
        
        if not score_object_spawn:
            score_object_pos = [random.randrange(1, (window_x//10)) *10, random.randrange(1, (window_y//10)) *10]
        
        score_object_spawn = True

        #adding the background image to the game
        game_window.blit(image, (0,0))

        #draws a rectangle for each position in  the snakes body
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        
        pygame.draw.rect(game_window, white, pygame.Rect(score_object_pos[0], score_object_pos[1], 10, 10))

        #conditions for a game over state to activate
        if snake_pos[0] < 0 or snake_pos[0] > window_x - 10:
            game_over()
        if snake_pos[1] < 0 or snake_pos[1] > window_y - 10:
            game_over()
        
        #detecting if the snake head touched the body
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over()
        
        #having the score always be up on the screen
        show_score(1, white, 'times new roman', 40)

        #refreshing the screen
        pygame.display.update()

        #setting up the refresh rate (dependant on the speed of the snake)
        fps.tick((snake_speed*10))