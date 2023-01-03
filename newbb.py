import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

# images
ball_image = pygame.image.load("ball.png")
paddle_image = pygame.image.load("paddle.png")
heart_image = pygame.image.load("heart.png")
brick1_image = pygame.image.load("1_brick.png")
brick2_image = pygame.image.load("2_brick.png")
brick3_image = pygame.image.load("3_brick.png")

font = pygame.font.Font(None, 36)

# ball position and speed
ball_x = WIDTH / 2
ball_y = HEIGHT / 2
ball_vx = 3
ball_vy = 3

# paddle position and speed
paddle_x = WIDTH / 2
paddle_y = HEIGHT - 50
paddle_vx = 5

# life of player, score
hearts = 3
score = 0

# empty list for bricks
bricks = []

# rows and columns of bricks
rows = 5
columns = 10

# bricks
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

countdown = 3
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ball's position
    ball_x += ball_vx
    ball_y += ball_vy

    # if ball hits sides and top walls
    if ball_x > WIDTH - 20 or ball_x < 20:
        ball_vx *= -1

    if ball_y < 20:
        ball_vy *= -1

    # if ball hits the paddle and bottom wall
    if ball_y > paddle_y and ball_x > paddle_x and ball_x < paddle_x + 100:
        ball_vy *= -1

    if ball_y > HEIGHT:
        hearts -= 1

        # ball's position and speed
        ball_x = WIDTH / 2
        ball_y = HEIGHT / 2
        ball_vx = 3
        ball_vy = 3

        # sets the paddle's position
        paddle_x = WIDTH / 2
        paddle_y = HEIGHT - 50

        # 0 player lives = game ends
        if hearts == 0:
            running = False

    # update paddle's position
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_vx
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - 100:
        paddle_x += paddle_vx

    # if player destroyed all the bricks
    if not bricks:
        # reset bricks at random placement
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

        # if ball hits a brick
    for brick in bricks:
        if ball_x > brick["x"] and ball_x < brick["x"] + 75 and ball_y > brick["y"] and ball_y < brick["y"] + 50:
            # decrement number of hits the brick has
            brick["hits"] -= 1

            # if brick destroyed, remove from list
            if brick["hits"] == 0:
                bricks.remove(brick)

                # score
                score += 10

            # change direction of ball
            ball_vy *= -1

            # change image when 1 hit left
            if brick["hits"] == 1:
                brick["image"] = brick1_image
            # change image when two hits left
            elif brick["hits"] == 2:
                brick["image"] = brick2_image

    screen.fill((0, 0, 0))

    if countdown > 0:
        text = font.render(str(countdown), True, (255, 255, 255))
        screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
        countdown -= 1
    else:
        # ball, paddle, brick, hearts, score
        screen.blit(ball_image, (ball_x, ball_y))

        screen.blit(paddle_image, (paddle_x, paddle_y))

        for brick in bricks:
            screen.blit(brick["image"], (brick["x"], brick["y"]))

        for i in range(hearts):
            screen.blit(heart_image, (WIDTH - (i + 1) * 50, 10))

        text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(text, (10, 10))

    pygame.display.flip()

    # time wait
    pygame.time.wait(10)

# "GAME OVER" text
text = font.render("GAME OVER", True, (255, 255, 255))
screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
pygame.display.flip()

# 3 sec wait
pygame.time.wait(3000)

# Quit Pygame - adjusted notes