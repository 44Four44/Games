from Mino import *

# List of all minos
minos = []
start = Mino(random.choice(shapes), True)

# Active Mino that is being controlled by player
activeM = start
minos.append(start)

# Mino in holding
holdM = Mino(random.choice(shapes), False)
for piece in holdM.pieces:
    blocks.remove(piece)

# Queue of upcoming minos
queue = []
for i in range(3):
    min = Mino(random.choice(shapes), False)
    queue.append(min)
    for piece in min.pieces:
        blocks.remove(piece)

# Levelling
lines = 0
level = 1
levelInterval = 5
dropPeriods = [80, 60, 40, 30, 20, 15, 10, 8, 6, 5, 4, 3, 2, 1]

# Counter that goes through cycles through 1 to 100 on frames
counter = 1

dropCounter = 1
dropPeriod = dropPeriods[0]

# True if the user is able to switch to another piece
canHold = True
# Piece that is stored as a switch
holdShape = ''

# Set up walls
for i in range(-1, rows + 1):
    walls.append([-1, i])
    walls.append([columns, i])

for i in range(0, columns):
    walls.append([i, rows])

while run:
    pygame.time.delay(math.floor(1000/FPS))

    # Count counters
    if counter < 1000:
        counter += 1
    else:
        counter = 1

    if dropCounter < dropPeriod:
        dropCounter += 1
    else:
        dropCounter = 1

    # Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Mouse events
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePress = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousePress = False

        # Key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Spin piece clockwise
                activeM.spin("cw")

            if event.key == pygame.K_DOWN:
                downPress = True
            if event.key == pygame.K_LEFT:
                leftPress = True
            if event.key == pygame.K_RIGHT:
                rightPress = True

            if event.key == pygame.K_SPACE:
                score += activeM.drop()

            if event.key == pygame.K_z:
                # Spin piece counter clockwise
                activeM.spin("ccw")
            if event.key == pygame.K_c:
                # Swtich pieces with hold
                if canHold:
                    beforeShape = copy.copy(holdShape)
                    holdShape = activeM.shape

                    # Delete active Mino
                    for piece in activeM.pieces:
                        blocks.remove(piece)
                    minos.remove(activeM)

                    # Spawn Mino in hold
                    if beforeShape == '':
                        activeM = Mino(queue[0].shape, True)

                        # Move the queue up
                        min = Mino(random.choice(shapes), False)

                        for piece in min.pieces:
                            blocks.remove(piece)

                        queue.append(min)
                        del queue[0]

                    else:
                        activeM = Mino(beforeShape, True)

                    # Update hold Mino and add activeM to minos on the board
                    holdM = Mino(holdShape, False)
                    for piece in holdM.pieces:
                        blocks.remove(piece)

                    minos.append(activeM)

                    canHold = False



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                downPress = False
            if event.key == pygame.K_LEFT:
                leftPress = False
            if event.key == pygame.K_RIGHT:
                rightPress = False


    # Screen display
    screen.fill((255, 255, 255))

    screen.blit(board, ((sWidth - bWidth)/2, (sHeight - bHeight)/2))
    board.fill(black)

    if downPress and counter % 3 == 0:
        activeM.move("down")
        score += 1
    if leftPress and counter % 4 == 0:
        activeM.move("left")
    if rightPress and counter % 4 == 0:
        activeM.move("right")

    if dropCounter == dropPeriod:
        activeM.move("down")

    # Clear lines
    if not activeM.active:

        # Rows that are going to be cleared

        cleared = []

        for y in range(rows):
            for x in range(columns):
                # If at least one block in the row is missing it is not cleared so check the next row
                if [x, y] not in blocks:
                    break

                # All the blocks are filled in this row
                if x == columns - 1:
                    cleared.append(y)


        # Topmost row cleared
        if cleared:
            print("Lines cleared: {}".format(cleared))

            # Clear all blocks as they are readded later
            blocks.clear()

            # minos that are completely cleared
            deadMinos = []

            # Clear pieces from Mino objects
            for mino in minos:
                # print("--------{}--------".format(mino.shape))
                # print("pieces: {}".format(mino.pieces))
                # List of pieces that will be cleared
                removing = []

                for piece in mino.pieces:
                    # Clear
                    if piece[1] in cleared:
                        removing.append(piece)

                # print("pieces that are going to be removed: {}".format(removing))
                # remove pieces in removing list
                mino.pieces = [i for i in mino.pieces if i not in removing]

                # print("pieces after clearing: {}".format(mino.pieces))

                # Delete Mino if all pieces are cleared
                if mino.pieces:
                    # Move down if above the topmost cleared row
                    for clearing in cleared:
                        for i in range(len(mino.pieces)):
                            if mino.pieces[i][1] < clearing:
                                mino.pieces[i] = [mino.pieces[i][0], mino.pieces[i][1] + 1]
                else:
                    deadMinos.append(mino)

            # Delete completely cleared minos
            for mino in deadMinos:
                minos.remove(mino)

            # Readd block pieces
            for mino in minos:
                blocks.extend(mino.pieces)

            # Scoring
            # Scores for single, double, triple and quadruple (tetris) line clear
            scores = [100, 300, 500, 800]
            score += scores[len(cleared) - 1]

            # Levelling
            lines += len(cleared)
            while lines >= level*levelInterval:
                level += 1
                dropPeriod = dropPeriods[level - 1]


    # Generates a new block if activeM is not active anymore
    if not activeM.active:
        # Take the next Mino in queue
        activeM = Mino(queue[0].shape, True)

        # Move the queue up
        min = Mino(random.choice(shapes), False)

        for piece in min.pieces:
            blocks.remove(piece)

        queue.append(min)
        del queue[0]

        minos.append(activeM)

        canHold = True

    # Draw grid lines
    for i in range(1, columns):
        pygame.draw.line(board, darkGrey, [i*tileSize, 0], [i*tileSize, rows*tileSize], 1)
    for i in range(1, rows):
        pygame.draw.line(board, darkGrey, [0, i*tileSize], [columns*tileSize, i*tileSize], 1)

    for mino in minos:
        mino.draw()

    #  For debugging, displays the positions of all blocks on the grid
    for block in blocks:
        pygame.draw.rect(board, white, [block[0]*tileSize, block[1]*tileSize, 4, 4])

    # Draw holding piece
    if not holdShape == '':
        for piece in holdM.pieces:
            # Border thickness
            border = 1

            # Position
            x = 60
            y = 100
            pygame.draw.rect(screen, darkGrey, [x + piece[0] * tileSize, y + piece[1] * tileSize, tileSize, tileSize])

            # Fill
            pygame.draw.rect(screen, holdM.color, [x + piece[0] * tileSize + border, y + piece[1] * tileSize + border,
                                                   tileSize - 2 * border, tileSize - 2 * border])

    # Draw queue
    # Position
    x = sWidth - 100
    y = 100
    for mino in queue:
        for piece in mino.pieces:
            # Border thickness
            border = 1
            pygame.draw.rect(screen, darkGrey, [x + piece[0] * tileSize, y + piece[1] * tileSize, tileSize, tileSize])
            # Fill
            pygame.draw.rect(screen, mino.color, [x + piece[0] * tileSize + border, y + piece[1] * tileSize + border,
                                                   tileSize - 2 * border, tileSize - 2 * border])
        y += 100

    # Score display
    text = font.render("Score", True, black)
    screen.blit(text, [10, sHeight - 240])
    text = font.render(str(score), True, black)
    screen.blit(text, [10, sHeight - 210])

    # Level
    text = font.render("Level", True, black)
    screen.blit(text, [10, sHeight - 160])
    text = font.render(str(level), True, black)
    screen.blit(text, [10, sHeight - 130])

    # Lines cleared
    text = font.render("Lines", True, black)
    screen.blit(text, [10, sHeight - 80])
    text = font.render(str(lines), True, black)
    screen.blit(text, [10, sHeight - 50])


    # Update pygame display
    pygame.display.update()
pygame.quit()