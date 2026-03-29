import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [docs, setDocs] = useState([]);

  const upload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    await axios.post("http://localhost:8000/upload", formData);
  };

  const fetchDocs = async () => {
    const res = await axios.get("http://localhost:8000/documents");
    setDocs(res.data);
  };

  useEffect(() => {
    fetchDocs();
  }, []);

  return (
    <div>
      <h1>Document Processor</h1>

      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={upload}>Upload</button>

      {docs.map(doc => (
        <div key={doc.id}>
          <p>{doc.filename} - {doc.status}</p>
        </div>
      ))}
    </div>
  );
}

export default App;
