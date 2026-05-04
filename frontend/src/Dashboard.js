import { useState } from "react";
import axios from "axios";

function Dashboard() {
  const [data, setData] = useState(null);

  const getSignal = async () => {
    const res = await axios.get("http://127.0.0.1:8000/signal");
    setData(res.data);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Forex AI Dashboard</h1>

      <button onClick={getSignal}>Get AI Signal</button>

      {data && (
        <div>
          <h2>Signal: {data.signal}</h2>
          <p>AI: {data.ai}</p>
        </div>
      )}
    </div>
  );
}

export default Dashboard;