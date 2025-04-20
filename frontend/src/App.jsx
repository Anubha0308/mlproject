import { useState } from "react";
import "./App.css";

function App() {
  const [text, setText] = useState("");
  const [sentiment, setSentiment] = useState("");
  const [showEmoji, setShowEmoji] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!text.trim()) return;

    setShowEmoji(false);
    setLoading(true);

    try {
      const response = await fetch("/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();
      setSentiment(data.sentiment.toLowerCase());
      setShowEmoji(true);
    } catch (error) {
      console.error("Error:", error);
    } finally {
      setLoading(false);
    }
  };

  const getEmoji = () => {
    if (sentiment === "positive")
      return <div className="text-8xl animate-bounce">😊</div>;
    if (sentiment === "negative")
      return <div className="text-8xl animate-wiggle">😢</div>;
    if (sentiment === "neutral")
      return <div className="text-8xl animate-pulse">😐</div>;
    return null;
  };

  return (
    <div className="min-h-screen bg-gradient-to-br bg-cyan-500 flex items-center justify-center px-4 py-10 text-white">
      <div className="bg-slate-800 shadow-2xl rounded-3xl p-10 max-w-2xl w-full text-center border border-slate-600">
        <h1 className="text-4xl font-extrabold text-cyan-300 mb-6">
           Sentiment Analyzer
        </h1>
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Type your thoughts here..."
          className="w-full h-40 p-4 text-white text-lg bg-slate-700 border border-slate-500 rounded-lg focus:outline-none focus:ring-2 focus:ring-cyan-400 resize-none mb-4 placeholder:text-slate-400"
        />
        <button
          onClick={handleAnalyze}
          className="bg-cyan-600 text-white font-semibold px-6 py-3 rounded-full hover:bg-cyan-500 transition duration-300 disabled:opacity-50"
          disabled={loading}
        >
          {loading ? "Analyzing..." : "Analyze"}
        </button>

        {loading && (
          <div className="mt-6 flex justify-center">
            <div className="spinner-border h-12 w-12 border-4 border-cyan-400 border-t-transparent rounded-full animate-spin"></div>
          </div>
        )}

        {showEmoji && !loading && (
          <div className="mt-8 transition-all duration-500 ease-in-out">
            {getEmoji()}
            <p className="mt-3 text-xl font-semibold text-slate-200 capitalize">
              Sentiment: <span className="text-cyan-300">{sentiment}</span>
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
