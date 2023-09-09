from PyQt5.QtWidgets import QApplication
from scripts.ui import UI
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec_())
