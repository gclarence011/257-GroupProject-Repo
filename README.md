# AI Image Detection Application

A full-stack application that detects whether an image is AI-generated using a pre-trained deep learning model.

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

