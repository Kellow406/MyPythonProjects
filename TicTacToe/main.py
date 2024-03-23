import pygame
window = pygame.display.set_mode((500, 700))
class Field(): #Field that player can click and make the move
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = '*'+str(x)+str(y)
        self.image_x = pygame.image.load('1.png')
        self.image_o = pygame.image.load('2.png')
        self.hitbox = pygame.Rect(x, y, 161, 161)

    def draw(self):
        if self.state == '*':
            pygame.draw.rect(window, (128, 128, 128), self.hitbox)

        elif self.state == 'o':
            window.blit(self.image_o, (self.x, self.y))
        elif self.state == 'x':
            window.blit(self.image_x, (self.x, self.y))

    def tick(self):
        #checking collision with mouse
        if self.state == '*'+str(self.x)+str(self.y):
            if self.hitbox.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    return True
class Rectangle(): # just rectangle
    def __init__(self, x=0, y=0, width=100, height=100, r = 0, g = 0, b = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (r,g,b)
        self.hitbox = pygame.rect.Rect(x, y, width, height)


    def tick(self):
        hitbox = pygame.rect.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(window, self.color, self.hitbox)

# This Function check that witch player won.
# If anyone isn' t a winner function return None
def who_win(x1, x2, x3, x4, x5, x6, x7, x8, x9):

    if x1 == x2 and x1 == x3:
        return x1
    elif x1 == x5 and x1 == x9:
        return x1
    elif x1 == x4 and x1 == x7:
        return x1
    elif x4 == x5 and x4 == x6:
        return x4
    elif x7 == x8 and x7 == x9:
        return x7
    elif x3 == x5 and x3 == x7:
        return x3
    elif x2 == x5 and x2 == x8:
        return x2
    elif x3 == x6 and x3 == x9:
        return x3


def main(screen_width,screen_height , FPS):

    winner = pygame.image.load('winner.png')
    pygame.init()

    #Making list of lines and add to it lines that will draw game board
    lines = []
    lines.append(Rectangle(0, 500/3, 500, 10))
    lines.append(Rectangle(0, (500/3)*2, 500, 10))
    lines.append(Rectangle((500/3)-5, 0, 10, 500))
    lines.append(Rectangle((500/3)*2-5, 0, 10, 500))
    lines.append(Rectangle(0, 500, 500, 10))


    # Making
    coordinates_of_fields = [0, 169, 340]
    fields = []
    for x in coordinates_of_fields:
        for y in coordinates_of_fields:
            fields.append(Field(x, y))

    # Declaring who starts
    who_now = 'x'
    showing_who_now = Field(166, 530)


    # Setup Game Loop
    run = True
    while run:

        # Pygame stuff
        pygame.time.Clock().tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        window.fill((255, 255, 255))

        # Cheking that game shoudnt be end
        # Btw sorry for this line
        if who_win(fields[0].state, fields[1].state, fields[2].state, fields[3].state, fields[4].state, fields[5].state, fields[6].state, fields[7].state, fields[8].state) == None:
            for field in fields:

                #Drawing every field
                field.draw()


                if field.tick():
                    field.state = who_now
                    if who_now == 'x':
                        who_now = 'o'
                    else: who_now = 'x'

            # Drawing lines of game board
            for line in lines:
                line.draw()

            # Showing player who has move
            showing_who_now.draw()
            showing_who_now.state = who_now


        else:

            # If someone win
            window.blit(winner, (170, 166))
            showing_who_now.y = 166*2 - 40
            showing_who_now.draw()
            showing_who_now.state = who_win(fields[0].state, fields[1].state, fields[2].state, fields[3].state, fields[4].state, fields[5].state, fields[6].state, fields[7].state, fields[8].state)
        pygame.display.update()


if __name__ == "__main__":
    screen_width = 500
    screen_height = 700
    FPS = 60
    main(screen_width, screen_height, FPS)
