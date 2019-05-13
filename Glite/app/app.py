from flask import Flask, render_template, request, session, g, url_for, redirect
from flask_cors import CORS
from models import create_post, create_post2, create_post3, create_post4, get_posts, get_posts2, get_posts3, get_posts4
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

CORS(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        session.pop('user', None)

        if request.form['password'] == 'glite2018':
            session['user'] = request.form['username']
            return redirect(url_for('chatrooms'))

                
    return render_template('home.html')



@app.route('/chat', methods=['GET', 'POST'])
def chat():

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        #name = request.form.get('name')
        name = session['user']
        post = request.form.get('post')
        create_post(name, post)

    posts = get_posts()
    if g.user:
        return render_template('chat.html', posts=posts)

    return redirect(url_for('home'))



@app.route('/chat2', methods=['GET', 'POST'])
def chat2():

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        #name = request.form.get('name')
        name = session['user']
        post2 = request.form.get('post2')
        create_post2(name, post2)

    posts2 = get_posts2()
    if g.user:
        return render_template('chat2.html', posts2=posts2)

    return redirect(url_for('home'))


@app.route('/chat3', methods=['GET', 'POST'])
def chat3():

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        #name = request.form.get('name')
        name = session['user']
        post3 = request.form.get('post3')
        create_post3(name, post3)

    posts3 = get_posts3()
    if g.user:
        return render_template('chat3.html', posts3=posts3)

    return redirect(url_for('home'))


@app.route('/chat4', methods=['GET', 'POST'])
def chat4():

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        #name = request.form.get('name')
        name = session['user']
        post4 = request.form.get('post4')
        create_post4(name, post4)

    posts4 = get_posts4()
    if g.user:
        return render_template('chat4.html', posts4=posts4)

    return redirect(url_for('home'))





@app.route('/account/', methods=['POST','GET'])
def account():
	if request.method == 'POST':
		return render_template('account.html', name = request.form['name'])

	else:

	    return render_template('accountget.html')



@app.route('/chatrooms')
def chatrooms():
    if g.user:
        return render_template('chatrooms.html')
    return redirect(url_for('home'))



@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']

    return 'Not logged in!'

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return render_template('dropsession.html')

@app.route ('/force404')
def force404 ():
	abort (404)

@app.errorhandler (404)
def page_not_found ( error ):
	return render_template ('error.html')

if __name__ == '__main__':
    app.run(debug=True)
