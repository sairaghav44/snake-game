import pygame

import random

pygame.init()
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1000, 680))

snake_x = 100
snake_y = 100
snake_body = [(snake_x, snake_y)]
snake_length = 1
score = 0
direction = "NONE"

apple_positions = [
    (40, 40),
    (200, 40),
    (400, 40),
    (600, 40),
    (800, 40),

    (120, 120),
    (320, 120),
    (520, 120),
    (720, 120),
    (920, 120),

    (40, 240),
    (240, 240),
    (440, 240),
    (640, 240),
    (840, 240),

    (120, 360),
    (320, 360),
    (520, 360),
    (720, 360),
    (920, 360),

    (40, 480),
    (240, 480),
    (440, 480),
    (640, 480),
    (840, 480),

    (160, 560),
    (400, 560),
    (640, 560),
    (880, 560)
]
apple_position = random.choice(apple_positions)

apple_x,apple_y = apple_position

running = True
game_over = False


while running:
    screen.fill((0, 0, 0))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    print("game loop is running ")


    if direction == "RIGHT":
     snake_x = snake_x +40
     if snake_x >= screen.get_width() -40:
        snake_x = screen.get_width() -40

    if direction == "LEFT":
     snake_x = snake_x - 40
     if snake_x <= 0:
        snake_x = 0

    if direction == "UP":
         snake_y = snake_y - 40
         if snake_y <= 0:
            snake_y = 0

    if direction == "DOWN":
     snake_y = snake_y +40
     if snake_y >= screen.get_height() -40:
        snake_y = screen.get_height() -40

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                if direction != "LEFT":
                      direction = "RIGHT"

            if event.key == pygame.K_LEFT:
                if direction != "RIGHT":
                 direction = "LEFT"

            if event.key == pygame.K_UP:
                if direction != "DOWN":
                 direction = "UP"

            if event.key == pygame.K_DOWN:
                if direction != "UP":
                 direction = "DOWN"

    snake_body.insert(0, (snake_x, snake_y))   
    if len(snake_body)> snake_length :
        snake_body.pop()

    for segment in snake_body[1:]:
        if (snake_x, snake_y) == segment:
            game_over = True  

    if game_over:
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(game_over_text, (400, 300))

    if game_over:
       running = False       

    snake_rect = pygame.Rect(snake_x, snake_y, 40, 40)
    apple_rect = pygame.Rect(apple_x, apple_y, 40, 40)

    for segment in snake_body:
        pygame.draw.rect(
            screen,
            (0,225,0),
            (segment[0],segment[1],40,40)
        )
    pygame.draw.rect(
        screen,
        (225,0,0),
        (apple_x,apple_y,40,40)
    )            


    if snake_rect.colliderect(apple_rect):
        snake_length +=1
        score += 1
        apple_position = random.choice(apple_positions)
        apple_x, apple_y = apple_position
        print("apple eaten !!!")


    pygame.display.flip()
    clock.tick(10)

#py -3.13 snake-game.py