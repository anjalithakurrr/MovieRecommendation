# MovieRecommendation
Content-based movie recommendation system using TF-IDF and cosine similarity, with an interactive Streamlit web app
# 🎬 MovieRecommendation

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=flat&logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=flat&logo=streamlit)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=flat)

A content-based movie recommendation system built using **TF-IDF vectorization** and **cosine similarity** on the MovieLens dataset, deployed as an interactive Streamlit web app.

---

## 🔗 Live Demo
> Coming soon — deploying on Streamlit Cloud

---

## 📌 Features
- Content-based filtering using movie genres
- TF-IDF vectorization + cosine similarity
- Top-10 similar movie recommendations
- Interactive Streamlit web interface
- Trained on MovieLens 100K dataset

---

## 🧠 How It Works
1. Movies are vectorized using TF-IDF on their genre tags
2. Cosine similarity is computed between all movie vectors
3. Given an input movie, the top-N closest matches are returned

---

## 🛠️ Tech Stack
| Tool | Purpose |
|---|---|
| Python | Core language |
| Pandas | Data loading & EDA |
| Scikit-learn | TF-IDF + cosine similarity |
| Streamlit | Web app frontend |
| MovieLens | Dataset (100K ratings) |

---

## 🚀 Run Locally
```bash
git clone https://github.com/anjalithakurrr/MovieRecommendation
cd MovieRecommendation
pip install -r requirements.txt
streamlit run app.py
```

---

## 📂 Project Structure
