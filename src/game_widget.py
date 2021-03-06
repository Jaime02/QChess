from PyQt5.QtWidgets import QWidget, QGridLayout, QMessageBox
from PyQt5.QtGui import QPixmap
from QChess.src.pieces.Bishop import WBishop, BBishop
from QChess.src.pieces.Blank import Blank
from QChess.src.pieces.King import WKing, BKing
from QChess.src.pieces.Knight import WKnight, BKnight
from QChess.src.pieces.Pawn import WPawn, BPawn
from QChess.src.pieces.Queen import WQueen, BQueen
from QChess.src.pieces.Rook import WRook, BRook


class GameWidget(QWidget):
    def __init__(self, window, w):
        QWidget.__init__(self, w)

        self.main_window = window

        # Main layout
        self.grid_layout: QGridLayout = QGridLayout()
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setHorizontalSpacing(0)
        self.grid_layout.setVerticalSpacing(0)
        self.setLayout(self.grid_layout)

        self.piece_set = "Default"

        # Initial board state
        self.pieces = [
            [BRook(self, 0, 0,), BKnight(self, 0, 1), BBishop(self, 0, 2), BQueen(self, 0, 3),
             BKing(self, 0, 4,), BBishop(self, 0, 5), BKnight(self, 0, 6), BRook(self, 0, 7)],
            [BPawn(self, 1, 0,), BPawn(self, 1, 1),   BPawn(self, 1, 2),   BPawn(self, 1, 3),
             BPawn(self, 1, 4,), BPawn(self, 1, 5),   BPawn(self, 1, 6),   BPawn(self, 1, 7)],
            [Blank(self, 2, 0),  Blank(self, 2, 1),   Blank(self, 2, 2),   Blank(self, 2, 3),
             Blank(self, 2, 4),  Blank(self, 2, 5),   Blank(self, 2, 6),   Blank(self, 2, 7)],
            [Blank(self, 3, 0),  Blank(self, 3, 1),   Blank(self, 3, 2),   Blank(self, 3, 3),
             Blank(self, 3, 4),  Blank(self, 3, 5),   Blank(self, 3, 6),   Blank(self, 3, 7)],
            [Blank(self, 4, 0),  Blank(self, 4, 1),   Blank(self, 4, 2),   Blank(self, 4, 3),
             Blank(self, 4, 4),  Blank(self, 4, 5),   Blank(self, 4, 6),   Blank(self, 4, 7)],
            [Blank(self, 5, 0),  Blank(self, 5, 1),   Blank(self, 5, 2),   Blank(self, 5, 3),
             Blank(self, 5, 4),  Blank(self, 5, 5),   Blank(self, 5, 6),   Blank(self, 5, 7)],
            [WPawn(self, 6, 0),  WPawn(self, 6, 1),   WPawn(self, 6, 2),   WPawn(self, 6, 3),
             WPawn(self, 6, 4),  WPawn(self, 6, 5),   WPawn(self, 6, 6),   WPawn(self, 6, 7)],
            [WRook(self, 7, 0),  WKnight(self, 7, 1), WBishop(self, 7, 2), WQueen(self, 7, 3),
             WKing(self, 7, 4),  WBishop(self, 7, 5), WKnight(self, 7, 6), WRook(self, 7, 7)]
        ]

        for x in range(8):
            for y in range(8):
                self.grid_layout.addWidget(self.pieces[x][y], x, y)

        self.turn = "w"
        self.selected_piece = None

    def reset_board(self):
        # This function returns the board to its initial state

        for x in range(8):
            for y in range(8):
                widget = self.grid_layout.itemAtPosition(x, y).widget()
                self.grid_layout.removeWidget(widget)
                widget.deleteLater()

        # Widgets can not be copied, hence they must be redeclared
        self.pieces = [
            [BRook(self, 0, 0,), BKnight(self, 0, 1), BBishop(self, 0, 2), BQueen(self, 0, 3),
             BKing(self, 0, 4,), BBishop(self, 0, 5), BKnight(self, 0, 6), BRook(self, 0, 7)],
            [BPawn(self, 1, 0,), BPawn(self, 1, 1),   BPawn(self, 1, 2),   BPawn(self, 1, 3),
             BPawn(self, 1, 4,), BPawn(self, 1, 5),   BPawn(self, 1, 6),   BPawn(self, 1, 7)],
            [Blank(self, 2, 0),  Blank(self, 2, 1),   Blank(self, 2, 2),   Blank(self, 2, 3),
             Blank(self, 2, 4),  Blank(self, 2, 5),   Blank(self, 2, 6),   Blank(self, 2, 7)],
            [Blank(self, 3, 0),  Blank(self, 3, 1),   Blank(self, 3, 2),   Blank(self, 3, 3),
             Blank(self, 3, 4),  Blank(self, 3, 5),   Blank(self, 3, 6),   Blank(self, 3, 7)],
            [Blank(self, 4, 0),  Blank(self, 4, 1),   Blank(self, 4, 2),   Blank(self, 4, 3),
             Blank(self, 4, 4),  Blank(self, 4, 5),   Blank(self, 4, 6),   Blank(self, 4, 7)],
            [Blank(self, 5, 0),  Blank(self, 5, 1),   Blank(self, 5, 2),   Blank(self, 5, 3),
             Blank(self, 5, 4),  Blank(self, 5, 5),   Blank(self, 5, 6),   Blank(self, 5, 7)],
            [WPawn(self, 6, 0),  WPawn(self, 6, 1),   WPawn(self, 6, 2),   WPawn(self, 6, 3),
             WPawn(self, 6, 4),  WPawn(self, 6, 5),   WPawn(self, 6, 6),   WPawn(self, 6, 7)],
            [WRook(self, 7, 0),  WKnight(self, 7, 1), WBishop(self, 7, 2), WQueen(self, 7, 3),
             WKing(self, 7, 4),  WBishop(self, 7, 5), WKnight(self, 7, 6), WRook(self, 7, 7)]
        ]

        # Restart of the turn and the selected piece
        self.turn = "w"
        self.main_window.update_turn_label("White's turn")
        self.selected_piece = None

        for x in range(8):
            for y in range(8):
                self.grid_layout.addWidget(self.pieces[x][y], x, y)

    def set_selected_piece(self, piece):
        # This function sets the clicked piece as the selected one
        if self.selected_piece:
            self.selected_piece.unselect()
        self.selected_piece = piece

    def opponent_eatings(self):
        opponent_pieces = []
        for row in self.pieces:
            for item in row:
                if item.color != self.turn and not isinstance(item, Blank):
                    opponent_pieces.append(item)

        mov = set()
        for piece in opponent_pieces:
            if piece.name[1] == "P":
                mov = mov.union(piece.possible_eatings())
            else:
                mov = mov.union(piece.possible_movements())

        return mov

    def free_movements(self):
        mov = self.opponent_eatings()
        # Selected piece is the king
        pos_mov = set(self.selected_piece.possible_movements())
        return pos_mov.difference(mov)

    def change_turn(self):
        # This function changes the player turn
        if self.selected_piece:
            self.selected_piece.unselect()
        if self.turn == "b":
            self.turn = "w"
            self.main_window.update_turn_label("White's turn")

        else:
            self.turn = "b"
            self.main_window.update_turn_label("Black's turn")

    def update_board(self):
        # This function updates the board when a piece has been moved
        # Two widgets have changed their positions and all the widgets are rearranged.
        # This could be improved
        # Deletes all the widgets from the grid
        for x in range(8):
            for y in range(8):
                self.grid_layout.removeWidget(self.pieces[x][y])
        # Adds all the widgets to the grid again
        for x in range(8):
            for y in range(8):
                self.grid_layout.addWidget(self.pieces[x][y], x, y)

    def highlight_possible_moves(self):
        # This function sets the highlight state True of the pieces which a piece can eat or move to them
        if self.selected_piece:
            if self.selected_piece.name[1] != "K":
                possible_movements = self.selected_piece.possible_movements()
            else:
                possible_movements = self.free_movements()
            for movement in possible_movements:
                self.pieces[movement[0]][movement[1]].highlight = True
                self.pieces[movement[0]][movement[1]].update()

    def eat_piece(self, eater_coords, eated_coords):
        # This function carries out the eating process of a piece
        # print(eater_coords, " eated ", eated_coords)

        self.grid_layout.removeWidget(self.pieces[eated_coords[0]][eated_coords[1]])
        self.pieces[eated_coords[0]][eated_coords[1]].deleteLater()

        w1 = self.pieces[eater_coords[0]][eater_coords[1]]
        w2 = Blank(self, *eater_coords)

        self.pieces[eated_coords[0]][eated_coords[1]] = w1
        self.pieces[eater_coords[0]][eater_coords[1]] = w2

        self.update_board()

        w1.coords = eated_coords
        w2.coords = eater_coords
        w1.update()
        w2.update()
        self.change_turn()

    def swap_pieces(self, coords1: tuple, coords2: tuple):
        # print("Swaped ", coords1, coords2)

        # * is also an unpack operator, *(x, y) -> x, y
        w1 = self.grid_layout.itemAtPosition(*coords1).widget()
        w2 = self.grid_layout.itemAtPosition(*coords2).widget()

        # Swap:
        self.pieces[coords1[0]][coords1[1]], self.pieces[coords2[0]][coords2[1]] = \
            self.pieces[coords2[0]][coords2[1]], self.pieces[coords1[0]][coords1[1]]

        self.update_board()
        w1.coords = coords2
        w2.coords = coords1
        w1.update()
        w2.update()
        self.change_turn()

    def change_images(self):
        for row in self.pieces:
            for piece in row:
                if not isinstance(piece, Blank):
                    piece.image_path = f"./images/{self.piece_set}/{piece.image_path[-2:]}"
                    piece.image = QPixmap(piece.image_path)

    def game_over(self, winner: str):
        QMessageBox.about(self, "Game over", winner)
        self.reset_board()
