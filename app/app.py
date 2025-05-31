from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os

app = Flask(__name__)

# Load the trained model  
model = tf.keras.models.load_model('weapon_classification_model.h5')

def preprocess_image(image):
    image = image.resize((256, 256))
    
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    image_array = image_array / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    
    return image_array

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image uploaded'}), 400
        
        image_file = request.files['image']
        
        image = Image.open(io.BytesIO(image_file.read()))
        processed_image = preprocess_image(image)
        
        prediction = model.predict(processed_image)
        
        prediction_class = 'Weapon detected' if prediction[0][0] > 0.5 else 'No Weapon detected'
        
        return jsonify({
            'class': prediction_class,
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)