import { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeResume = async () => {
    if (!file && !text.trim()) {
      alert("Please upload a resume or paste resume text.");
      return;
    }

    setLoading(true);
    setResult(null);

    const formData = new FormData();
    if (file) formData.append("file", file);
    if (text) formData.append("text", text);

    try {
      const response = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      alert("Failed to analyze resume");
    }

    setLoading(false);
  };

  const normalizeScore = (score) => {
  const num = Number(score) || 0;
  return num <= 10 ? num * 10 : num;
};

const ScoreCircle = ({ score, label }) => {
  const finalScore = normalizeScore(score);

  return (
    <div className="score-card">
      <div
        className="circle"
        style={{
          background: `conic-gradient(#2563eb ${finalScore}%, #e5e7eb 0)`
        }}
      >
        <span>{finalScore}%</span>
      </div>
      <h3>{label}</h3>
    </div>
  );
};

  const ListCard = ({ title, items }) => (
    <div className="card">
      <h3>{title}</h3>
      {items && items.length > 0 ? (
        <ul>
          {items.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      ) : (
        <p>No data found</p>
      )}
    </div>
  );

  return (
    <div className="app">
      <header>
        <h1>Resume Analyzer AI</h1>
        <p>Upload your resume and get an ATS-focused professional report.</p>
      </header>

      <section className="upload-box">
        <input
          type="file"
          accept=".pdf,.docx"
          onChange={(e) => setFile(e.target.files[0])}
        />

        <textarea
          placeholder="Or paste resume text here..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        />

        <button onClick={analyzeResume} disabled={loading}>
          {loading ? "Analyzing..." : "Analyze Resume"}
        </button>
      </section>

      {result && result.error && (
        <div className="error-box">
          <h3>Error</h3>
          <p>{result.error}</p>
        </div>
      )}

      {result && !result.error && (
        <section className="dashboard">
          <div className="scores">
            <ScoreCircle score={result.ats_score} label="ATS Score" />
            <ScoreCircle score={result.overall_score} label="Overall Score" />
          </div>

          <div className="grid">
            <ListCard title="Skills Found" items={result.skills_found} />
            <ListCard title="Missing Skills" items={result.missing_skills} />
            <ListCard title="Strengths" items={result.strengths} />
            <ListCard title="Weaknesses" items={result.weaknesses} />
            <ListCard title="Improvement Suggestions" items={result.improvements} />
          </div>

          <div className="analysis">
            <div className="card">
              <h3>Experience Analysis</h3>
              <p>{result.experience_analysis}</p>
            </div>

            <div className="card">
              <h3>Education Analysis</h3>
              <p>{result.education_analysis}</p>
            </div>

            <div className="card summary">
              <h3>Final Summary</h3>
              <p>{result.final_summary}</p>
            </div>
          </div>
        </section>
      )}
    </div>
  );
}

export default App;