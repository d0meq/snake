import pygame
import time
import random

pygame.init()

screen_width = 600
screen_height = 400

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Snake Game by Dominik')

blue = (0,0,255)
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,102)
green = (50,153,213)
orange = (255,154,0)

snake_block = 10
snake_speed= 10
snake_colors= [blue, red, white, black, yellow, green, orange]

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 15)

def settings():
    settings_over = False

    screen.fill(black)
    settings_message("2 - Blue 1 - Red", orange)
    pygame.display.update()

    while not settings_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    i = 0
                    gameLoop()
                if event.key == pygame.K_1:
                    i = 1
                    gameLoop()

def menu():
    menu_over = False

    screen.fill(black)
    continue_message("2 - change color 1 - Play 0 - Quit", orange)
    pygame.display.update()

    while not menu_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    settings()
                if event.key == pygame.K_1:
                    gameLoop()
                if event.key == pygame.K_0:
                    pygame.quit()
                    quit()
                

def score(score):
    value = score_font.render("Your score: "+ str(score), True, orange)
    screen.blit(value, [10,0])

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, orange, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [0.2*screen_width, 0.1*screen_height])

def continue_message(msg, color):
    c_mesg = font_style.render(msg, True, color)
    screen.blit(c_mesg, [0.2*screen_width, 0.1*screen_height])

def settings_message(msg, color):
    s_mesg = font_style.render(msg, True, color)
    screen.blit(s_mesg, [0.2*screen_width, 0.1*screen_height])

def gameLoop():
    over = False
    close = False

    x1 = screen_width/2
    y1 = screen_height/2

    x1_change = 0
    y1_change = 0

    snake_list = []
    Length_of_snake = 1
    
    foodX = round(random.randrange(0,screen_width - snake_block) / 10.0) * 10.0
    foodY = round(random.randrange(0,(screen_height - 50) - snake_block) / 10.0) * 10.0

    while not over:

        while close == True:
            screen.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", orange)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        over = True
                        close = False
                    if event.key == pygame.K_c:
                        menu()
                        gameLoop()

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        
        if x1 == screen_width or x1 == 0 or y1 == screen_height or y1 == 0:
            close = True 

        x1 += x1_change
        y1 += y1_change

        screen.fill(black)
        
        pygame.draw.rect(screen, orange, [foodX, foodY, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > Length_of_snake:
            del snake_list[0]
        
        for x in snake_list[:-1]:
            if x == snake_head:
                close = True

        snake(snake_block, snake_list)
        score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodX and y1 == foodY:
            foodX = round(random.randrange(0,screen_width - snake_block) / 10.0) * 10.0
            foodY = round(random.randrange(0,screen_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

menu()
gameLoop()