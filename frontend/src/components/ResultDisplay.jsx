import React from 'react';
import './ResultDisplay.css';

function ResultDisplay({ result }) {
  const { percentage, isAIGenerated, confidence } = result;
  const displayText = isAIGenerated ? 'AI-Generated' : 'Real Image';
  const displayIcon = isAIGenerated ? '🤖' : '✓';
  const resultClass = isAIGenerated ? 'ai-generated' : 'real-image';

  return (
    <div className="result-container">
      <div className={`result-card ${resultClass}`}>
        <div className="result-icon">{displayIcon}</div>
        
        <div className="result-title">{displayText}</div>
        
        <div className="percentage-display">
          <div className="percentage-value">{percentage.toFixed(1)}%</div>
          <div className="percentage-label">AI-Generated Probability</div>
        </div>

      </div>
    </div>
  );
}

export default ResultDisplay;
