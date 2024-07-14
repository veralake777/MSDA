"""Flask App Project."""

from flask import Flask, render_template, request

from model import get_prediction

app = Flask(__name__, template_folder='./templates')


@app.route('/')
def index():
    """Return homepage."""
    return render_template('index.html')


@app.route("/process", methods=["GET", "POST"])
def process_form():
    formData = request.values if request.method == "GET" else request.values
    user_input = []
    for item in formData.items():
        user_input.append(item[1])


    # return response
    response = get_prediction(user_input)
    print(user_input)
    if response == '2':
        return render_template('rating.html', rating='AVERAGE')
    elif response == '1':
        return render_template('rating.html', rating='POOR')
    elif response == '3':
        return render_template('rating.html', rating='EXCELLENT')
    else:
        return render_template('rating.html', rating='Something went wrong. Please try again.')


if __name__ == '__main__':
    app.debug = True
    app.run()
