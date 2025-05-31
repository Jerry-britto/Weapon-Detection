# 🔫 Weapon Detection System using CNN and Flask

## 📌 Objective

The primary objective of this project is to develop a **Weapon Detection System** that can accurately identify whether an image contains a weapon or not. The system utilizes a **Convolutional Neural Network (CNN)** model for classification and is deployed using a **Flask web application**, providing an easy-to-use interface for end-users to upload images and receive detection results in real-time.

---

## 🌟 Features

- ✅ Detects presence or absence of weapons in uploaded images
- 🧠 CNN-based custom model for high accuracy
- 💻 Flask-powered lightweight web application
- 📤 Image upload interface
- ⚡ Real-time prediction
- 📊 Clean and organized codebase for easy understanding
- 🧪 Easily extendable for video surveillance integration

---

## 🧠 Model Architecture

- **Model Type:** Convolutional Neural Network (CNN)
- **Input Shape:** Preprocessed image (e.g., 128x128 or 224x224 pixels)
- **Layers:**
  - Convolutional Layers
  - Max Pooling Layers
  - Flatten Layer
  - Dense Layers
  - Dropout Layer
  - Output Layer with Softmax/Sigmoid Activation
- **Output Classes:** Weapon, No Weapon
- **Loss Function:** Binary Crossentropy
- **Optimizer:** Adam
- **Metrics:** Accuracy, Precision, Recall

---

## 🛠️ Implementation

### 1. Data Collection & Preprocessing
- Gathered a dataset of images containing weapons and non-weapons.
- Preprocessed images: resizing, normalization, and augmentation.
- Split into training, testing and validation sets.

### 2. Model Training
- Built and trained the CNN using TensorFlow/Keras.
- Evaluated performance using accuracy, precision, and recall.
- Saved the trained model using `model.save('weapon_detector.h5')`.

### 3. Flask Integration
- Created a Flask application to serve the model.
- Users can upload an image via a simple UI.
- The server loads the saved model, processes the image, and returns prediction results.

### 4. UI/UX
- HTML form with file input for image upload.
- Display area to show image and classification result.
- Error handling for invalid files or upload issues.

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Jerry-britto/Weapon-Detection.git
cd Weapon-Detection/app
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask App

```bash
python app.py
```

### 4. Access the Web Interface

Open your browser and go to: `http://127.0.0.1:5000`

---

## 🧪 Sample Usage

1. Open the web interface.
2. Upload an image.
3. Click the "Detect" button.
4. Get prediction result: “Weapon Detected” or “No Weapon Detected”.

---

## 🛡️ Use Cases

* Surveillance and security monitoring systems
* Crime prevention tools
* Restricted area monitoring (schools, airports, etc.)
* Law enforcement decision-support systems

---

## 📈 Future Enhancements

* Integrate with live video feed for real-time detection
* Add bounding box localization for weapon in the image
* Implement confidence score display
* Deploy to cloud (AWS/GCP/Azure)
* Mobile app integration using APIs




