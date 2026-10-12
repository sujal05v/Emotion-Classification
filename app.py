
import streamlit as st
import joblib
import html

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="EmotiSense | AI Emotion Detection",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    return joblib.load("emotion_model.pkl")

model = load_model()

# ---------------- CUSTOM DESIGN ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background: linear-gradient(135deg, #080d1d 0%, #10152e 55%, #171039 100%);
    color: #f4f6ff;
    font-family: 'Inter', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1120px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

#MainMenu, footer {
    visibility: hidden;
}

.hero {
    text-align: center;
    padding: 30px 10px 24px;
}

.eyebrow {
    display: inline-block;
    padding: 9px 17px;
    border: 1px solid #5141a4;
    border-radius: 50px;
    background: #1a1940;
    color: #c5b8ff;
    font-size: 13px;
    margin-bottom: 20px;
}

.hero h1 {
    font-size: clamp(34px, 5vw, 56px);
    line-height: 1.15;
    font-weight: 800;
    letter-spacing: -1.8px;
    margin: 0 0 15px;
    color: #ffffff;
}

.gradient-text {
    background: linear-gradient(90deg, #43c6ff, #8185ff, #df65ef);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    color: #aab7df;
    font-size: 16px;
    line-height: 1.8;
}

.panel {
    background: linear-gradient(135deg, #171f3b, #111a31);
    border: 1px solid #354777;
    border-radius: 22px;
    padding: 28px;
    margin-bottom: 20px;
    box-shadow: 0 15px 45px rgba(0,0,0,.18);
}

.panel h3 {
    margin: 0 0 8px;
    color: #ffffff;
}

.muted {
    color: #aab7df;
    font-size: 14px;
}

.stTextArea textarea {
    background: #0d142a !important;
    color: #f5f7ff !important;
    border: 1px solid #40558b !important;
    border-radius: 14px !important;
    font-size: 16px !important;
}

.stTextArea textarea:focus {
    border-color: #8b69ff !important;
    box-shadow: 0 0 0 2px rgba(139,105,255,.15) !important;
}

.stButton > button {
    border: none;
    border-radius: 12px;
    min-height: 48px;
    font-weight: 700;
    color: white;
    background: linear-gradient(90deg, #318cf5, #7052f5, #c13be8);
    transition: .2s ease;
}

.stButton > button:hover {
    filter: brightness(1.12);
    border: none;
    color: white;
    transform: translateY(-1px);
}

.result-card {
    background: linear-gradient(120deg, #0c302f, #11243a);
    border: 1px solid #176d68;
    border-radius: 22px;
    padding: 26px;
    margin-top: 14px;
    margin-bottom: 25px;
}

.result-label {
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #54e5c0;
    font-weight: 700;
}

.result-emotion {
    font-size: 34px;
    font-weight: 800;
    margin: 8px 0;
    color: white;
}

.feature-card {
    background: #151d36;
    border: 1px solid #29385f;
    border-radius: 17px;
    padding: 20px 16px;
    min-height: 145px;
    text-align: center;
}

.feature-icon {
    font-size: 28px;
    margin-bottom: 10px;
}

.feature-card h4 {
    font-size: 15px;
    margin: 5px 0;
    color: #ffffff;
}

.feature-card p {
    color: #aab7df;
    font-size: 12px;
    line-height: 1.6;
}

.footer {
    text-align: center;
    color: #8898c2;
    font-size: 12px;
    padding: 28px 0 8px;
}

div[data-testid="stProgress"] > div > div {
    background: linear-gradient(90deg, #20d7a0, #31c5eb);
}

@media (max-width: 640px) {
    .block-container { padding: 1rem; }
    .panel { padding: 18px; }
    .hero { padding-top: 20px; }
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
    <div class="eyebrow">✦ AI POWERED &nbsp;·&nbsp; NLP &nbsp;·&nbsp; MACHINE LEARNING</div>
    <h1>Discover the Emotion<br>
    <span class="gradient-text">in Your Text</span></h1>
    <p>Words carry feelings. Let AI help you explore the emotion behind them.</p>
</div>
""", unsafe_allow_html=True)

# ---------------- INPUT PANEL ----------------
st.markdown("""
<div class="panel">
    <h3>💬 Express yourself</h3>
    <div class="muted">Write a sentence below and let the model predict its emotion.</div>
</div>
""", unsafe_allow_html=True)

if "user_text" not in st.session_state:
    st.session_state.user_text = ""

st.text_area(
    "Your text",
    key="user_text",
    height=140,
    max_chars=500,
    placeholder="For example: I am feeling wonderful today..."
)

st.caption(f"{len(st.session_state.user_text)}/500 characters")

# Example sentences
st.markdown("**✨ Try an example**")

examples = [
    ("😊 Happy", "I am so happy today, everything is going wonderfully!"),
    ("😢 Sad", "I feel lonely and I miss my friends so much."),
    ("😠 Angry", "I am really frustrated about what happened today."),
]

example_cols = st.columns(3)

for i, (label, sentence) in enumerate(examples):
    with example_cols[i]:
        if st.button(label, key=f"example_{i}", use_container_width=True):
            st.session_state.user_text = sentence
            st.rerun()

# ---------------- PREDICTION ----------------
if st.button("✨  Detect Emotion", use_container_width=True):
    text = st.session_state.user_text.strip()

    if not text:
        st.warning("Please enter a sentence before detecting its emotion.")
    else:
        try:
            prediction = model.predict([text])[0]
            emotion = str(prediction).strip()

            # These are presentation labels, not model retraining.
            emotion_styles = {
                "joy": ("😊", "#f6bd45"),
                "happy": ("😊", "#f6bd45"),
                "happiness": ("😊", "#f6bd45"),
                "sadness": ("😢", "#65a9ff"),
                "sad": ("😢", "#65a9ff"),
                "anger": ("😠", "#ff707b"),
                "angry": ("😠", "#ff707b"),
                "love": ("❤️", "#ff75b5"),
                "fear": ("😨", "#b79aff"),
                "surprise": ("😲", "#49d8d0"),
                "neutral": ("😐", "#aab7df"),
            }

            emoji, accent = emotion_styles.get(
                emotion.lower(), ("🧠", "#a78bfa")
            )

            # Escape the label before inserting it into HTML.
            safe_emotion = html.escape(emotion.title())

            st.markdown(f"""
            <div class="result-card">
                <div class="result-label">✓ Predicted Emotion</div>
                <div style="font-size:48px;margin-top:12px">{emoji}</div>
                <div class="result-emotion">{safe_emotion}</div>
                <div class="muted">
                    Prediction generated by your trained ML model.
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Optional confidence score from the model
            if hasattr(model, "predict_proba"):
                probabilities = model.predict_proba([text])[0]
                confidence = float(max(probabilities))

                st.markdown("**Model confidence**")
                st.progress(confidence)
                st.caption(
                    f"{confidence * 100:.1f}% estimated probability. "
                    "This is not a guarantee of correctness."
                )

                with st.expander("View prediction breakdown"):
                    classifier = model[-1] if hasattr(model, "__getitem__") else None
                    classes = getattr(classifier, "classes_", None)

                    if classes is not None:
                        for label, probability in sorted(
                            zip(classes, probabilities),
                            key=lambda x: x[1],
                            reverse=True
                        ):
                            st.write(
                                f"{str(label).title()}: "
                                f"{float(probability) * 100:.1f}%"
                            )
            else:
                st.info(
                    "This model does not provide probability estimates."
                )

        except Exception as error:
            st.error("Prediction failed. Please check your saved model.")
            st.caption(str(error))

# ---------------- FEATURES ----------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### ⚡ How it works")
st.markdown(
    '<div class="muted">From raw words to an emotion prediction in seconds.</div>',
    unsafe_allow_html=True
)
st.markdown("<br>", unsafe_allow_html=True)

features = [
    ("🧹", "Text Processing", "Prepares text for analysis."),
    ("🧠", "TF-IDF", "Transforms text into numerical features."),
    ("📊", "Logistic Regression", "Predicts the emotion from text."),
    ("⚡", "Instant Results", "Displays the model prediction."),
]

cols = st.columns(4)

for col, (icon, title, description) in zip(cols, features):
    with col:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <h4>{title}</h4>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    EMOTISENSE · EMOTION CLASSIFICATION<br><br>
    Built with Python · Scikit-learn · Streamlit<br>
    Made with ❤️ by Sujal Verma
</div>
""", unsafe_allow_html=True)
