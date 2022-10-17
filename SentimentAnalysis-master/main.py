from flask import Flask,render_template,request,redirect,session

from sentiments import second
import os

app=Flask(__name__)
app.secret_key=os.urandom(24)
app.register_blueprint(second)



@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/home',methods=['POST'])
def Home():
    print('function calling is working...')
    return render_template('home.html')

    # else:
    #     return redirect('/')





if __name__=="__main__":
    app.run(debug=True)