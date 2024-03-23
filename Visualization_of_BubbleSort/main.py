import pygame
from random import randint

#Config ----------------------
HOW_MANY_NUMBER = 1900
RANGE_OF_NUMBERS = (1, 1000)
WIDTH_OF_NUMBER = 1
#-----------------------------

# Generating Random Number array
array_to_sort = []
for i in range(HOW_MANY_NUMBER):
    array_to_sort.append(randint(RANGE_OF_NUMBERS[0], RANGE_OF_NUMBERS[1]))

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1900, 1000))
clock = pygame.time.Clock()
running = True

def drawing_array(array_to_sort: list, green):
    for index_of_number in range(len(array_to_sort)):
        height = array_to_sort[index_of_number]
        x = index_of_number * WIDTH_OF_NUMBER
        y = 1000 - height
        rectangle = pygame.rect.Rect(x, y, WIDTH_OF_NUMBER, height)
        if green:
            pygame.draw.rect(screen, (0, 255, 0), rectangle)
        else:
            pygame.draw.rect(screen, (255, 255, 255), rectangle)

Sorting_is_comlete = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Sorting an Array by bouble sort algorithm
    if not Sorting_is_comlete:

        for x in range(len(array_to_sort)):
            for i in range(len(array_to_sort)-1):
                if array_to_sort[i] > array_to_sort[i+1]:
                    helper = array_to_sort[i]
                    array_to_sort[i] = array_to_sort[i+1]
                    array_to_sort[i+1] = helper

            # Drawing numbers and refreshing screen
            screen.fill("black")
            drawing_array(array_to_sort, False)
            pygame.display.flip()

    else:
        drawing_array(array_to_sort, True)
    Sorting_is_comlete = True

    pygame.display.flip()

pygame.quit()
