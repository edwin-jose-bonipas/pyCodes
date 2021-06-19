from PyQt5.QtWidgets import QApplication, QMessageBox
import clipboard
import os
import sys
import time

clear = ""
clipboard.copy(clear)

app = QApplication(sys.argv)
msg = QMessageBox()

while True:
    data = clipboard.paste()
    time.sleep(0.5)
    if data != clear:
        last = data
        with open("clippy.py", 'w+') as cbpy:
            cbpy.write(data)
        status = os.system("python3 clippy.py > out")
        clipboard.copy(clear)
        if status == 0:
            with open("out", 'r') as fo:
                odata = fo.read()
            msg.setText("="*len(odata) + "\n"+ odata + "="*len(odata))
            msg.setFocus()
            msg.setWindowTitle("Output")
            msg.exec()











