import sys
import time
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally

## Set up the image URL and filename
image_url = "https://imgur.com/3VNVbnA"
filename = image_url.split("/")[-1]

# Open the url image, set stream to True, this will return the stream content.
r = requests.get(image_url, stream = True)

# Check if the image was retrieved successfully
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True
    
    # Open a local file with wb ( write binary ) permission.
    with open('UI/blue screen.jpg','wb') as f:
        shutil.copyfileobj(r.raw, f)
        
    print('Image sucessfully Downloaded: ',filename)
else:
    print('Image Couldn\'t be retreived')
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

misspell = input("Please spell /misˈspel/, the words are phonetic so you cant cheat\n");

if misspell == "misspell":
	pharaoh = input("Yay you did it, lets move on to a harder one, please spell /ˈferō/\n");
  
	if pharaoh == "pharaoh":

		weird = input("Please spell /wird/\n");
		if weird == "weird":
			print("L")

    

	else:
		blue()

else:
	blue()

