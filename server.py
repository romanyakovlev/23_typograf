from flask import Flask, render_template, request, abort
from typograf import format_text


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def start_page():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        original_text = request.form['text']
        if type(original_text) != str:
            abort(403)
        formatted_text = format_text(original_text)
        return formatted_text


if __name__ == "__main__":
    app.run()
