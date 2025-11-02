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

The session is designed around **Explain → Demonstrate → Explore**.

* **10 min — Introduction**
  * Discuss how machines attempt to interpret text and emotion

* **25 min — Demonstration + Explanation**
  * Show how the app processes input and assigns a mood label  
  * Use Teacher Mode to display polarity values and mapping logic  

* **20 min — Student Activity**
  * Students experiment with their own examples  
  * They try unusual sentences (including sarcastic attempts) and compare results  

* **5 min — Recap**
  * Review the simple rules used in classification  
  * Discuss why the model sometimes makes mistakes and why safety filters matter  

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


