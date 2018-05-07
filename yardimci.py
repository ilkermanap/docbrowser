from PyQt5.QtWidgets import QDialog, QApplication
from ui_ekran import Ui_yardimci
import pkgutil
import importlib
import sys

def hatali(hata):
    print( hata)
    print( "hata oldu")

class MainWindow(QDialog, Ui_yardimci):
    def __init__(self, app=None):
        super(MainWindow, self).__init__()
        self.app = app
        self.modul = None        
        self.setupUi(self)
        self.modul_listesi = []
        self.moduller()
        self.show()

    def arama(self):
        ara = self.editModul.text().strip()
        if ara == "":
            pass
        else:
            self.listModuller.clear()
            for modul in self.modul_listesi:
                if modul.find(ara) > -1:
                    self.listModuller.addItem(modul)
        
    def moduller(self):
        for modul_adi in pkgutil.walk_packages(onerror=hatali):
            self.modul_listesi.append(modul_adi[1])
            self.listModuller.addItem(modul_adi[1])
        
    def modulsec(self):
        secilen = self.listModuller.currentItem().text()
        self.listModul.clear()
        try:
            self.modul = importlib.import_module(secilen, secilen)
            for icerik in  dir(self.modul):
                self.listModul.addItem(icerik)                                              
        except:
            print( "modul yok")
        pass
        
    def detay(self):
        secilen = self.listModul.currentItem().text()
        nesne = getattr(self.modul, secilen)
        self.editTip.setText(str(type(nesne)))
        self.textYardim.setPlainText(nesne.__doc__)

        
    def doldur(self):
        self.listModul.clear()
        try:
            self.modul = __import__(self.editModul.text())
            for icerik in  dir(self.modul):
                self.listModuller.addItem(icerik)                                              
        except:
            print( "modul yok")
           
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow(app)
    sys.exit(app.exec_())
 
