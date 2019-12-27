from Shape import *
class Mino(pygame.sprite.Sprite):
    def __init__(self, shape, adjust):

        # True if this is the block currently being moved
        self.active = True

        # I, O, T, S, Z, J, or L
        self.shape = shape

        shapeObject = copy.copy(shapeData[shapes.index(shape)])

        self.color = copy.copy(shapeObject.color)
        self.pieces = copy.copy(shapeObject.pieces)
        self.center = copy.copy(shapeObject.center)


        # # Skeleton mode
        # if shape == 'I':
        #     self.color = lightBlue
        #     self.pieces = [[-2, 0], [-1, 0], [1, 0], [2, 0]]
        #     self.center = [0, 0]
        # if shape == 'O':
        #     self.color = yellow
        #     self.pieces = [[-1, 0], [1, 0], [-1, 2], [1, 2]]
        #     self.center = [0, 1]
        # if shape == 'T':
        #     self.color = purple
        #     self.pieces = [[0, 0], [-1, 2], [0, 2], [1, 2]]
        #     self.center = [0, 1]
        # if shape == 'S':
        #     self.color = green
        #     self.pieces = [[0, 0], [1, 0], [-1, 2], [0, 2]]
        #     self.center = [0, 1]
        # if shape == 'Z':
        #     self.color = red
        #     self.pieces = [[-1, 0], [0, 0], [0, 2], [1, 2]]
        #     self.center = [0, 1]
        # if shape == 'J':
        #     self.color = darkBlue
        #     self.pieces = [[-1, 0], [-1, 2], [0, 2], [1, 2]]
        #     self.center = [0, 1]
        # if shape == 'L':
        #     self.color = orange
        #     self.pieces = [[1, 0], [-1, 2], [0, 2], [1, 2]]
        #     self.center = [0, 1]

        # Adjust pieces to center
        if adjust:
            adjustment = math.floor((columns - 1) / 2)
            for i in range(len(self.pieces)):
                self.pieces[i] = [self.pieces[i][0] + adjustment, self.pieces[i][1]]

            self.center = [self.center[0] + adjustment, self.center[1]]

        blocks.extend(self.pieces)

    def draw(self):
        for piece in self.pieces:
            # Border thickness
            border = 1
            pygame.draw.rect(board, darkGrey, [piece[0] * tileSize, piece[1] * tileSize, tileSize, tileSize])

            # Fill
            pygame.draw.rect(board, self.color, [piece[0] * tileSize + border, piece[1] * tileSize + border, tileSize - 2*border, tileSize - 2*border])

    def move(self, direction):

        # Remove pieces from blocks list
        for piece in self.pieces:
            blocks.remove(piece)

        # Movements of X and Y coordinate
        moveX = 0
        moveY = 0

        if direction == "down":
            moveX = 0
            moveY = 1

        if direction == "left":
            moveX = -1
            moveY = 0

        if direction == "right":
            moveX = 1
            moveY = 0

        # Pieces after movement
        futurePieces = []
        for piece in self.pieces:
            futurePieces.append([piece[0] + moveX, piece[1] + moveY])

        # Check for collision with other minos or ground
        if any(i in futurePieces for i in blocks) or any(i in futurePieces for i in walls):
            # Put original pieces back into blocks lists
            blocks.extend(self.pieces)

            # Deactivates block if the move was down
            if direction == "down":
                self.active = False
        else:

            # Move coordinates
            self.pieces = futurePieces

            self.center = [self.center[0] + moveX, self.center[1] + moveY]

            # Add new pieces into blocks list
            blocks.extend(self.pieces)


    def spin(self, direction):
        # O minos don't spin
        if not self.shape == 'O':
            # Remove pieces from blocks list
            for piece in self.pieces:
                blocks.remove(piece)

            # Future coordinates of Mino
            futurePieces = []

            # Clockwise spin
            if direction == "cw":
                for piece in self.pieces:
                    futurePieces.append([self.center[0] + self.center[1] - piece[1], self.center[1] + piece[0] - self.center[0]])
            elif direction == "ccw":
                for piece in self.pieces:
                    futurePieces.append([self.center[0] - self.center[1] + piece[1], self.center[1] - piece[0] + self.center[0]])

            if not (any(i in futurePieces for i in blocks) or any(i in futurePieces for i in walls)):
                # Move coordinates
                self.pieces = futurePieces
                # Add new pieces into blocks list
            blocks.extend(self.pieces)

    def drop(self):

        # Remove pieces from blocks list
        for piece in self.pieces:
            blocks.remove(piece)

        # Future coordinates of Mino
        futurePieces = []
        for piece in self.pieces:
            futurePieces.append([piece[0], piece[1] + 1])

        distance = 0

        while not (any(i in futurePieces for i in blocks) or any(i in futurePieces for i in walls)):
            for i in range(len(self.pieces)):
                self.pieces[i] = [self.pieces[i][0], self.pieces[i][1] + 1]
            for i in range(len(futurePieces)):
                futurePieces[i] = [futurePieces[i][0], futurePieces[i][1] + 1]
            distance += 1

        # Add new pieces into blocks list
        blocks.extend(self.pieces)

        # Deactivate self
        self.active = False

        # Return drop distance for score calculating
        return distance * 2


