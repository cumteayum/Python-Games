import pygame as pg
import random

pg.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 1366
screen_height = 768
gameWindow = pg.display.set_mode((screen_width, screen_height))

# Game Title
pg.display.set_caption("SnakesWithIshan")
pg.display.update()
clock = pg.time.Clock()
font = pg.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pg.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,233,210))
        text_screen("Welcome to Snakes", black, 260, 250)
        text_screen("Press Space Bar To Play", black, 232, 290)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit_game = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    gameloop()

        pg.display.update()
        clock.tick(40)


# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit_game = True

                if event.type == pg.K_SPACE:
                    if event.key == pg.K_SPACE:
                        welcome()

        else:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit_game = True

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pg.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pg.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pg.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pg.K_q:
                        score +=10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<8:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            text_screen("Score: " + str(score) + "  Hiscore: "+str(hiscore), red, 5, 5)
            pg.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
            plot_snake(gameWindow, black, snk_list, snake_size)
        pg.display.update()
        clock.tick(fps)

    pg.quit()
    quit()
welcome() 
