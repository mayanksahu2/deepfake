# 🔍 Deepfake Detection Web App

This is a deep learning-based web application built using **Flask** that detects whether a given video is real or fake (deepfake). It uses a fine-tuned **MobileNetV2** model to analyze video frames and provide predictions along with confidence scores.

---

## 🚀 Features

- Upload video and detect deepfakes
- Displays prediction result with confidence score
- Shows extracted frames from the uploaded video
- Clean and responsive UI (HTML + CSS)
- Ready for deployment

---

## 📂 Project Structure

deepfake_webapp/
├── static/
│ ├── style.css
│ └── frames/
├── templates/
│ └── index.html
├── app.py
├── mobilenetv2_deepfake_model.h5
└── README.md



---

## 🔧 Technologies Used

- Python 3.x
- Flask
- OpenCV
- TensorFlow / Keras
- HTML, CSS (for styling)

---

## 📁 Model & Test Videos

🔗 Model and sample test videos are hosted on Google Drive:

👉 [Download Model & Videos](https://drive.google.com/your-google-drive-link)

> Upload the `.h5` model in the root folder as `mobilenetv2_deepfake_model.h5` before running.

---

## 📸 Screenshots

Add your screenshots here:

| Upload Video | Prediction Result |
|--------------|-------------------|
| ![Upload](screenshots/upload.png) | ![Result](screenshots/result.png) |

---

## 🛠️ How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/your-username/deepfake.git
cd deepfake

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py

Visit http://localhost:5000 in your browser.




