import React, { useState } from 'react';
import './App.css';
import ImageUploader from '../../frontend/src/components/ImageUploader';
import ResultDisplay from '../../frontend/src/components/ResultDisplay';

function App() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleUpload = async (file) => {
    setLoading(true);
    setError(null);
    setResult(null);

    const formData = new FormData();
    formData.append('image', file);

    try {
      const response = await fetch('http://localhost:5010/predict', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }

      const data = await response.json();
      
      if (data.success) {
        setResult({
          percentage: data.ai_generated_percentage,
          isAIGenerated: data.is_ai_generated,
          confidence: data.confidence,
        });
      } else {
        setError(data.error || 'Unknown error occurred');
      }
    } catch (err) {
      setError(err.message || 'Failed to connect to server. Make sure the backend is running.');
      console.error('Upload error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>🤖 AI Image Detector</h1>
        <p>Upload an image to detect if it's AI-generated</p>
      </header>
      
      <main className="App-main">
        <ImageUploader onUpload={handleUpload} disabled={loading} />
        
        {loading && <div className="loading">Analyzing image...</div>}
        
        {error && <div className="error-message">❌ {error}</div>}
        
        {result && <ResultDisplay result={result} />}
      </main>

      <footer className="App-footer">
        <p>Backend: http://localhost:5000</p>
      </footer>
    </div>
  );
}

export default App;
