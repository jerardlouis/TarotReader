/*
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
*/
import React, { useState } from 'react';
import './App.css';
//import './Tarot.JSON';

function App() {
  const [tarotReading, setTarotReading] = useState(null);

  // Function to fetch a Tarot reading from the API
  const fetchTarotReading = async () => {
    try {
      const response = await fetch('/api/tarot-reading'); // Replace with your API endpoint
      if (!response.ok) {
        throw new Error('Failed to fetch Tarot reading');
      }
      const data = await response.json();
      setTarotReading(data);
    } catch (error) {
      console.error('Error fetching Tarot reading:', error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Tarot Card Reading App</h1>
        {tarotReading && (
          <div className="Tarot-Reading">
            <h2>Your Tarot Reading</h2>
            <ul>
              {tarotReading.cards.map((card, index) => (
                <li key={index}>
                  <strong>Card:</strong> {card} <br />
                  <strong>Interpretation:</strong> {tarotReading.interpretations[index]}
                </li>
              ))}
            </ul>
          </div>
        )}
        <button onClick={fetchTarotReading}>Get Tarot Reading</button>
      </header>
    </div>
  );
}

export default App;
