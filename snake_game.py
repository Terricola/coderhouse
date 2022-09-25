import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 650
dis_height  = 450

dis = pygame.display.set_mode((dis_width, dis_height)) # Tamaño de la pantalla
pygame.display.set_caption("Snake Game by Michael") # Da nombre a la pantalla

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list): # Esta es la funcion que hare crecer la snake
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

# Ciclo while para evitar que se cierred automaticamente la pantalla con quit()
#game_over = False

def gameLoop():  # creating a function
    game_over = False
    game_close = False

    # Definimos el centro de la pantalla donde aparecera la "snake"
    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("Perdiste!, Presiona 'Q' para salir o 'C' para jugar de nuevo", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                        #time.sleep(3) --> Esto nos da 3 segundos para que la pantalla se cierre
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get(): # Captura cualquier evento que suceda en la ventana
            #print(event) # Imprime todas las acciones que se realicen en la pantalla
            if event.type == pygame.QUIT: # Lo usamos para poder cerrar la pantalla
                game_over = True
            if event.type == pygame.KEYDOWN: # Inicializamos la posibilidad de usar las flechas del teclado
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0                
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
    
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True    
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue) # Cambiamos el fondo de pantalla
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) # Dibujamos la comida
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        
        our_snake(snake_block, snake_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)
        
    pygame.quit()
    quit()

gameLoop()