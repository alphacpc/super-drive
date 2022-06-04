from flask import Flask, render_template

app = Flask(__name__)





@app.route("/")
def home():
    return render_template('pages/home.html')




@app.route("/connexion/")
def login():
    return render_template('pages/login.html')




@app.route("/inscription/")
def register():
    return render_template('pages/register.html')





# @app.errorhandler(404)
# def not_found(error):
#     return render_template('pages/not_found.html'),404





if __name__=='__main__':
    app.run(debug=True,port=5000)