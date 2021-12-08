import sys
import time
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from os.path import exists
## Importing Necessary Modules

file_exists = exists('./UI/blue screen.jpg')

if file_exists:
  pass

else:
  print("You are missing a required file, please download it from https://imgur.com/PWP7j5Q and put that file in th UI folder or the gitbub repository")
  exit()

def blue():
	print("Deleting Partitions...")
	time.sleep(1)
	print("Formating hard Disk...")
	time.sleep(2)
	app = QGuiApplication(sys.argv)
	engine = QQmlApplicationEngine()
	engine.quit.connect(app.quit)
	engine.load('./UI/main.qml')
	sys.exit(app.exec())

print("Warning, all inputs must be lowercase otherwise they will be marked wrong\n")

misspell = input("Please spell /misˈspel/, the words are phonetic so you cant cheat\n");


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

