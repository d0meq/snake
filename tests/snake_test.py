import pygame
import time
import random

pygame.init()

# Snake settings
snake_size = 10

# Screen settings
screen_width = 300
screen_heigt = 300
screen = pygame.display.set_mode((screen_width,screen_heigt))
pygame.display.set_caption('Snake Game')

def message(input, positionX, positionY, size):
    font_style = pygame.font.SysFont("bahnschrift", size)
    msg = font_style.render(input, True, (255,255,255))
    screen.blit(msg, [positionX, positionY])    

# Classes of objects
class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.body = [(x, y)]

    def move(self, dx, dy):
        new_head = (self.body[0][0] + dx, self.body[0][1] + dy)
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])
        
class Food:
    def __init__(self, fx, fy, radius):
        self.fx = fx
        self.fy = fy
        self.radius = radius

def drawSnake(snake, food):
    screen.fill((0, 0, 0))  # Clear the screen before drawing
    pygame.draw.circle(screen, (255, 255, 255), (food.fx, food.fy), food.radius)  # Draw the food
    for segment in snake.body:
        pygame.draw.rect(screen, (255, 255, 255), (segment[0], segment[1], snake_size, snake_size))


def mainMenu():
    menu_over = False

    screen.fill((0,0,0))
    message("Press 1 to play a game !", 0.15*screen_width, 0.4*screen_heigt, 20)
    message("Press 2 to open settings !", 0.15*screen_width, 0.5*screen_heigt, 20)
    pygame.display.update()
    
    while not menu_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game()
                    menu_over = True
                elif event.key == pygame.K_2:
                    settings()
                    menu_over = True
                elif event.key == pygame.K_0:
                    pygame.quit()

def settings():
    settings_over = False
    
    screen.fill((0,0,0))
    message("Press 1 to chose red !", 0.15*screen_width, 0.4*screen_heigt, 20)
    message("Press 2 to chose blue !", 0.15*screen_width, 0.5*screen_heigt, 20)
    pygame.display.update()
    
    while not settings_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game()
                    settings_over = True
                elif event.key == pygame.K_2:
                    game()
                    settings_over = True

def game():
    score = 0
    game_over = False

    snake = Snake(screen_heigt / 2, screen_width / 2)
    dx, dy = 0, 0

    food = Food(random.randint(0, screen_width - 10), random.randint(0, screen_heigt - 10), 5)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    pygame.quit()
                elif event.key == pygame.K_LEFT:
                    dx, dy = -10, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = 10, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -10
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, 10

        snake.move(dx, dy)

        if snake.body[0][0] < 0 or snake.body[0][0] >= screen_width or snake.body[0][1] < 0 or snake.body[0][1] >= screen_heigt:
            pygame.quit()
            game_over = True
        
        # Adjust collision detection logic
        if abs(snake.body[0][0] - food.fx) < snake_size and abs(snake.body[0][1] - food.fy) < snake_size:
            snake.grow()
            food = Food(random.randint(0, screen_width - 10), random.randint(0, screen_heigt - 10), 5)
            score += 1
        
        drawSnake(snake, food)
        message("Your score: "+ str(score) , 0.05*screen_width, 0.05*screen_heigt, 15)
        pygame.display.update()
        time.sleep(0.1)
    pygame.quit()

mainMenu()
game()
