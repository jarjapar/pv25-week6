from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QSlider, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("F1D022072-M. Fajar Maulana")
        MainWindow.resize(550, 300)

        self.centralwidget = QWidget(MainWindow)
        self.layout = QVBoxLayout(self.centralwidget)

        self.displayLabel = QLabel("F1D022072")
        self.displayLabel.setAlignment(Qt.AlignCenter)
        self.displayLabel.setFont(QFont("Arial", 40))
        self.displayLabel.setStyleSheet("background-color: white; color: black;")
        self.layout.addWidget(self.displayLabel)

        self.fontSizeLayout = QHBoxLayout()
        self.fontSizeLabel = QLabel("Font Size")
        self.fontSizeSlider = QSlider(Qt.Horizontal)
        self.fontSizeSlider.setMinimum(20)
        self.fontSizeSlider.setMaximum(60)
        self.fontSizeSlider.setValue(40)
        self.fontSizeSlider.valueChanged.connect(self.changefont)
        self.fontSizeLayout.addWidget(self.fontSizeLabel)
        self.fontSizeLayout.addWidget(self.fontSizeSlider)
        self.layout.addLayout(self.fontSizeLayout)

        self.bgColorLayout = QHBoxLayout()
        self.bgColorLabel = QLabel("Background Color")
        self.bgColorSlider = QSlider(Qt.Horizontal)
        self.bgColorSlider.setMinimum(0)
        self.bgColorSlider.setMaximum(255)
        self.bgColorSlider.setValue(255)
        self.bgColorSlider.valueChanged.connect(self.changewarna)
        self.bgColorLayout.addWidget(self.bgColorLabel)
        self.bgColorLayout.addWidget(self.bgColorSlider)
        self.layout.addLayout(self.bgColorLayout)

        self.fontColorLayout = QHBoxLayout()
        self.fontColorLabel = QLabel("Font Color")
        self.fontColorSlider = QSlider(Qt.Horizontal)
        self.fontColorSlider.setMinimum(0)
        self.fontColorSlider.setMaximum(255)
        self.fontColorSlider.setValue(0)
        self.fontColorSlider.valueChanged.connect(self.changewarna)
        self.fontColorLayout.addWidget(self.fontColorLabel)
        self.fontColorLayout.addWidget(self.fontColorSlider)
        self.layout.addLayout(self.fontColorLayout)

        MainWindow.setCentralWidget(self.centralwidget)

    def changefont(self):
        font = self.displayLabel.font()
        font.setPointSize(self.fontSizeSlider.value())
        self.displayLabel.setFont(font)

    def changewarna(self):
        bg_val = self.bgColorSlider.value()
        font_val = self.fontColorSlider.value()
        bg_color = QColor(bg_val, bg_val, bg_val).name()
        font_color = QColor(font_val, font_val, font_val).name()
        self.displayLabel.setStyleSheet(f"background-color: {bg_color}; color: {font_color};")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
