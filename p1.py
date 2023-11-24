import pygame   #used for game development
import sys      # system related function
import random   #generating random numbers

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20  #size of food and snake  
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS =10    #frame per second

# Colors
BLACK = (0, 0, 0)
WHITE = (100, 100, 100)  #used to increse or decrease brightness
GREEN = (0, 100, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))  #to create new game window
pygame.display.set_caption("Snake Game")  #windows title

# initialise Snake
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = (1, 0)  #by using vector graph

#initialise Food
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Main game loop
running = True  #We set up a main game loop that will continue until the running variable is set to False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get(): #retrive the information from given server
        if event.type == pygame.QUIT:
            running = False  # If the user closes the window or quit the game

    keys = pygame.key.get_pressed() #user input  can change snake direction usig arrow keys 
    if keys[pygame.K_UP] and snake_direction != (0, 1):
        snake_direction = (0, -1)
    elif keys[pygame.K_DOWN] and snake_direction != (0, -1):
        snake_direction = (0, 1)
    elif keys[pygame.K_LEFT] and snake_direction != (1, 0):
        snake_direction = (-1, 0)
    elif keys[pygame.K_RIGHT] and snake_direction != (-1, 0):
        snake_direction = (1, 0)

    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, new_head)  #We insert the new head at the front of the snake list.

    if (
        new_head[0] < 0
        or new_head[0] >= GRID_WIDTH
        or new_head[1] < 0
        or new_head[1] >= GRID_HEIGHT
        or new_head in snake[1:]
    ):
        running = False  #We check for collisions: if the snake hits the wall or itself, the game ends.

    if new_head == food:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop() # If the snake's head reaches the food, it eats it and a new food is placed randomly.
               #If the snake doesn't eat, we remove the last element from the snake's body to simulate movement.
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)) #snake segments as green rectangles 
    pygame.draw.rect(screen, WHITE, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)) #food segment as white circle
    pygame.display.update()
    clock.tick(FPS)     # to control the game spped

# Quit Pygame
pygame.quit()
sys.exit()  #Finally, when the game loop ends, we quit the Pygame library and exit the program.