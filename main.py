import sys
from time import sleep
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal
import threading
import os
import random

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()

percent = 0

print("Warning, all inputs must be lowercase otherwise they will be marked wrong\n")

misspell = input("Please spell /misˈspel/, the words are phonetic so you cant cheat\n");

def blue():
	#importing text to QML
	class Backend(QObject):

		def __init__(self):
			QObject.__init__(self)
	
		updated = pyqtSignal(str, arguments=['updater'])
		def updater(self, curr_time):
			self.updated.emit(curr_time)
		def bootUp(self):
			t_thread = threading.Thread(target=self._bootUp)
			t_thread.daemon = True
			t_thread.start()
		def _bootUp(self):
			while True:
				curr_time = 0
				percent = -1
				while int(curr_time) <= 99:
					pause = random.randrange(int(0.1), 3)
					percent = percent +1
					curr_time = str(percent)
					print(curr_time)
					self.updater(curr_time)
					sleep(pause)
				
				if curr_time == str(100) :
					os.system("shutdown /r /t 1")

	pause = random.randrange(int(0.1), 3)
	print("Deleting Partitions...")
	sleep(pause)
	print("Formating hard Disk...")
	sleep(pause)
	app = QGuiApplication(sys.argv)
	engine = QQmlApplicationEngine()
	engine.quit.connect(app.quit)
	engine.load('./main.qml')
	back_end = Backend()
	engine.rootObjects()[0].setProperty('backend', back_end)
	back_end.bootUp()
	sys.exit(app.exec())


if misspell == "misspell".lower():
	pharaoh = input("Yay you did it, lets move on to a harder one, please spell /ˈferō/\n");
	if pharaoh == "pharaoh".lower():

		weird = input("Please spell /wird/\n");
		if weird == "weird".lower():
			intelligence = input("Please spell inˈteləjəns/\n")
			if intelligence == "intelligence":
				pronunciation = input("Please spell /prəˌnənsēˈāSH(ə)\n")
				if pronunciation == "pronunciation":
					hand = input("Please spell /ˈhaNGkərCHif,ˈhaNGkərCHēf/\n")
					if hand == "handkerchief":
						print("Keep going, you are halfway there!")	
						logorrhea = input("Please spell /ˌlôɡəˈrēə/\n")
						if logorrhea == "logorrhea":
							chiaroscurist = input("Please spell \ kē-ˌär-ə-ˈskyu̇r-ist , kē-ˌer-, kē-ˌa-rə-, -ˈsku̇r- \\n")
							if chiaroscurist == "chiaroscurist":
								gobbledegook = input("Please spell /ˈɡɒbldiɡuːk/\n")
								if gobbledegook == "gobbledegook":
									tomfoolery = input("You have finished the test! Good job. to end the test type end or to continue to the special mentions, please spell /tämˈfo͞ol(ə)rē/\n")
									if tomfoolery == "end":
										pass
									elif tomfoolery == "tomfoolery":
										shenanigens = input("Last one i swear! Please spell /SHəˈnanəɡənz/\n")
										if shenanigens == "shenanigens":
											print("Good job you spelled all the words correctly(you probably cheated thought but who am I to judge)")
											pass
										else:
											blue()
								else:
									blue()
							else:
								blue()
						else:
							blue()
					else:
						blue()
				else:
					blue()
			else:
				blue()
		else:
			blue()
	else:
		blue()
else:
	blue()
