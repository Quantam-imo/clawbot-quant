import React, { useState } from 'react';
import axios from 'axios';

// Use environment variable for API base URL, fallback to localhost
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';
import './App.css';

const panels = [
  { key: 'volume', label: 'Volume Profile' },
  { key: 'gann', label: 'Gann' },
  { key: 'astrology', label: 'Astrology' },
  { key: 'news', label: 'News' },
  { key: 'mentor', label: 'AI Mentor' }
];

function App() {
  const [activePanel, setActivePanel] = useState('volume');
  const [result, setResult] = useState('');
  const [symbol, setSymbol] = useState('AAPL');
  const [interval, setInterval] = useState('1d');
  const [newsSymbol, setNewsSymbol] = useState('AAPL');

  const handlePanel = async (key) => {
    setActivePanel(key);
    setResult('Loading...');
    try {
      if (key === 'volume') {
        const res = await axios.post(`${API_BASE_URL}/api/volume-profile`, { symbol, interval });
        if (res.data.error) {
          setResult('Error: ' + res.data.error);
        } else {
          setResult(JSON.stringify(res.data, null, 2));
        }
      } else if (key === 'gann') {
        const res = await axios.get(`${API_BASE_URL}/api/gann`);
        setResult(res.data.result);
      } else if (key === 'astrology') {
        const res = await axios.get(`${API_BASE_URL}/api/astrology`);
        setResult(res.data.result);
      } else if (key === 'news') {
        const res = await axios.post(`${API_BASE_URL}/api/news`, { symbol: newsSymbol });
        setResult(`${res.data.news}\nMarket Move: ${res.data.market_move}`);
      } else if (key === 'mentor') {
        const res = await axios.get(`${API_BASE_URL}/api/ai-mentor/volume`);
        setResult(res.data.text);
      }
    } catch (err) {
      if (err.response && err.response.data && err.response.data.error) {
        setResult('API Error: ' + err.response.data.error);
      } else if (err.message) {
        setResult('Network Error: ' + err.message);
      } else {
        setResult('Unknown error occurred.');
      }
    }
  };

  return (
    <div className="container">
      <h1>Clawbot Panel</h1>
      <div className="button-row">
        {panels.map(panel => (
          <button
            key={panel.key}
            className={activePanel === panel.key ? 'active' : ''}
            onClick={() => handlePanel(panel.key)}
          >
            {panel.label}
          </button>
        ))}
      </div>
      {activePanel === 'news' && (
        <div className="input-row">
          <input value={newsSymbol} onChange={e => setNewsSymbol(e.target.value)} placeholder="Symbol" />
        </div>
      )}
      {activePanel === 'volume' && (
        <div className="input-row">
          <input value={symbol} onChange={e => setSymbol(e.target.value)} placeholder="Symbol (e.g. AAPL)" />
          <input value={interval} onChange={e => setInterval(e.target.value)} placeholder="Interval (e.g. 1d)" />
        </div>
      )}
      <div className="panel">
        <pre>{result}</pre>
      </div>
    </div>
  );
}

export default App;
