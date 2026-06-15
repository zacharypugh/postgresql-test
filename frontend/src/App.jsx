import { React, useEffect, useState } from "react";
import AnalysisConfig from './AnalysisConfig';

function App() {

  const [sales, setSales] = useState([]);

  useEffect(() => {

    fetch("http://localhost:8000/api/sales/")
      .then(res => res.json())
      .then(data => setSales(data));

  }, []);

  return (
    <>
      <h1>Sales Data</h1>

      {sales.map(s => (
        <div key={s.id}>
          {s.customer}: ${s.amount}
        </div>
      ))}

          <div className="App">
      {/* This line is what actually draws the dropdown component on your screen */}
      <AnalysisConfig /> 
    </div>
    </>
  );
}

export default App;