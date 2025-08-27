# Multithreading = threading.Thread(target=my_function), args=(tuple), import threading, thread1.start(), join()
# multitasking, main thread with other thread concurrently
# Python API request(import requests), install request package(pip install requests), request.get(), response.status_code ==

# Python Graphical User Interface, PyQt5(pip install PyQt5), import sys

import sys
from PyQt5.Qtwidgets import Qapplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().init()