# 🎬 GenAI Movie Analyzer

An AI-powered movie analysis application that leverages Generative AI to extract insights, summaries, and patterns from movie data.

This project combines **LLMs (Large Language Models)** with structured movie datasets to provide intelligent analysis such as sentiment, summaries, recommendations, and trends.

---

## 🚀 Features

- 🎥 Movie Data Analysis using AI
- 🧠 LLM-powered insights (summaries, themes, sentiment)
- 🔍 Search and analyze movies dynamically
- 📊 Trend analysis (genres, popularity, ratings, etc.)
- 💬 Natural language querying (ask anything about movies)
- ⚡ Fast and scalable architecture

---

## 🛠️ Tech Stack

- **Frontend**: (Streamlit)
- **LLM**: ( Mistral )
- **Libraries**:
  - LangChain
- **Database / Storage**:
  - (ChromaDB / Vector DB — update this)

---

---

## ⚙️ Installation

```bash
git clone https://github.com/onkarlonkar9/GenAI-Movie-Analyzer.git
cd GenAI-Movie-Analyzer
```

Create Virtual Environment
```bash
python -m venv venvsource venv/bin/activate   # Linux / Macvenv\Scripts\activate      # Windows
Install Dependencies
pip install -r requirements.txt

```

🔑 Environment Variables
Create a .env file and add:
```bash
API_KEY=your_api_key_here
```
(Use your LLM provider key)

▶️ Usage
 Streamlit:
 ```bash
streamlit run app.py
```
🧠 How It Works


Load movie dataset or API data


Preprocess and clean data


Convert data into embeddings (if using vector DB)


Query LLM for:


Summaries


Insights


Recommendations




Return AI-generated analysis to user



📊 Example Use Cases


“Summarize this movie”


“Top trending genres in last decade”


“Recommend similar movies”


“Analyze sentiment of reviews”



📸 Screenshots
Add screenshots here if UI exists

🚧 Future Improvements


Add real-time movie API integration (TMDB)


Improve recommendation system


Add user authentication


Deploy on cloud (AWS / GCP / Azure)


Build full frontend dashboard



🤝 Contributing
Contributions are welcome!
fork → clone → create branch → commit → push → PR

📄 License
This project is licensed under the MIT License.

👨‍💻 Author
Onkar Lonkar


GitHub: https://github.com/onkarlonkar9



⭐ Support
If you like this project, give it a ⭐ on GitHub!
---## ⚠️ Straight feedback (don’t ignore this)Right now your project looks like:- “GenAI + movies” (generic idea)- Not clearly differentiatedTo make this resume-worthy:- Add **one strong feature**:  - RAG-based movie QA (huge upgrade)  - Real-time TMDB API + AI insights  - Personalized recommendation engineOtherwise it’s just another “LLM demo”.---If you want, drop your actual repo structure/code here — I’ll **rewrite this README specifically for your project (not template-level)** and make it stand out for recruiters.::contentReference[oaicite:0]{index=0}
