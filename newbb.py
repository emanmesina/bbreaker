import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window dimensions
WIDTH = 800
HEIGHT = 600

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window
pygame.display.set_caption("Brick Breaker")

# Load the ball image
ball_image = pygame.image.load("ball.png")

# Load the paddle image
paddle_image = pygame.image.load("paddle.png")

# Load the heart image
heart_image = pygame.image.load("heart.png")

# Load the 1_brick image
brick1_image = pygame.image.load("1_brick.png")

# Load the 2_brick image
brick2_image = pygame.image.load("2_brick.png")

# Load the 3_brick image
brick3_image = pygame.image.load("3_brick.png")

# Set the font for the countdown and score
font = pygame.font.Font(None, 36)

# Set the ball's initial position and velocity
ball_x = WIDTH / 2
ball_y = HEIGHT / 2
ball_vx = 3
ball_vy = 3

# Set the paddle's initial position and velocity
paddle_x = WIDTH / 2
paddle_y = HEIGHT - 50
paddle_vx = 5

# Set the number of hearts the player has
hearts = 3

# Set the score to 0
score = 0

# Set the number of bricks
bricks = []

# Set the number of rows and columns of bricks
rows = 5
columns = 10

# Create the bricks
for row in range(rows):
    for column in range(columns):
        brick_x = column * 75 + 10
        brick_y = row * 50 + 10
        if row == 0:
            brick = {"x": brick_x, "y": brick_y, "image": brick3_image, "hits": 3}
        elif row == 1 or row == 2:
            brick = {"x": brick_x, "y": brick_y, "image": brick2_image, "hits": 2}
        else:
            brick = {"x": brick_x, "y": brick_y, "image": brick1_image, "hits": 1}
        bricks.append(brick)

# Set the countdown to 3
countdown = 3

# Set the game to running
running = True

# Main game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the ball's position
    ball_x += ball_vx
    ball_y += ball_vy

    # Check if the ball has hit the left or right wall
    if ball_x > WIDTH - 20 or ball_x < 20:
        ball_vx *= -1

    # Check if the ball has hit the top wall
    if ball_y < 20:
        ball_vy *= -1

    # Check if the ball has hit the paddle
    if ball_y > paddle_y and ball_x > paddle_x and ball_x < paddle_x + 100:
        ball_vy *= -1

    # Check if the ball has hit the bottom wall
    if ball_y > HEIGHT:
        # Decrement the number of hearts
        hearts -= 1

        # Reset the ball's position and velocity
        ball_x = WIDTH / 2
        ball_y = HEIGHT / 2
        ball_vx = 3
        ball_vy = 3

        # Reset the paddle's position
        paddle_x = WIDTH / 2
        paddle_y = HEIGHT - 50

        # If the player is out of hearts, end the game
        if hearts == 0:
            running = False

    # Update the paddle's position
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_vx
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - 100:
        paddle_x += paddle_vx

    # Check if the player has destroyed all the bricks
    if not bricks:
        # Reset the bricks with random placement
        bricks = []
        for row in range(rows):
            for column in range(columns):
                brick_x = column * 75 + 10
                brick_y = row * 50 + 10
                if row == 0:
                    brick = {"x": brick_x, "y": brick_y, "image": brick3_image, "hits": 3}
                elif row == 1 or row == 2:
                    brick = {"x": brick_x, "y": brick_y, "image": brick2_image, "hits": 2}
                else:
                    brick = {"x": brick_x, "y": brick_y, "image": brick1_image, "hits": 1}
                bricks.append(brick)

    # Check if the ball has hit a brick
    for brick in bricks:
        if ball_x > brick["x"] and ball_x < brick["x"] + 75 and ball_y > brick["y"] and ball_y < brick["y"] + 50:
            # Decrement the number of hits the brick has
            brick["hits"] -= 1

            # If the brick has been destroyed, remove it from the list
            if brick["hits"] == 0:
                bricks.remove(brick)

                # Increment the score
                score += 10

            # Change the direction of the ball
            ball_vy *= -1

            # If the brick has one hit left, change its image
            if brick["hits"] == 1:
                brick["image"] = brick1_image
            # If the brick has two hits left, change its image
            elif brick["hits"] == 2:
                brick["image"] = brick2_image

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the countdown
    if countdown > 0:
        text = font.render(str(countdown), True, (255, 255, 255))
        screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
        countdown -= 1
    else:
        # Draw the ball
        screen.blit(ball_image, (ball_x, ball_y))

        # Draw the paddle
        screen.blit(paddle_image, (paddle_x, paddle_y))

        # Draw the bricks
        for brick in bricks:
            screen.blit(brick["image"], (brick["x"], brick["y"]))

        # Draw the hearts
        for i in range(hearts):
            screen.blit(heart_image, (WIDTH - (i + 1) * 50, 10))

        # Draw the score
        text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Wait 10 milliseconds
    pygame.time.wait(10)

# Display the "GAME OVER" text
text = font.render("GAME OVER", True, (255, 255, 255))
screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
pygame.display.flip()

# Wait 3 seconds
pygame.time.wait(3000)

# Quit Pygame
