
from flask import Flask,render_template, request
app= Flask(__name__)
@app.route('/')
def f():
    return render_template('temp.html')

@app.route('/submit', methods=["POST"])
def display():
    Name = request.form.get('Name')
    email = request.form.get('email')
    return render_template("hello.html", Name=Name, email=email)
    
if __name__=='__main__':
    app.run(debug=True, port=8000)
    
