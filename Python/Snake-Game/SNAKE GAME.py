import pygame
import random

# Initialize pygame
pygame.init()

# Screen size
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 20

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Game speed
clock = pygame.time.Clock()
FPS = 10

# Font for score
font = pygame.font.SysFont(None, 35)


# Show score on screen
def draw_score(score):
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))


# Main game function
def game():

    # Snake starting position
    snake = [(100, 100)]

    # Snake starting direction
    direction = "RIGHT"

    # Random food position
    food_x = random.randrange(0, WIDTH, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT, BLOCK_SIZE)

    # Initial score
    score = 0

    # Game loop
    running = True

    while running:

        # Check events
        for event in pygame.event.get():

            # Close window
            if event.type == pygame.QUIT:
                running = False

            # Keyboard controls
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"

                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"

                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"

                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        # Current head position
        head_x, head_y = snake[0]

        # Move snake
        if direction == "UP":
            head_y -= BLOCK_SIZE

        elif direction == "DOWN":
            head_y += BLOCK_SIZE

        elif direction == "LEFT":
            head_x -= BLOCK_SIZE

        elif direction == "RIGHT":
            head_x += BLOCK_SIZE

        # New head position
        new_head = (head_x, head_y)

        # Check wall collision
        if (
            head_x < 0
            or head_x >= WIDTH
            or head_y < 0
            or head_y >= HEIGHT
        ):
            break

        # Check self collision
        if new_head in snake:
            break

        # Add new head
        snake.insert(0, new_head)

        # Check food collision
        if head_x == food_x and head_y == food_y:

            score += 1

            # Generate new food
            food_x = random.randrange(0, WIDTH, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT, BLOCK_SIZE)

        else:
            # Remove last block
            snake.pop()

        # Fill background
        screen.fill(WHITE)

        # Draw food
        pygame.draw.rect(
            screen,
            RED,
            (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE)
        )

        # Draw snake
        for block in snake:
            pygame.draw.rect(
                screen,
                GREEN,
                (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE)
            )

        # Display score
        draw_score(score)

        # Update screen
        pygame.display.flip()

        # Control game speed
        clock.tick(FPS)

    # Exit pygame
    pygame.quit()


# Run the game
if __name__ == "__main__":
    game()
