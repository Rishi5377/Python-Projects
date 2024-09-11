#PYTHON DIGITAL CLOCK
import sys
from PyQt5.QtCore import Qt,QTime,QTimer
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtGui import QFont,QFontDatabase

    #CREATE A CONSTRUCTOR

class Digital_Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)

        self.initUI()

    #  USER INTERFACE

    def initUI(self):
        self.setWindowTitle("DIGITAL CLOCK")
        self.setGeometry(375,275,600,200)
        self.setStyleSheet("background : black;")
        #CREATE A TIME LABEL FIRST
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        #CUSTOMIZE IT 
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size : 135px;"
                                      "color : hsl(111, 100%, 50%);"
                                    )
        # TO ADD NEW DESIGN OR FONT TO THE NUMBERS IN THE CLOCK
        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family,150)
        self.time_label.setFont(my_font)
        #TO UPDATE THE TIME IN THE CLOCK
        self.timer.timeout.connect(self.Update_Clock)
        self.timer.start(1000)

        self.Update_Clock()

        #    

    def Update_Clock(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

def main():
    app = QApplication(sys.argv)
    window = Digital_Clock()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()