import os
from flask import Flask, request, render_template
from model_utils import predict_deepfake

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'video' not in request.files:
        return "No file uploaded."

    video = request.files['video']
    path = os.path.join(UPLOAD_FOLDER, video.filename)
    video.save(path)

    result, confidence, frames = predict_deepfake(path)
    return render_template('result.html', result=result, confidence=confidence, frames=frames)

if __name__ == '__main__':
    app.run(debug=True)
