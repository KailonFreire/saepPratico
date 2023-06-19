from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from detalhes import DetalhesWindow

class MenuWindow(QMainWindow):
  def __init__(self, parent = None, session = None):
    super(MenuWindow, self).__init__(parent)
    uic.loadUi('telas/inicial.ui', self)

    self.session = session
    self.parent = parent

    self.btnSaque.clicked.connect(self.openSaque)
    self.btnSair.clicked.connect(self.encerrarSessao)
    self.btnManutencao.clicked.connect(self.openManutencao)
    
    self.botoes = [
            self.btnArea1,
            self.btnArea2,
            self.btnArea3,
            self.btnArea4,
            self.btnArea5,
            self.btnArea6,
            self.btnArea7,
            self.btnArea8,
            self.btnArea9,
            self.btnArea10,
            self.btnArea11,
    ]
    
    self.chamarBotoes()

def chamarBotoes(self):
    for i in range(len(self.botoes)):
        self.botoes[i].clicked.connect(lambda checked, i=i: self.mostrarDetalhes(i + 1))
        