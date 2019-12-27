from Tile import *

# Create tile objects
for X in range(x):
    for Y in range(y):
        Tile(margin + X*tile_size, header + margin + Y*tile_size, tile_size, grey, False, 0)

while run:
    pygame.time.delay(math.floor(1000/FPS))

    # Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            press = True
        if event.type == pygame.MOUSEBUTTONUP:
            press = False

    # Screen display
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, light_grey, (margin, header + margin, width, height))

    # Tiles
    for tile in tiles:
        tile.update()
        tile.draw()

    print(first_move)

    pygame.display.update()
pygame.quit()