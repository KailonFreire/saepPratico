from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from DetalhesWindow import DetalhesWindow

class MenuWindow(QMainWindow):
  def __init__(self, parent = None, session = None):
    super(MenuWindow, self).__init__(parent)
    uic.loadUi('telas/inicial.ui', self)

    self.session = session
    self.parent = parent

    self.btnSaque.clicked.connect(self.openSaque)
    self.btnSair.clicked.connect(self.encerrarSessao)
    self.btnManutencao.clicked.connect(self.openManutencao)