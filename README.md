# AI Image Detection Application

A full-stack application that detects whether an image is AI-generated using a pre-trained deep learning model.
# Models 
Our code for training the models is in the models folder.
- KNN.ipynb : Our EDA on the images and the Training + Evaluation of the KNN model. (Gabriel)
- Logistic_regression .ipynb : Training and Evaluation of the Logistic Regression. (Soham)
- SVM.ipynb : Training and Evaluation of the SVM model. (Terin)
- XGBoost.ipynb : Training and Evaluation of the XGBoost. (Terin)
- cnn-model.ipynb : Training and Evaluation of the CNN. (Gabriel)
- svm.ipynb : The same SVM model and code but designed to run in kaggle to run the SHAP analysis (Gabriel)
- svm_pipeline_grid (1).joblib : The exported svm model
- xgb_model2.json : The exported XGBoost model

#Dataset
The dataset we used for this project is [CIFAKE](https://www.kaggle.com/datasets/birdy654/cifake-real-and-ai-generated-synthetic-images).

# DEMO

Demo link: https://youtu.be/lMtHq4mod6A

## 🚀 Quick Start

### Backend Setup

1. **Install Python dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Add your trained model:**
   - Place your trained model file as `backend/model.h5`
   - Update `MODEL_PATH` in `.env` if your model has a different name

3. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env to set MODEL_PATH if needed
   ```

4. **Run the backend:**
   ```bash
   python app.py
   ```
   Backend will be available at `http://localhost:5010`

### Frontend Setup

1. **Install dependencies:**
   ```bash
   cd frontend
   npm install
   ```

2. **Start the development server:**
   ```bash
   npm run dev
   ```
   Frontend will open at `http://localhost:3000`

