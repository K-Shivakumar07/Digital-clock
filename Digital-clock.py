#Python PyQt5 DigitalClock
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,QPushButton, QTimeEdit

from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600,400,300,100)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        
        self.time_label.setAlignment(Qt.AlignCenter)
        
        self.time_label.setStyleSheet("font-size:150px;"
                                      
                                      "color:hsl(111, 100%, 50%);")
        
        self.setStyleSheet("background-color:black;")
        
        font_id = QFontDatabase.addApplicationFont("GUI/DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)
        
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        
        self.update_time()
        
    def update_time(self):
        current_time = QTime.currentTime()
        self.time_label.setText(current_time.toString("hh:mm:ss AP"))
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
    