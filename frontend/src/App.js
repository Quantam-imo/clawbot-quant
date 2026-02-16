import React, { useState } from 'react';
import axios from 'axios';
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
    if (key === 'volume') {
      const res = await axios.post('http://localhost:8000/api/volume-profile', { symbol, interval });
      if (res.data.error) {
        setResult('Error: ' + res.data.error);
      } else {
        setResult(JSON.stringify(res.data, null, 2));
      }
    } else if (key === 'gann') {
      const res = await axios.get('http://localhost:8000/api/gann');
      setResult(res.data.result);
    } else if (key === 'astrology') {
      const res = await axios.get('http://localhost:8000/api/astrology');
      setResult(res.data.result);
    } else if (key === 'news') {
      const res = await axios.post('http://localhost:8000/api/news', { symbol: newsSymbol });
      setResult(`${res.data.news}\nMarket Move: ${res.data.market_move}`);
    } else if (key === 'mentor') {
      const res = await axios.get('http://localhost:8000/api/ai-mentor/volume');
      setResult(res.data.text);
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
