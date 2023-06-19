from model.inicial import InicialWindow
from PyQt5.QtWidgets import QApplication
import Helpers.database as database

def appStartup():
  database.start()
  
  app = QApplication([])
  tela = InicialWindow()
  app.exec_()

if __name__ == '__main__':
  appStartup()