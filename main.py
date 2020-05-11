import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow ,QLabel

if __name__ == '__main__':
    
    application = QApplication(sys.argv)
    
    w =QMainWindow()
    w.setGeometry(200,200,800,600)
    w.setWindowTitle('Random Generator')
    label_bonjour = QLabel('Bonjour, bienvenue sur mon programme ')
    w.show()

    
    sys.exit(application.exec_())

