import React, { useState } from 'react';

function AnalysisConfig() {
  const [category, setCategory] = useState('< 100');
  const [resultCount, setResultCount] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleRunAnalysis = async () => {
    setLoading(true);
    setResultCount(null); // Reset previous results

    try {
      const response = await fetch('https://postgresql-test-vcsu.onrender.com:8000/api/run-analysis/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ category: category }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      setResultCount(data.count);
    } catch (error) {
      console.error('Error running analysis:', error);
      alert('Failed to run analysis. Check console for details.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h2>Analysis Configuration</h2>
      <hr />
      
      <div style={{ marginBottom: '15px' }}>
        <label htmlFor="category-select" style={{ marginRight: '10px', fontWeight: 'bold' }}>
          Select Value Category:
        </label>
        <select
          id="category-select"
          value={category}
          onChange={(e) => setCategory(e.target.value)}
          style={{ padding: '5px', fontSize: '16px' }}
        >
          <option value="< 100">&lt; 100</option>
          <option value=">= 100">&gt;= 100</option>
        </select>
      </div>

      <button
        onClick={handleRunAnalysis}
        disabled={loading}
        style={{
          padding: '8px 16px',
          fontSize: '16px',
          backgroundColor: '#007bff',
          color: 'white',
          border: 'none',
          borderRadius: '4px',
          cursor: loading ? 'not-allowed' : 'pointer'
        }}
      >
        {loading ? 'Running...' : 'Run Analysis'}
      </button>

      {resultCount !== null && (
        <div style={{ marginTop: '20px', padding: '15px', backgroundColor: '#f8f9fa', borderRadius: '4px' }}>
          <h3>Analysis Results</h3>
          <p>
            Total cases fitting <strong>{category}</strong>: <span>{resultCount}</span>
          </p>
        </div>
      )}
    </div>
  );
}

export default AnalysisConfig;