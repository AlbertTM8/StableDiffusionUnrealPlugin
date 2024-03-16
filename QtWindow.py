import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QLabel
from PySide6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input & Generate Example")
        self.resize(600, 600)

        # self.imagePath = image_path

        # Central widget and layout
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)

        # LineEdit for input
        self.lineEdit = QLineEdit(self)
        layout.addWidget(self.lineEdit)


        # Button to generate output
        self.generateButton = QPushButton("Generate", self)
        layout.addWidget(self.generateButton)
        # self.generateButton.clicked.connect(self.generateClicked)

        # Label for displaying the image
        self.imageLabel = QLabel(self)
        layout.addWidget(self.imageLabel)
        
    # def generateClicked(self):
    #     if self.imagePath:
    #         pixmap = QPixmap(self.imagePath)
    #         self.imageLabel.setPixmap(pixmap)
    #         self.imageLabel.adjustSize()
    #         print(self.imagePath)


def run_gui_app():
    app = QApplication.instance()
    if not app:  # if it does not exist then create a new instance
        app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_gui_app()