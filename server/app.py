from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        image = request.files['image']
        remove_background = request.form.get('remove_background') == 'true'
        seed = int(request.form.get('seed', 0))
        sample_steps = int(request.form.get('sample_steps', 1))

        # Process image and generate mesh here
        # Placeholder for processing function
        # result = process_image(image, remove_background, seed, sample_steps)

        return jsonify({'message': 'Image processed successfully'})


if __name__ == "__main__":
    app.run(debug=True)
