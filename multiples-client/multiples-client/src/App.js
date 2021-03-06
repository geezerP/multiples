import "./App.css";
import { useState } from "react";
import axios from "axios";

function App() {
  const [integer, setInteger] = useState("");
  const [message, setMessage] = useState("");

  let handleSubmit = async (e) => {
    e.preventDefault();
    try {
      let payload = { "integer":parseInt(integer) };
      let res = await axios.post('http://localhost:8000/GET/', payload);

      if (res.status === 200) {
        setInteger("");
        setMessage(`${JSON.stringify(res.data)}`);
      } else {
        setMessage(`Error: ${res.status}: ${res.message}`);
      }
    } catch (err) {
      console.error(err)
      setMessage("Kindly provide an integer/number to check");
    }
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <input
          type="integer"
          value={integer}
          placeholder="Integer"
          onChange={(e) => setInteger(e.target.value)}
        />

        <button type="submit">Check Multiple</button>

        <div className="message">{message ? <p>{message}</p> : null}</div>
      </form>
    </div>
  );
}

export default App;