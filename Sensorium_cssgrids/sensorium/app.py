from flask import Flask, render_template, url_for, request
app = Flask (__name__)

@app.route ('/')
def home ():
	return render_template ('index.html')



@app . route ('/force404 ')
def force404 ():
	abort (404)

@app . errorhandler (404)
def page_not_found ( error ):
	return render_template ('error.html')

@app.route ('/kids')
def kids ():
	return render_template ('kids.html')



if __name__ == (" __main__ "):
 app.run( host ='0.0.0.0 ', debug = True )
