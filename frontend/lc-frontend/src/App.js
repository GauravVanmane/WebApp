import React, { useState } from "react";
import axios from "axios";

function App() {
  const [index, setIndex] = useState("");
  const [result, setResult] = useState("");
  const [error, setError] = useState("");

  const handleInputChange = (e) => {
    setIndex(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.get(`http://localhost:8000/solution/${index}`);
      const data = response.data;
      if (response.status === 200) {
        setResult(data.contents);
        setError("");
      } else {
        setResult("");
        setError(data[0].msg);
      }
    } catch (error) {
      setResult("");
      setError("An error occurred while fetching the data.");
    }
  };

  return (
    <div className="container">
  <h1 className="title">FastAPI and React Example</h1>
  <form className="form" onSubmit={handleSubmit}>
    <div className="form-group">
      <label className="label" htmlFor="index-input">
        Enter item index:
      </label>
      <input
        className="input"
        type="number"
        id="index-input"
        value={index}
        onChange={handleInputChange}
      />
    </div>
    <button className="button button-green" type="submit">
      Fetch Item
    </button>
  </form>
  {result && (
    <div className="result-container">
      <pre className="result-content">{result}</pre>
    </div>
  )}
  {error && <div className="error">Error: {error}</div>}
</div>

  );
}

export default App;
