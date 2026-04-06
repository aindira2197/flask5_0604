from flask import Flask, render_template

app = Flask(__name__)

@app.route('/password')
def password_page():
    password = "hello"

    length = len(password)

    if length < 6:
        status = "Zaif parol"
        color = "red"
    elif 6 <= length <= 10:
        status = "O'rtacha parol"
        color = "orange"
    else:
        status = "Kuchli parol"
        color = "green"

    return render_template("password.html", status=status, color=color)

if __name__ == '__main__':
    app.run(debug=True)
