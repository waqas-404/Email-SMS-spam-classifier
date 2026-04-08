# 📧 Spam Classifier using Machine Learning

A complete end-to-end Spam Detection system built using Natural Language Processing (NLP) and Machine Learning. This project classifies messages as **Spam** or **Not Spam** with high precision and reliability, and includes an interactive web interface built with Streamlit.

🔗 **Live Demo:** [spam-classifier.streamlit.app/](https://email-sms-spam-classifier-j2.streamlit.app/)


---

## 🚀 Project Overview

This project focuses on building an efficient spam classification model capable of handling real-world message variations including long texts, links, and promotional content.

The system uses advanced text preprocessing, feature extraction, and probabilistic modeling to achieve strong performance metrics.

---

## 🧠 Model Details

* **Algorithm Used:** Bernoulli Naive Bayes (BNB)
* **Vectorization:** TF-IDF Vectorizer with n-grams
* **Text Preprocessing:**

  * Lowercasing
  * Stopword removal
  * Tokenization
  * Stemming
  * Removal of punctuation and special characters

---

## 📊 Model Performance

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 98%   |
| Precision | 100%  |
| Recall    | 89%   |

### 🔍 Interpretation

* **High Precision (100%)**: The model is extremely reliable when predicting spam (no false positives).
* **Recall (89%)**: The model successfully identifies most spam messages but may miss a small portion.
* **Balanced Performance**: The model is tuned to minimize false positives while maintaining strong recall.

---

## 🧪 Testing & Verification

The model was rigorously tested using:

### ✅ Diverse Message Types

* Short and long messages
* Promotional spam
* Phishing and scam messages
* Legitimate notifications (OTP, orders, payments)
* Work and personal communication

### ✅ Edge Case Testing

* Messages containing words like "free" in non-spam context
* Long non-spam messages to avoid length bias
* Mixed language messages

### ✅ Confusion Matrix Analysis

* True Negatives (TN): High
* False Positives (FP): 0
* False Negatives (FN): Low but present
* True Positives (TP): Strong detection

This confirms the model is conservative but highly accurate when labeling spam.

---

## 🌐 Web Application

An interactive web app is built using **Streamlit**:

### Features:

* User-friendly interface
* Real-time message classification
* Instant prediction (Spam / Not Spam)
* Clean and responsive UI

---

## ☁️ Deployment

The application is deployed on **Streamlit Cloud** and can be accessed online.

---

## 📂 Project Structure

```
├── app.py                 # Streamlit application
├── model.pkl             # Trained ML model
├── appl.ipynb
├── requirements.txt
├── spam.csv              # Dataset
├── transform_text.pkl    # Transform text function
├── vectorizer.pkl        # TF-IDF vectorizer
├── utils.py              # Text preprocessing (transform_text)
├── README.md             # Project documentation
```

---

## ⚙️ How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Create virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
streamlit run app.py
```

---

## 🔮 Future Improvements

* Improve recall using threshold tuning
* Experiment with Logistic Regression and SVM
* Add more training data for better generalization
* Deploy using Docker for scalability

---

## 🙌 Acknowledgements

This project is built as part of a machine learning practice to understand text classification, model evaluation, and deployment.

---

## 📬 Contact

If you have any questions or suggestions, feel free to reach out!

---

⭐ If you found this project useful, consider giving it a star on GitHub!
