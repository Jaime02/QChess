from PyQt5.QtGui import QPixmap

from .Queen import Queen
from .Piece import Piece, QColor, QPainter, QLabel


# Creation of the class King from where the classes BKing and WKing will inherit
# This class inherits at the same time from the class Piece
class King(Queen):
    def __init__(self, game, x, y):
        Queen.__init__(self, game, x, y)

    def is_on_check(self):
        mov = self.game.opponent_eatings()
        return any(self.coords == position for position in mov)

    def paintEvent(self, event):
        Piece.paintEvent(self, event)
        x, y = self.width(), self.height()
        qp = QPainter(self)
        if self.is_on_check():
            qp.fillRect(0, 0, x, y, QColor(225, 0, 0))

        qp.drawPixmap(0, 0, x, y, self.image)

    def possible_movements(self):
        # Creation of a list to append all the possible positions
        positions = []
        # Creation of a list that stores all the possible movements of the queen
        queen_positions = Queen.possible_movements(self)

        # The directions in which the king can move are the same as the queen so the only thing we have
        # to check is that the x and y coordinates do not go more than one square away from the king
        for position in queen_positions:
            if self.coords[0] - 1 <= position[0] <= self.coords[0] + 1:
                if self.coords[1] - 1 <= position[1] <= self.coords[1] + 1:
                    positions.append(position)

        return positions


# Creation of the class WKing (the parameters that change are the image, the name and the color)
class WKing(King):
    def __init__(self, game, x, y):
        King.__init__(self, game, x, y)
        self.image_path = f"./images/{self.game.piece_set}/wK"
        self.image = QPixmap(self.image_path)
        self.name = "wK"
        self.color = "w"


# Creation of the class BKing (the parameters that change are the same than WKing)
class BKing(King):
    def __init__(self, game, x, y):
        King.__init__(self, game, x, y)
        self.image_path = f"./images/{self.game.piece_set}/bK"
        self.image = QPixmap(self.image_path)
        self.name = "bK"
        self.color = "b"
