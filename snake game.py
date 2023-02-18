import pygame
import random

# set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# set up the snake
snake_x = 100
snake_y = 100
snake_size = 10
snake_speed = 5
snake_direction = 'right'
snake_body = [(snake_x, snake_y)]

# set up the food
food_size = 10
food_x = random.randint(0, window_width - food_size)
food_y = random.randint(0, window_height - food_size)

# main game loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction != 'right':
                snake_direction = 'left'
            elif event.key == pygame.K_RIGHT and snake_direction != 'left':
                snake_direction = 'right'
            elif event.key == pygame.K_UP and snake_direction != 'down':
                snake_direction = 'up'
            elif event.key == pygame.K_DOWN and snake_direction != 'up':
                snake_direction = 'down'
                
    # update snake position
    if snake_direction == 'right':
        snake_x += snake_speed
    elif snake_direction == 'left':
        snake_x -= snake_speed
    elif snake_direction == 'up':
        snake_y -= snake_speed
    elif snake_direction == 'down':
        snake_y += snake_speed
        
    # check for collision with food
    if snake_x < food_x + food_size and snake_x + snake_size > food_x and snake_y < food_y + food_size and snake_y + snake_size > food_y:
        food_x = random.randint(0, window_width - food_size)
        food_y = random.randint(0, window_height - food_size)
        snake_body.append((snake_x, snake_y))
    
    # update the snake's body
    snake_body.insert(0, (snake_x, snake_y))
    if len(snake_body) > 1:
        snake_body.pop()
    
    # draw the snake and food
    window.fill(BLACK)
    for part in snake_body:
        pygame.draw.rect(window, WHITE, [part[0], part[1], snake_size, snake_size])
    pygame.draw.rect(window, RED, [food_x, food_y, food_size, food_size])
    
    # update the display
    pygame.display.update()
