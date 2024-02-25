from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon

class InterfaceBase(QWidget):
    def __init__(self, name, icon):
        super().__init__()

        self.setObjectName(name)
        self.icon = icon

class FFmpegInterface(InterfaceBase):
    def __init__(self):
        super().__init__("FFmpeg", FluentIcon.MOVIE)

class PacmanInterface(InterfaceBase):
    def __init__(self):
        super().__init__("Pacman", FluentIcon.APPLICATION)
