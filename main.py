from PyQt5 import QtWidgets
import sys
import os
os.environ["QT_LOGGING_RULES"] = "*.debug=false;qt.qpa.*=false"
from load.load_ui_login import Load_ui_login
from load.load_ui_productos import Load_ui_productos
from load.load_ui_menu import Load_ui_menu

def main():
    app = QtWidgets.QApplication(sys.argv)
    while True:
        window_login = Load_ui_login()

        if window_login.exec_() == QtWidgets.QDialog.Accepted:
            window_menu = Load_ui_menu()
            window_menu.show()
            app.exec_()
        else:
            break

    sys.exit()
    
if __name__ == "__main__":
    main()



