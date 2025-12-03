import os
import numpy as np
from PIL import Image
from io import BytesIO
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import tensorflow as tf

load_dotenv()

app = Flask(__name__)
CORS(app)

# Configuration
MODEL_PATH = os.getenv('MODEL_PATH', './model.pth')
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Global model variable
model = None
device = None

def load_model():
    """Load the trained TensorFlow model"""
    global model
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        print("TensorFlow model loaded successfully")
        return True
    except Exception as e:
        print(f"Error loading TensorFlow model: {e}")
        return False

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(image_path):
    image = Image.open(image_path).convert('RGB').resize((32, 32))
    image = np.expand_dims(image, axis=0)
    return image

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'model_loaded': model is not None}), 200

@app.route('/predict', methods=['POST'])
def predict():
    """Predict if image is AI-generated"""
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500
    
    # Check if image is in request
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    file = request.files['image']
    
    if file.filename == '':
        return jsonify({'error': 'No image selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type. Allowed: ' + ', '.join(ALLOWED_EXTENSIONS)}), 400
    
    try:
      image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
      file.save(image_path)

      image_tensor = preprocess_image(image_path)
      output = model.predict(image_tensor)[0]

      # Determine probability
      if len(output) == 1:  # single output neuron (sigmoid)
          ai_generated_percentage = float(output[0] * 100)
      else:  # multi-class softmax, class 1 = AI image
          ai_generated_percentage = float(output[1] * 100)

      os.remove(image_path)

      return jsonify({
          'success': True,
          'ai_generated_percentage': round(100 - ai_generated_percentage, 2),
          'is_ai_generated': ai_generated_percentage < 50
      }), 200
    
    except Exception as e:
        # Clean up on error
        if os.path.exists(image_path):
            os.remove(image_path)
        return jsonify({'error': f'Prediction error: {str(e)}'}), 500

@app.route('/info', methods=['GET'])
def info():
    """Get API information"""
    return jsonify({
        'name': 'AI Image Detection API',
        'version': '1.0.0',
        'description': 'Detects if an image is AI-generated',
        'model_loaded': model is not None,
        'device': str(device),
        'allowed_formats': list(ALLOWED_EXTENSIONS)
    }), 200

if __name__ == '__main__':
    print("Loading model...")
    if load_model():
        print("Starting Flask server...")
        app.run(debug=True, port=5010, host='0.0.0.0')
    else:
        print("Failed to load model. Please check MODEL_PATH in .env file")
