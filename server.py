from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def format_text(original_text):
    #Logic for text formatting
    formatted_text = original_text
    return formatted_text

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        data_json = request.get_json()
        original_text = data_json['text_string']
        formatted_text = format_text(original_text)
        return jsonify(formatted_text=formatted_text)

if __name__ == "__main__":
    app.run()
