🔗AI-Powered News Aggregator
 This Project is a smart web app that uses semantic search with AI embeddings to help users find relevant news articles quickly. It leverages FAISS for fast similarity search and Flask for the web interface, providing an efficient, easy-to-use platform for exploring categorized news content.

🔗 Features
🔎 Semantic Search: Find news articles using AI embeddings instead of plain keywords.

⚡ Fast Indexing: Uses FAISS for high-speed similarity search.

🌐 Web Interface: Simple, clean UI built with Flask & HTML templates.

🗂️ Organized Data: News articles stored in JSON, pre-indexed for efficiency.

🔗 Technologies Used
Python 3 — main programming language.

Flask — lightweight web framework.

FAISS — Facebook AI Similarity Search for vector search.

Gunicorn — production WSGI server for deployment.

HTML/CSS — for frontend templates.

Render — for hosting your app online.

🔗 How to Set Up & Run
🔹 1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/ai_aggregator.git
cd ai_aggregator
🔹 2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔹 3. Generate the Index (if needed)
bash
Copy
Edit
python generate_index.py
🔹 4. Run the Flask App Locally
bash
Copy
Edit
python app.py
Then open http://localhost:5000 in your browser.

 Deploy Online (Recommended)
Push your code to GitHub.

Sign up on Render.

Connect your repo & deploy as a Web Service.

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

