from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtGui import QPainter, QPen, QBrush
from PySide6.QtCore import Qt, QRectF

CELL = 30
STONE_MARGIN = 4

class Gomoku:
  def __init__(self, size=9, st="pvp"):
    self.size = size
    self.t = 1  # 1 = X, 0 = O
    self.type = 1 if st == "pvp" else 2
    self.board = [["_" for _ in range(self.size)] for _ in range(self.size)]

  def make_move(self, r, c):
    if r >= self.size or c >= self.size:
      return False
    if self.board[r][c] != '_':
      return False
    self.board[r][c] = 'X' if self.t else 'O'
    self.t = (self.t + 1) % 2
    return True

  def check_win_after(self, r, c):
    t = 'O' if self.t == 1 else 'X'
    for dx in [-1, 0, 1]:
      for dy in [-1, 0, 1]:
        if dx == 0 and dy == 0:
          continue
        cnt = 0
        x1, y1 = r, c
        x2, y2 = r, c
        while 0 <= x1 < self.size and 0 <= y1 < self.size and self.board[x1][y1] == t:
          cnt += 1
          x1 += dx
          y1 += dy

        while 0 <= x2 < self.size and 0 <= y2 < self.size and self.board[x2][y2] == t:
          cnt += 1
          x2 -= dx
          y2 -= dy

        if cnt >= 6:
          return True
    return False

class GomokuBoard(QWidget):
  def __init__(self, game):
    super().__init__()
    self.game = game
    self.size = game.size

    px = self.size * CELL
    self.setFixedSize(px, px)
    self.setWindowTitle("Gomoku - PySide6")

  def paintEvent(self, event):
    qp = QPainter(self)
    qp.setRenderHint(QPainter.Antialiasing)

    # Draw grids
    qp.setPen(QPen(Qt.black, 1))
    for i in range(self.size):
      y = i * CELL + CELL/2
      qp.drawLine(CELL/2, y, self.size*CELL - CELL/2, y)
      x = i * CELL + CELL/2
      qp.drawLine(x, CELL/2, x, self.size*CELL - CELL/2)

    # Draw stones
    for r in range(self.size):
      for c in range(self.size):
        v = self.game.board[r][c]
        if v == '_':
          continue
        cx = c*CELL + CELL/2
        cy = r*CELL + CELL/2
        if v == 'X':
          qp.setBrush(QBrush(Qt.black))
        else:
          qp.setBrush(QBrush(Qt.white))

        radius = CELL/2 - STONE_MARGIN
        qp.drawEllipse(QRectF(cx - radius, cy - radius, radius*2, radius*2))

  def mousePressEvent(self, event):
    if event.button() != Qt.LeftButton:
      return

    c = event.position().x() // CELL
    r = event.position().y() // CELL
    if not self.game.make_move(int(r), int(c)):
      return

    # Check win
    if self.game.check_win_after(int(r), int(c)):
      self.update()
      winner = "O" if self.game.t == 1 else "X"
      QMessageBox.information(self, "Game Over", f"{winner} wins!")
      self.setEnabled(False)
      return

    self.update()

if __name__ == "__main__":
  from sys import exit
  from sys import argv
  app = QApplication(argv)
  game = Gomoku(9)  # board size as an argument
  window = GomokuBoard(game)
  window.show()

  exit(app.exec())