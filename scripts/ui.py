from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtWidgets import QApplication
from scripts.file_operations import FileOperations
import sys
import filetype


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        self.setWindowTitle("Randomize Hex")
        self.setGeometry(100, 100, 400, 200)

        self.label_hex_digits = QLabel("Hex digits:", self)
        self.label_hex_digits.move(20, 20)
        self.label_hex_digits.resize(120, 30)

        self.input_hex_digits = QLineEdit(self)
        self.input_hex_digits.move(140, 20)
        self.input_hex_digits.resize(120, 30)

        self.label_random_chance = QLabel("Random chance:", self)
        self.label_random_chance.move(20, 52)
        self.label_random_chance.resize(120, 30)

        self.input_random_chance = QLineEdit(self)
        self.input_random_chance.move(140, 52)
        self.input_random_chance.resize(120, 30)

        self.label_header_size = QLabel("Header size:", self)
        self.label_header_size.move(20, 84)
        self.label_header_size.resize(120, 30)

        self.input_header_size = QLineEdit(self)
        self.input_header_size.move(140, 84)
        self.input_header_size.resize(120, 30)

        self.label_file_path = QLabel("File Path:", self)
        self.label_file_path.move(20, 116)
        self.label_file_path.resize(120, 30)

        self.input_file_path = QLineEdit(self)
        self.input_file_path.move(140, 116)
        self.input_file_path.resize(120, 30)

        self.button_browse = QPushButton("Browse", self)
        self.button_browse.move(265, 116)
        self.button_browse.clicked.connect(self.browse_file)

        self.button_randomize = QPushButton("Randomize", self)
        self.button_randomize.move(20, 150)
        self.button_randomize.clicked.connect(self.randomize_hex)

        self.file_operations = FileOperations()

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
        self.input_file_path.setText(file_path)

    def randomize_hex(self):
        _hex_digits = self.input_hex_digits.text()
        _random_chance = int(self.input_random_chance.text())
        _header_size = int(self.input_header_size.text())
        file_path = self.input_file_path.text()

        with open(file_path, 'rb') as f:
            video_content = f.read()

        hex_content = video_content.hex()
        content_randomized = [hex_content[i:i + 2] for i in range(0, len(hex_content), 2)]
        randomized_content = self.file_operations.randomize_content(content_randomized, _random_chance)

        kind = filetype.guess(file_path)
        if kind is None:
            QMessageBox.critical(self, "Error", "Unable to determine file type.")
            return

        file_extension = kind.extension
        file_mime_type = kind.mime

        save_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", f"{file_mime_type} (*.{file_extension})")
        if save_path:
            try:
                self.file_operations.write_content_to_file(randomized_content, save_path)
                QMessageBox.information(self, "Success", "File saved successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec_())
