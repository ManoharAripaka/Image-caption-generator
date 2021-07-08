from flask import Flask, render_template, redirect, request
import Caption
from gtts import gTTS
from time import sleep
import os
app = Flask(__name__)

@app.route('/')
def hello():
	return render_template("index.html")

@app.route('/', methods= ['POST'])
def fun():
	if request.method == 'POST':
		f = request.files['userfile']
		path = "./static/{}".format(f.filename)
		if (path != './static/'):
			f.save(path)
			caption = Caption.tempo(path)
			temp=caption.split()
			temp.pop(0)
			temp.pop(-1)
			tex=""
			for i in temp:
				tex=tex+i+" "
			myobj = gTTS(text=tex, lang='en', slow=False )
			sleep(5)
			myobj.save("./static/welcome.mp3")
			myobj.save("./static/welcome.mp3")
			aud='./static/welcome.mp3'
			print(aud)
			print(path)
			print(f)
			return render_template("index.html", yourCaption=tex, loc=path, audio=aud)
		else:
			return render_template("index.html")


if __name__ == '__main__':
	app.run(debug = True)