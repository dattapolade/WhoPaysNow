from flask import Flask, render_template, request
import random

app = Flask(__name__)

def select_person(names):
    if len(names) == 0:
        return "Please enter at least one name."
    else:
        random_person = random.choice(names)
        return f"{random_person} is going to pay the todays bill!"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        names_string = request.form['names']
        names = [name.strip() for name in names_string.split(",")]
        result = select_person(names)
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True, port=8000)