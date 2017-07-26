# Interfile_Analysis_Tools.py
# A cross-platform, GUI based toolset, designed to visualise, analyse
# and process medical images, stored in interfile format
# By William Scott-Jackson

# This source file will serve as the entry point into the application

# TODO: Layout GUI for more effective use and conveyance of different anatomical planes
# TODO: Tools to manipulate viewing of the image
# TODO: Tools to quantitatively analyse the images
# TODO: Tools to manipulate and process the images

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500, 500)
    w.move(300,300)
    w.setWindowTitle('Interfile Analysis Tools')

    w.show()

    sys.exit(app.exec_())
    
