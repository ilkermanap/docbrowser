from PyQt5.QtWidgets import QDialog, QApplication
from ui_ekran import Ui_yardimci

import sys

class MainWindow(QDialog, Ui_yardimci):
    def __init__(self, app=None):
        super(MainWindow, self).__init__()
        self.app = app
        self.modul = None
        self.setupUi(self)
        self.show()

    def detay(self):
        secilen = self.listModuller.currentItem().text()
        nesne = getattr(self.modul, secilen)
        self.editTip.setText(str(type(nesne)))
        self.textYardim.setPlainText(nesne.__doc__)
        
    def doldur(self):
        self.listModuller.clear()
        try:
            self.modul = __import__(self.editModul.text())
            for icerik in  dir(self.modul):
                self.listModuller.addItem(icerik)                                              
        except:
            print "modul yok"
           
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow(app)
    sys.exit(app.exec_())
 
