import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os
import uuid

model = load_model('mobilenetv2_deepfake_model.h5')

def extract_frames(video_path, max_frames=5):
    cap = cv2.VideoCapture(video_path)
    frames = []
    saved_filenames = []
    count = 0
    while count < max_frames:
        ret, frame = cap.read()
        if not ret:
            break
        resized = cv2.resize(frame, (224, 224))
        frames.append(resized)

        # Save frame image for display
        filename = f"{uuid.uuid4().hex[:8]}.jpg"
        filepath = os.path.join('static', 'uploads', filename)
        cv2.imwrite(filepath, frame)
        saved_filenames.append(filename)

        count += 1
    cap.release()
    return np.array(frames), saved_filenames

def predict_deepfake(video_path):
    frames, frame_files = extract_frames(video_path)
    frames = frames / 255.0
    preds = model.predict(frames)
    avg_pred = np.mean(preds)
    label = "Deepfake" if avg_pred > 0.5 else "Real"
    confidence = round(float(avg_pred) * 100, 2)
    return label, confidence, frame_files
