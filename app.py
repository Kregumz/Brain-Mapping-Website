from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/home')
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
	return render_template('faq.html')

@app.errorhandler(404)
def page_not_found(e):
	 return render_template('404.html'), 404


if __name__ == "__main__":
    app.run()
