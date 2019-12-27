from settings import *
class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, size, fill, mine, mode):
        self.size = size
        self.b = 1
        self.fill = fill
        self.color = fill
        self.mine = mine
        self.mode = mode

        pygame.sprite.Sprite.__init__(self)
        tiles.append(self)

        self.image = pygame.Surface((size, size))

        # Define tile's rectangle
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        global first_move
        # Mouse events
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            # Darkens as cursor hovers over

            if pygame.mouse.get_pressed()[2]:
                # Flag a tile
                self.mode = 1
            elif pygame.mouse.get_pressed()[0]:
                # Reveal a tile
                self.mode = 2
                first_move = True
                first_move = True
        else:
            self.color = self.fill

    def draw(self):
        if self.mode == 0:
            self.color = self.fill
        elif self.mode == 1:
            self.color = red
        elif self.mode == 2:
            if self.mine:
                self.color = black
            else:
                self.color = light_grey
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.color = [hex * 0.9 for hex in self.color]

        pygame.draw.rect(screen, (0, 0, 0), (self.rect.x, self.rect.y, self.size, self.size))
        pygame.draw.rect(screen, self.color, (self.rect.x + self.b, self.rect.y + self.b, self.size-self.b*2, self.size-self.b*2))
