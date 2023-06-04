import chess
import chess.svg
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QDialog
from PyQt5.QtSvg import QSvgWidget
from anki.hooks import addHook as A

class C(QDialog):
    def __init__(self, p=None):
        super().__init__(p)
        self.setWindowTitle("Chess Visualizer")
        self.l = QVBoxLayout(self)
        self.s = QSvgWidget()
        self.l.addWidget(self.s)

    def show(self, c):
        b = chess.Board()
        for m in c.split():
            b.push(chess.Move.from_uci(m))
        s = chess.svg.board(board=b)
        self.s.load(s)
        self.s.show()

def v(b):
    n = b.selectedNotes()
    if not n: return
    f = "chess_log"
    c = b.mw.col.getNote(n[0]).get(f, "")
    d = C(b)
    d.show(c)
    q = QApplication.instance()
    if not q: q = QApplication([])
    q.exec_()

A("browser.setupMenus", v)
