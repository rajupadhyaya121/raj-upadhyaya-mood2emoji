## Streamlit-link: https://text-mood-detector-for-kids-bxjgpnya4bcvxgz6pbkvgp.streamlit.app/

# Kid-Safe Text-Mood Detector

This project is a lightweight web tool that examines a short text input and returns a child-friendly mood output (such as happy, neutral, or sad).  
It is built using Python with Streamlit for the interface and TextBlob for simple sentiment scoring.  
The system also checks for unsafe vocabulary so it can be used comfortably by learners aged 12–16.

---

## 1. Setup and Run Instructions

Follow the steps below to run this application on your system:

1. **Clone the repository**
    ```bash
    git clone https://github.com/rajupadhyaya121/Text-mood-detector-for-kids.git
    cd Text-mood-detector-for-kids
    ```

2. **Install required packages**  
   Make sure you have Python 3.9+ installed, then run:
    ```bash
    pip install -r requirements.txt
    python -m textblob.download_corpora
    ```

3. **Launch the Streamlit app**
    ```bash
    streamlit run app.py
    ```

---

## 2. What the Project Does and How Students Benefit

**Summary:**  
The app receives a sentence typed by the user and assigns it an emotional score ranging from −1 to +1.  
Depending on this score, the text is categorized into a simple mood class.  
Before evaluation, a small filter checks for sensitive or inappropriate words to keep the experience safe for younger students.

**Key Learning Outcomes (Ages 12–16):**
- How computers analyze written language on a basic level  
- What polarity means and how it relates to sentiment  
- Introduction to rule-based decision methods  
- How numbers can be used to represent feelings or opinions  

---

## 3. Teaching Approach — Approx. 60 Minutes

### Introduction (10 min)
1. Short discussion: “Can computers understand feelings?”
2. Ask students to share sentences with different tones.

### Concept Teaching (15 min)
1. Introduce sentiment score in simple language.
2. Explain how rules divide scores into categories.
3. Introduce the idea of filtering unsafe language.

### App Demonstration (15 min)
1. Show how text is entered.
2. Display output emoji + short explanation.
3. Observe changes when wording changes.

### Student Practice (20 min)
1. Students experiment using their own short sentences.
2. Ask them to try:
   - Happy sentence
   - Sad sentence
   - Very neutral sentence
   - Slightly confusing sentence

---

## 4. Known Limitations

* **Struggles with emotional tone beyond simple wording:**  
  The app mainly checks word-level polarity, so it cannot recognize deeper emotional context (e.g., excitement behind calm wording).

* **Weak performance on playful or metaphorical text:**  
  Sentences like “My brain is on vacation today” can be interpreted incorrectly because literal meaning differs from intended feeling.

* **Limited multilingual and hybrid-language support:**  
  Inputs mixing English with another language (e.g., “Aaj mood off but trying to stay positive”) may lead to inconsistent classification.

* **Difficulty with subtle intensity differences:**  
  It treats mild expressions (“This is slightly annoying”) similarly to stronger ones because basic polarity may not reflect emotional strength.


