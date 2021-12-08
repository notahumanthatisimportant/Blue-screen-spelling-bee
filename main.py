import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

def blue():
	app = QGuiApplication(sys.argv)
	engine = QQmlApplicationEngine()
	engine.quit.connect(app.quit)
	engine.load('./UI/main.qml')
	sys.exit(app.exec())

misspell = input("Please spell /misˈspel/, the words are phonetic so you cant cheat\n");

if misspell == "misspell":
	pharaoh = input("Yay you did it, lets move on to a harder one, please spell /ˈferō/\n");
  
	if pharaoh == "pharaoh":
		weird = input("Please spell /wird/\n");
	  
    if weird == "weird":
      print("just a couple more")
    
    else:
	    blue

	else:
		blue()

else:
	blue()

def blue():
	app = QGuiApplication(sys.argv)
	engine = QQmlApplicationEngine()
	engine.quit.connect(app.quit)
	engine.load('./UI/main.qml')
	sys.exit(app.exec())