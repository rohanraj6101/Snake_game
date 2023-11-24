# Snak_game
Description:
This Python script implements a simple Snake Game using the Pygame library. The game features a snake controlled by the player to eat food and grow longer. 
The objective is to avoid collisions with the game boundaries and the snake's own body.


* How to Play:
-Install the Pygame library using pip install pygame.
-Run the script.
-Use arrow keys to control the snake.
-Avoid collisions with the walls and the snake's body.
-Try to eat the white rectangles representing food to grow longer.
-The game ends if the snake collides with the walls or itself.

Detail_view
* Libraries Used:
pygame: Utilized for game development.
sys: Used for system-related functions.
random: Employed for generating random numbers.

* Initialization:
Pygame is initialized using pygame.init().

* Constants:
WIDTH and HEIGHT: Define the dimensions of the game window.
GRID_SIZE: Specifies the size of both the food and the snake.
GRID_WIDTH and GRID_HEIGHT: Calculate the number of grid cells based on the window dimensions.
FPS: Sets the frames per second for the game.

* Game Window Setup:
pygame.display.set_mode(): Creates a new game window.
pygame.display.set_caption(): Sets the window title.

* Snake and Food Initialization:
snake: Represents the snake's body as a list of coordinates.
snake_direction: Represents the snake's current direction using a vector.
food: Represents the initial position of the food.

* Main Game Loop:
The script enters a main game loop (while running:) that continues until the running variable is set to False.

* User Input Handling:
Arrow keys are used to change the snake's direction.
The snake cannot reverse its direction instantaneously to avoid self-collisions.

* Drawing on the Screen:
The screen is filled with a black color.
Snake segments are drawn as green rectangles, and the food is drawn as a white rectangle.
The pygame.display.update() function updates the display.

* Game Speed Control:
clock.tick(FPS): Controls the game speed by limiting the frames per second.

* Game Termination:
When the game loop ends, Pygame is quit using pygame.quit() and the program exits using sys.exit().



