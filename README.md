# Auto Tagging Tool for Research Papers Using Semantic Analysis

## 📌 Project Description
This project is a web-based system that automatically generates meaningful tags from research papers in PDF format using Natural Language Processing (NLP). It helps users quickly understand the main topic of a research paper without reading the entire document.

---

## 🎯 Objectives
- Extract text from research papers (PDF)
- Generate most frequent terms
- Identify important semantic tags
- Provide intelligent suggestions (insights)
- Reduce manual effort in analyzing research papers

---

## ⚙️ Technologies Used
- Python
- Flask (Web Framework)
- spaCy (Natural Language Processing)
- PDFMiner (PDF Text Extraction)
- HTML, CSS (Frontend Design)

---

## 🚀 How to Run the Project

1. Download the project (ZIP)
2. Extract the folder
3. Open Command Prompt in the folder
4. Run the following commands:

```bash
py -3.11 -m pip install flask spacy scikit-learn nltk pdfminer.six
py -3.11 -m spacy download en_core_web_sm
py -3.11 app.py
