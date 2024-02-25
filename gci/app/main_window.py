from app.interface import FFmpegInterface, PacmanInterface

from qfluentwidgets import FluentWindow

class MainWindow(FluentWindow):

    def __init__(self):
        super().__init__()

        self.interfaces = []

        self.addInterface()
        self.initNavigation()

    def initNavigation(self):
        for interface in self.interfaces:
            self.addSubInterface(interface, interface.icon, interface.objectName())

    def addInterface(self):
        self.interfaces.append(FFmpegInterface())
        self.interfaces.append(PacmanInterface())
