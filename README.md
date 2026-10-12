# 😊 Emotion Classification Using Machine Learning

A Machine Learning project that predicts the emotion expressed in a text sentence using Natural Language Processing (NLP), TF-IDF vectorization, and Logistic Regression. The project is deployed using Streamlit to provide an interactive web application.

## 🚀 Live Demo

**Try the application:** [Emotion Classification App][(https://emotion-classification-v5byadkc7rbvtl2nczrbnz.streamlit.app/)]


> Replace `YOUR_STREAMLIT_APP_URL` with your actual deployed Streamlit application link.

## 📌 Project Overview

Text Emotion Classification is an NLP-based Machine Learning project that analyzes textual input and predicts its associated emotion.

The project processes text data, converts text into numerical features using TF-IDF, and uses a Logistic Regression classifier to predict the emotion. A Streamlit interface allows users to enter text and view the model's prediction.

## ✨ Features

- Predict emotions from user-provided text.
- Text preprocessing and cleaning.
- TF-IDF feature extraction.
- Machine Learning classification using Logistic Regression.
- Interactive and user-friendly Streamlit interface.
- Real-time predictions for new text input.
- Web-based access through a deployed application.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **NLP:** Text preprocessing and TF-IDF
- **Data Processing:** Pandas, NumPy
- **Model:** Logistic Regression
- **Web Framework:** Streamlit
- **Model Serialization:** Joblib
- **Development Environment:** Google Colab

## 📂 Project Structure

```text
Emotion-Classification/
│
├── app.py
├── emotion_model.pkl
├── requirements.txt
└── README.md
```

### File Description

- `app.py` — Streamlit application for text emotion prediction.
- `emotion_model.pkl` — Saved Machine Learning pipeline containing TF-IDF vectorization and the trained Logistic Regression model.
- `requirements.txt` — Python dependencies required to run the application.
- `README.md` — Project documentation.

## ⚙️ Machine Learning Workflow

The project follows these steps:

1. **Data Loading:** Load the text dataset from `train.txt`.
2. **Data Cleaning:** Convert text to lowercase and remove punctuation, numbers, and emojis.
3. **Stopword Removal:** Remove common English stopwords using NLTK.
4. **Data Splitting:** Split the dataset into training and testing sets.
5. **Feature Extraction:** Convert text into numerical features using TF-IDF.
6. **Model Training:** Train a Logistic Regression classifier.
7. **Model Evaluation:** Evaluate predictions using accuracy.
8. **Model Saving:** Save the trained pipeline using Joblib.
9. **Deployment:** Build an interactive application with Streamlit.

## 🧠 Machine Learning Model

### Logistic Regression

Logistic Regression is used as the classification algorithm to predict the emotion associated with the input text.

### TF-IDF Vectorization

Term Frequency–Inverse Document Frequency (TF-IDF) transforms text into numerical features based on the importance of words within the dataset.

The TF-IDF vectorizer and classifier are saved together in a Scikit-learn pipeline to ensure consistent feature transformation during prediction.

## 💻 Run the Project Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Navigate to the project directory

```bash
cd Emotion-Classification
```

### 3. Install the dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
python -m streamlit run app.py
```

The application will usually open at:

```text
http://localhost:8501
```

## 📦 Requirements

The `requirements.txt` file contains:

```text
streamlit
scikit-learn
pandas
joblib
```

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

Deployment steps:

1. Upload the project files to a GitHub repository.
2. Sign in to Streamlit Community Cloud using GitHub.
3. Create a new application.
4. Select the repository and deployment branch.
5. Set `app.py` as the main file path.
6. Deploy the application and access the generated public URL.

## 📊 Model Evaluation

The model is evaluated using accuracy on a held-out test dataset.

**Evaluation metric:** Accuracy

The final accuracy should be recorded from the output generated during model training. Actual performance depends on the dataset, class distribution, and preprocessing.

## 🔮 Future Improvements

- Experiment with additional classification algorithms.
- Evaluate performance using precision, recall, F1-score, and a confusion matrix.
- Improve preprocessing and handle different writing styles.
- Add visualizations for predicted emotion probabilities.
- Improve the user interface and prediction history.
- Explore advanced NLP models such as transformer-based classifiers.

## ⚠️ Limitations

- Predictions depend on the quality and coverage of the training dataset.
- Text can express multiple emotions, while the model may return only one predicted label.
- The prediction is a machine-generated estimate and may not reflect the writer's actual emotional state.
- Model performance may decrease on text that differs significantly from the training data.

## 👨‍💻 Author

**Sujal Verma**

GitHub: [@sujal05v](https://github.com/sujal05v)

---

⭐ If you find this project interesting, consider starring the repository!

*Built with Python, Machine Learning, NLP, and Streamlit.*
