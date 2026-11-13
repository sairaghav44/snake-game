import pygame

import random

pygame.init()
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1000, 680))

play_again_button = pygame.Rect(400, 390, 200, 60)


snake_x = 120
snake_y = 120
snake_body = [(snake_x, snake_y)]
snake_length = 1
score = 0
direction = "NONE"

def spawn_apple():

    while True:

        x = random.randrange(0, screen.get_width(), 40)
        y = random.randrange(0, screen.get_height() // 40 * 40, 40)

        position = (x, y)

        if position not in snake_body:
            return position


apple_position = spawn_apple()

apple_x,apple_y = apple_position

running = True
game_over = False


while running:
    screen.fill((0, 0, 0))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and not game_over:

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over and play_again_button.collidepoint(event.pos):
                # Reset game state
                snake_x = 120
                snake_y = 120
                snake_body = [(snake_x, snake_y)]
                snake_length = 1
                
                score = 0
                direction = "NONE"
                apple_position = spawn_apple()
                apple_x, apple_y = apple_position
                game_over = False

    # GAME UPDATE:runs while the game is active
    if not game_over:

        # Movement
        if direction == "RIGHT":
            snake_x += 40
            if snake_x >= screen.get_width() - 40:
                snake_x = screen.get_width() - 40

        if direction == "LEFT":
            snake_x -= 40
            if snake_x <= 0:
                snake_x = 0

        if direction == "UP":
            snake_y -= 40
            if snake_y <= 0:
                snake_y = 0

        if direction == "DOWN":
            snake_y += 40
            if snake_y >= screen.get_height() - 40:
                snake_y = screen.get_height() - 40

        # Snake body update
        snake_body.insert(0, (snake_x, snake_y))

        if len(snake_body) > snake_length:
            snake_body.pop()

        # Self-collision detection
        for segment in snake_body[1:]:
            if (snake_x, snake_y) == segment:
                game_over = True

        # Apple collision
        snake_rect = pygame.Rect(snake_x, snake_y, 40, 40)
        apple_rect = pygame.Rect(apple_x, apple_y, 40, 40)

        if snake_rect.colliderect(apple_rect):
            snake_length += 1
            score += 1

            apple_position = spawn_apple()
            apple_x, apple_y = apple_position

            print("apple eaten !!!")

    
    for segment in snake_body:
        pygame.draw.rect(
            screen,
            (0, 225, 0),
            (segment[0], segment[1], 40, 40)
        )

    pygame.draw.rect(
        screen,
        (225, 0, 0),
        (apple_x, apple_y, 40, 40)
    )

    if game_over:

        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        final_score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
        play_again_text = font.render("PLAY AGAIN", True, (0, 0, 0))

        screen.blit(game_over_text, (400, 280))
        screen.blit(final_score_text, (400, 330))

        pygame.draw.rect(screen, (0, 255, 0), play_again_button)
        screen.blit(play_again_text, (415, 408))
        
    pygame.display.flip()
    clock.tick(10)

#py -3.13 snake-game_v02.py