Auto Tagging Tool for Research Papers Using Semantic Analysis

📌 Project Description

This project is a web-based system that analyzes research papers in PDF format and automatically generates useful information such as keywords, tags, summary, and important sentences. It uses basic Natural Language Processing (NLP) techniques to help users understand the main content of a research paper quickly without reading the entire document.

🎯 Objectives

- Extract text from research papers (PDF)
- Generate important keywords and tags
- Provide a short summary of the document
- Highlight important sentences
- Reduce manual effort in analyzing research papers

⚙️ Technologies Used

🔹 Backend (Python)

- Python
- Flask (Web Framework)
- NLTK (Text preprocessing)
- Scikit-learn (TF-IDF for keyword extraction)
- PyMuPDF (PDF text extraction)

🔹 Backend (Node.js)

- Node.js
- Express.js
- MongoDB (Database)
- Mongoose

🔹 Frontend

- HTML
- CSS
- JavaScript
- Chart.js (for data visualization)

🚀 How to Run the Project

Step 1: Install Node dependencies

npm install

Step 2: Install Python libraries

pip install flask flask-cors scikit-learn nltk pymupdf

Step 3: Run Flask backend

python app.py

Step 4: Run Node server (optional for auth/database)

node server.js

Step 5: Open in browser

http://127.0.0.1:5000

💡 Features

- Upload PDF and analyze content
- Keyword and tag generation
- Summary and important sentences
- Graphical visualization of data
- Simple and user-friendly interface
