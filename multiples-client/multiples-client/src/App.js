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
        setMessage(`Check Multiple Result: ${res.data.result}`);
      } else {
        setMessage("Some error occured");
      }
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
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