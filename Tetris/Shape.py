from settings import *
class Shape():
    def __init__(self, name, color, pieces, center):
        self.name = name
        self.color = color
        self.pieces = pieces
        self.center = center

# List of possible Mino shapes with their data
shapes = ['I', 'O', 'T', 'S', 'Z', 'J', 'L']
shapeData = []
shapeData.append(Shape('I', lightBlue, [[-1, 0], [0, 0], [1, 0], [2, 0]], [0, 0]))
shapeData.append(Shape('O', yellow, [[0, 0], [1, 0], [0, 1], [1, 1]], [0, 1]))
shapeData.append(Shape('T', purple, [[0, 0], [-1, 1], [0, 1], [1, 1]], [0, 1]))
shapeData.append(Shape('S', green, [[0, 0], [1, 0], [-1, 1], [0, 1]], [0, 1]))
shapeData.append(Shape('Z', red, [[-1, 0], [0, 0], [0, 1], [1, 1]], [0, 1]))
shapeData.append(Shape('J', darkBlue, [[-1, 0], [-1, 1], [0, 1], [1, 1]], [0, 1]))
shapeData.append(Shape('L', orange, [[1, 0], [-1, 1], [0, 1], [1, 1]], [0, 1]))