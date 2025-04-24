---
title: Email PII Classifier
sdk: gradio
emoji: 💻
colorFrom: indigo
colorTo: purple
pinned: false
thumbnail: >-
  https://cdn-uploads.huggingface.co/production/uploads/6786a2f263f79d7a7035838f/Riw9F1B1o5LjZIry-b-eW.jpeg
short_description: Email classification system for a company's support team. Th
license: mit
sdk_version: 5.26.0
---
# Email Classification System for Support Team

## ✅ 1. Problem Statement

The goal of this project is to build an **email classification system** that:
- **Detects and masks Personally Identifiable Information (PII)** such as emails, phone numbers, names, and account numbers.
- **Classifies emails** into appropriate support categories like billing, technical support, general inquiry, etc.

This is particularly useful for support teams dealing with customer data, ensuring compliance with data protection laws.

---

## 📂 2. Dataset Description

We used a dataset of support emails that contain:
- **Natural language messages** written by customers.
- **Embedded PII**, such as email addresses, phone numbers, names, and IDs.
- **Labels** for the category of each email (e.g., Billing, Tech Support, Complaints, etc.)

### Key Properties:
- CSV Format
- ~X rows (based on your dataset size)
- Column: `email_text`, `label`

---

## 🧹 3. Preprocessing Steps

We performed multiple preprocessing steps to clean and prepare the data:

1. **PII Detection and Masking:**
   - Used regex patterns to find and replace:
     - Email addresses → `[EMAIL]`
     - Phone numbers → `[PHONE]`
     - Account numbers → `[ACCOUNT]`
     - Names (if found with heuristics) → `[NAME]`

2. **Text Normalization:**
   - Lowercased the text
   - Removed special characters and extra whitespace

---

## 🔍 4. Feature Engineering

Used **TF-IDF Vectorization** (`TfidfVectorizer` from Scikit-learn) to convert email text into numerical features:
- `max_features=5000`
- `ngram_range=(1, 2)`
- `stop_words='english'`

---

## 🤖 5. Model Used + Justification

We chose **Logistic Regression** as our base classifier due to:
- Good performance on text classification
- Fast training time
- Interpretability

> Model: `sklearn.linear_model.LogisticRegression`

Evaluation Metrics:
- Accuracy, Precision, Recall, F1-score on test split

---

## 🛠️ 6. API Design Explanation

Built using **FastAPI** with the following endpoints:

### `POST /predict`
- **Input**: Raw email text (JSON body)
```json
{
  "email": "Hello, I need help with my bill. My email is riya897@gmail.com."
}
```

- **Output**: 
```json
{
  "masked_email": "hello, i need help with my bill. my email is [email].",
  "category": "Billing"
}
```

---

## ⚙️ 7. Tools and Libraries Used

- **Programming Language**: Python
- **Web Framework**: FastAPI
- **NLP Tools**: Scikit-learn (TF-IDF, Logistic Regression)
- **Deployment**: Hugging Face Spaces
- **Other Tools**: Pandas, Regex, Uvicorn

---

## 🚀 8. How to Deploy

1. Push your code to [Hugging Face Spaces](https://huggingface.co/spaces).
2. Make sure your repo contains:
   - `app.py` (entrypoint)
   - `README.md` with Space metadata block (SDK: `gradio` or `fastapi`)
   - `requirements.txt` with all dependencies
   - Your model (`.pkl` file) and vectorizer
3. Space should run automatically.

---

## 🔎 9. How to Verify

- Go to Space URL:  
  `https://huggingface.co/spaces/shwetajha977/email-pii-classifier`

- Go to GitHub URL:  
  `https://github.com/shwetajha977/email-pii-classifier`


- Test with:
  - Sample support emails
  - Edge cases with multiple PII types
  - Emails without any PII


## 🚀 Features
- ✅ Classify emails (Incident, Request, Problem, etc.)
- 🔒 Mask PII (Name, Email, Phone, etc.)
- 🌐 FastAPI-based API
- 📊 Batch processing supported

## 🛠 Setup

```bash
pip install -r requirements.txt
python -c "from models import train_model; train_model()"
python app.py

---

Name: Shweta Jha</br>
Email: shwetajha977@gmail.com</br>
Thank You</br>
