from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f'Name: {name}')
        print(f"Email: {email}")
        print(f"Message: {message}")
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)